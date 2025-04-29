from unittest.mock import MagicMock, patch

import pytest

from ansible_collections.juniper.device.plugins.modules.system import main


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_reboot_action(MockJuniperJunosModule):
    # Create a mock instance of JuniperJunosModule
    mock_module = MockJuniperJunosModule.return_value
    mock_module.params = {
        "action": "reboot",
        "at": "now",
        "in_min": 0,
        "all_re": True,
        "other_re": False,
        "vmhost": False,
        "media": False,
        "member_id": None,
    }

    mock_module.check_mode = False
    mock_module.conn_type = "local"
    mock_module.dev = MagicMock()
    mock_module.dev.timeout = 30
    mock_module._pyez_conn = MagicMock()
    mock_module.sw = MagicMock()
    mock_module.pyez_exception = MagicMock()

    # Simulate the expected behavior of the module
    mock_module._pyez_conn.system_api.return_value = "Reboot initiated."
    mock_module.sw.reboot.return_value = "Reboot initiated."

    # Execute the main function
    main()

    # Assert expected results
    mock_module.exit_json.assert_called_once_with(
        changed=True,
        msg="reboot successfully initiated. Response got Reboot initiated.",
        reboot=True,
        action="reboot",
        all_re=True,
        other_re=False,
        media=False,
        vmhost=False,
        failed=False,
    )


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_shutdown_action(MockJuniperJunosModule):
    # Create a mock instance of JuniperJunosModule
    mock_module = MockJuniperJunosModule.return_value
    mock_module.params = {
        "action": "shutdown",
        "at": "now",
        "in_min": 0,
        "all_re": True,
        "other_re": False,
        "vmhost": False,
        "media": False,
        "member_id": None,
    }

    mock_module.check_mode = False
    mock_module.conn_type = "local"
    mock_module.dev = MagicMock()
    mock_module.dev.timeout = 30
    mock_module._pyez_conn = MagicMock()
    mock_module.sw = MagicMock()
    mock_module.pyez_exception = MagicMock()

    # Simulate the expected behavior of the module
    mock_module._pyez_conn.system_api.return_value = "Shutdown initiated."
    mock_module.sw.poweroff.return_value = "Shutdown initiated."

    # Execute the main function
    main()

    # Assert expected results
    mock_module.exit_json.assert_called_once_with(
        changed=True,
        msg="shutdown successfully initiated. Response got Shutdown initiated.",
        reboot=False,
        action="shutdown",
        all_re=True,
        other_re=False,
        media=False,
        vmhost=False,
        failed=False,
    )


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_zeroize_action(MockJuniperJunosModule):
    # Create a mock instance of JuniperJunosModule
    mock_module = MockJuniperJunosModule.return_value
    mock_module.params = {
        "action": "zeroize",
        "at": None,
        "in_min": 0,
        "all_re": True,
        "other_re": False,
        "vmhost": False,
        "media": True,
        "member_id": None,
    }

    mock_module.check_mode = False
    mock_module.conn_type = "local"
    mock_module.dev = MagicMock()
    mock_module.dev.timeout = 30
    mock_module._pyez_conn = MagicMock()
    mock_module.sw = MagicMock()
    mock_module.pyez_exception = MagicMock()

    # Simulate the expected behavior of the module
    mock_module._pyez_conn.system_api.return_value = "Zeroize initiated."
    mock_module.sw.zeroize.return_value = "Zeroize initiated."

    # Execute the main function
    main()

    # Assert expected results
    mock_module.exit_json.assert_called_once_with(
        changed=True,
        msg="zeroize successfully initiated. Response got Zeroize initiated.",
        reboot=False,
        action="zeroize",
        all_re=True,
        other_re=False,
        media=True,
        vmhost=False,
        failed=False,
    )


if __name__ == "__main__":
    pytest.main()
