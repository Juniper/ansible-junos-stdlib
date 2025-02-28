from unittest.mock import patch
import pytest
from ansible_collections.juniper.device.plugins.modules.file_copy import main


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule"
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_file_copy_put(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = {
        "local_dir": "/local",
        "remote_dir": "/remote",
        "file": "testfile.txt",
        "action": "put",
    }

    mock_instance.scp_file_copy_put.return_value = ("File copied successfully", True)

    with patch("sys.exit") as mock_exit:
        main()

        mock_instance.scp_file_copy_put.assert_called_once_with(
            "/local/testfile.txt", "/remote/testfile.txt"
        )
        mock_instance.exit_json.assert_called_once_with(
            msg="File copied successfully", changed=True, failed=False
        )


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule"
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_file_copy_get(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = {
        "local_dir": "/local",
        "remote_dir": "/remote",
        "file": "testfile.txt",
        "action": "get",
    }

    mock_instance.scp_file_copy_get.return_value = ("File copied successfully", True)

    with patch("sys.exit") as mock_exit:
        main()

        mock_instance.scp_file_copy_get.assert_called_once_with(
            "/remote/testfile.txt", "/local/testfile.txt"
        )
        mock_instance.exit_json.assert_called_once_with(
            msg="File copied successfully", changed=True, failed=False
        )


if __name__ == "__main__":
    pytest.main([__file__])
