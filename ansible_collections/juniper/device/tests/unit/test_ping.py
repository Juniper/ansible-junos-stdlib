from types import SimpleNamespace
from unittest.mock import patch

import pytest

from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator
from jnpr.junos import Device
from lxml import etree

from ansible_collections.juniper.device.plugins.connection.pyez import Connection
from ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common import (
    JuniperJunosModule,
)
from ansible_collections.juniper.device.plugins.modules.ping import main


# Helper function to create a mock response for the ping action
def create_ping_response(success=True):
    return {
        "msg": "Ping successful" if success else "Ping failed",
        "changed": False,
        "failed": not success,
        "success": success,
    }


@pytest.mark.parametrize(
    ("inet", "expected_rpc"),
    [(True, {"inet": True}), (False, {}), (None, {})],
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_ping_inet_option(mock_junos_module, inet, expected_rpc):
    mock_instance = mock_junos_module.return_value
    params = {"dest": "example.com"}
    if inet is not None:
        params["inet"] = inet

    def create_module(argument_spec, **kwargs):
        validated = ModuleArgumentSpecValidator(argument_spec).validate(params)
        assert not validated.error_messages
        mock_instance.params = validated.validated_parameters
        return mock_instance

    mock_junos_module.side_effect = create_module
    mock_instance.ping.return_value = create_ping_response()

    main()

    rpc_params = mock_instance.ping.call_args.args[0]
    assert rpc_params == {"host": "example.com", "count": "5", "rapid": True, **expected_rpc}
    assert mock_instance.ping.call_args.kwargs["results"]["inet"] is (inet is True)


@pytest.mark.parametrize("conn_type", ["local", "pyez"])
@pytest.mark.parametrize("inet", [True, False, None])
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_ping_inet_rpc_xml(mock_junos_module, conn_type, inet):
    module = mock_junos_module.return_value
    params = {"dest": "example.com", "acceptable_percent_loss": 100}
    if inet is not None:
        params["inet"] = inet

    def create_module(argument_spec, **kwargs):
        validated = ModuleArgumentSpecValidator(argument_spec).validate(params)
        assert not validated.error_messages
        module.params = validated.validated_parameters
        return module

    mock_junos_module.side_effect = create_module
    module.ping.side_effect = lambda *args, **kwargs: JuniperJunosModule.ping(
        module, *args, **kwargs
    )
    module.conn_type = conn_type
    module.etree = etree
    device = Device(host="example.com")
    module.dev = device
    module._pyez_conn.ping_device.side_effect = lambda **kwargs: Connection.ping_device(
        SimpleNamespace(dev=device), **kwargs
    )
    response = etree.fromstring(
        b"<ping-results><probe-results-summary><packet-loss>100</packet-loss>"
        b"<probes-sent>5</probes-sent><responses-received>0</responses-received>"
        b"</probe-results-summary></ping-results>"
    )

    with patch.object(device, "execute", return_value=response) as execute:
        main()

    rpc = execute.call_args.args[0]
    assert rpc.tag == "ping"
    assert rpc.findtext("host") == "example.com"
    assert (rpc.find("inet") is not None) is (inet is True)
    assert module.exit_json.call_args.kwargs["inet"] is (inet is True)


# Test for valid ping parameters
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_ping_valid_ping_params(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = {
        "dest": "8.8.8.8",
        "acceptable_percent_loss": 0,
        "count": 5,
        "rapid": True,
        "ttl": 64,
        "size": 100,
        "source": "192.168.1.1",
        "interface": "ge-0/0/0",
        "routing_instance": "default",
    }
    mock_instance.ping.return_value = create_ping_response(success=True)

    with patch("sys.exit") as mock_exit:
        results = {
            "msg": "",
            "changed": False,
            "failed": True,
            "dest": "8.8.8.8",
            "acceptable_percent_loss": "0",
            "count": "5",
            "rapid": True,
            "ttl": "64",
            "size": "100",
            "do_not_fragment": None,
            "inet": None,
            "source": "192.168.1.1",
            "interface": "ge-0/0/0",
            "routing_instance": "default",
            "timeout": "None",
            "host": "8.8.8.8",
            "dest_ip": "8.8.8.8",
            "source_ip": "192.168.1.1",
        }
        main()
        mock_instance.ping.assert_called_once_with(
            {
                "host": "8.8.8.8",
                "count": "5",
                "rapid": True,
                "ttl": "64",
                "size": "100",
                "source": "192.168.1.1",
                "interface": "ge-0/0/0",
                "routing_instance": "default",
            },
            acceptable_percent_loss=0,
            results=results,
        )
        mock_instance.exit_json.assert_called_once_with(
            msg="Ping successful",
            changed=False,
            failed=False,
            success=True,
        )


# Test for invalid acceptable_percent_loss
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_ping_invalid_acceptable_percent_loss(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = {
        "dest": "8.8.8.8",
        "acceptable_percent_loss": 150,  # Invalid percentage
    }

    with patch("sys.exit") as mock_exit:
        main()
        mock_instance.fail_json.assert_called_once_with(
            msg="The value of the acceptable_percent_lossoption (150) is a percentage and must have a value between 0 and 100.",
        )


# Test for ping failure
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_ping_ping_failure(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = {
        "dest": "8.8.8.8",
        "acceptable_percent_loss": 0,
        "count": 5,
        "rapid": True,
        "ttl": 64,
        "size": 100,
        "source": "192.168.1.1",
        "interface": "ge-0/0/0",
        "routing_instance": "default",
    }
    mock_instance.ping.return_value = create_ping_response(success=False)

    with patch("sys.exit") as mock_exit:
        results = {
            "msg": "",
            "changed": False,
            "failed": True,
            "dest": "8.8.8.8",
            "acceptable_percent_loss": "0",
            "count": "5",
            "rapid": True,
            "ttl": "64",
            "size": "100",
            "do_not_fragment": None,
            "inet": None,
            "source": "192.168.1.1",
            "interface": "ge-0/0/0",
            "routing_instance": "default",
            "timeout": "None",
            "host": "8.8.8.8",
            "dest_ip": "8.8.8.8",
            "source_ip": "192.168.1.1",
        }
        main()
        mock_instance.ping.assert_called_once_with(
            {
                "host": "8.8.8.8",
                "count": "5",
                "rapid": True,
                "ttl": "64",
                "size": "100",
                "source": "192.168.1.1",
                "interface": "ge-0/0/0",
                "routing_instance": "default",
            },
            acceptable_percent_loss=0,
            results=results,
        )
        mock_instance.exit_json.assert_called_once_with(
            msg="Ping failed",
            changed=False,
            failed=True,
            success=False,
        )


if __name__ == "__main__":
    pytest.main([__file__])
