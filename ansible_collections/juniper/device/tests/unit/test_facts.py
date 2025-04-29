from unittest.mock import MagicMock, patch

import pytest

from ansible_collections.juniper.device.plugins.modules.facts import (
    get_facts_dict,
    main,
)


@pytest.fixture
def mock_junos_module():
    mock_module = MagicMock()
    mock_module.conn_type = "local"
    mock_module.dev = MagicMock()
    mock_module.dev.facts = {
        "hostname": "router1",
        "version": "18.1R3",
        "2RE": True,
        "version_info": MagicMock(),
        "junos_info": {
            "re0": {"object": MagicMock()},
            "re1": {"object": MagicMock()},
        },
    }
    mock_module.dev.re_name = "re0"
    mock_module.dev.master = "re0"
    return mock_module


def test_get_facts_dict(mock_junos_module):
    facts = get_facts_dict(mock_junos_module)
    assert facts["hostname"] == "router1"
    assert facts["version"] == "18.1R3"
    assert facts["has_2RE"] is True
    assert "2RE" not in facts
    assert isinstance(facts["version_info"], dict)
    assert isinstance(facts["junos_info"]["re0"]["object"], dict)
    assert isinstance(facts["junos_info"]["re1"]["object"], dict)
    assert facts["re_name"] == "re0"
    assert facts["master_state"] == "re0"


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_facts(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params.get.return_value = "/tmp"
    mock_instance.etree = MagicMock()
    mock_instance.dev = MagicMock()
    mock_instance.dev.facts = {"hostname": "router1"}
    mock_instance.dev.rpc.get_chassis_inventory.return_value = (
        "<inventory>data</inventory>"
    )
    mock_instance.get_facts.return_value = {"hostname": "router1"}
    mock_instance.get_configuration.side_effect = [("<config_data>", "<config_parsed>")]

    with patch("builtins.open", new_callable=MagicMock):
        with patch("sys.exit") as mock_exit:
            main()
            mock_instance.exit_json.assert_called_once_with(
                changed=False,
                failed=False,
                ansible_facts={"junos": mock_instance.get_facts.return_value},
                facts=mock_instance.get_facts.return_value,
            )


if __name__ == "__main__":
    pytest.main([__file__])
