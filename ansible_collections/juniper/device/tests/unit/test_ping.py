from unittest.mock import patch

import pytest

from ansible_collections.juniper.device.plugins.modules.ping import main


# Helper function to create a mock response for the ping action
def create_ping_response(success=True):
    return {
        "msg": "Ping successful" if success else "Ping failed",
        "changed": False,
        "failed": not success,
        "success": success,
    }


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
