from unittest.mock import patch

from ansible_collections.juniper.device.plugins.modules.file_copy import main


# Helper to provide default valid params with optional overrides
def build_params(**overrides):
    base = {
        "local_dir": "/local",
        "remote_dir": "/remote",
        "file": "test.txt",
        "action": "put",
        "protocol": "scp",
        "checksum": True,
        "transfer_filename": None,
    }
    base.update(overrides)
    return base


# ---- PUT TEST CASES ----


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule"
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_put_scp_with_checksum(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = build_params()
    mock_instance.scp_file_copy_put.return_value = ("SCP put with checksum", True)

    with patch("sys.exit"):
        main()

    mock_instance.scp_file_copy_put.assert_called_once_with(
        "/local/test.txt", "/remote/test.txt"
    )
    mock_instance.exit_json.assert_called_once_with(
        msg="SCP put with checksum",
        changed=True,
        failed=False,
    )


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule"
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_put_scp_without_checksum(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = build_params(checksum=False)
    mock_instance.scp_file_copy_put_without_checksum.return_value = (
        "SCP put without checksum",
        True,
    )

    with patch("sys.exit"):
        main()

    mock_instance.scp_file_copy_put_without_checksum.assert_called_once_with(
        "/local/test.txt", "/remote/test.txt"
    )
    mock_instance.exit_json.assert_called_once_with(
        msg="SCP put without checksum",
        changed=True,
        failed=False,
    )


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule"
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_put_ftp_with_checksum(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = build_params(protocol="ftp")
    mock_instance.ftp_file_copy_put.return_value = ("FTP put with checksum", True)

    with patch("sys.exit"):
        main()

    mock_instance.ftp_file_copy_put.assert_called_once_with(
        "/local/test.txt", "/remote/test.txt"
    )
    mock_instance.exit_json.assert_called_once_with(
        msg="FTP put with checksum",
        changed=True,
        failed=False,
    )


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule"
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_put_ftp_without_checksum(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = build_params(protocol="ftp", checksum=False)
    mock_instance.ftp_file_copy_put_without_checksum.return_value = (
        "FTP put without checksum",
        True,
    )

    with patch("sys.exit"):
        main()

    mock_instance.ftp_file_copy_put_without_checksum.assert_called_once_with(
        "/local/test.txt", "/remote/test.txt"
    )
    mock_instance.exit_json.assert_called_once_with(
        msg="FTP put without checksum",
        changed=True,
        failed=False,
    )


# ---- GET TEST CASES ----


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule"
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_get_scp_with_checksum(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = build_params(action="get")
    mock_instance.scp_file_copy_get.return_value = ("SCP get with checksum", True)

    with patch("sys.exit"):
        main()

    mock_instance.scp_file_copy_get.assert_called_once_with(
        "/remote/test.txt", "/local/test.txt"
    )
    mock_instance.exit_json.assert_called_once_with(
        msg="SCP get with checksum",
        changed=True,
        failed=False,
    )


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule"
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_get_scp_without_checksum(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = build_params(action="get", checksum=False)
    mock_instance.scp_file_copy_get_without_checksum.return_value = (
        "SCP get without checksum",
        True,
    )

    with patch("sys.exit"):
        main()

    mock_instance.scp_file_copy_get_without_checksum.assert_called_once_with(
        "/remote/test.txt", "/local/test.txt"
    )
    mock_instance.exit_json.assert_called_once_with(
        msg="SCP get without checksum",
        changed=True,
        failed=False,
    )


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule"
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_get_ftp_with_checksum(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = build_params(action="get", protocol="ftp")
    mock_instance.ftp_file_copy_get.return_value = ("FTP get with checksum", True)

    with patch("sys.exit"):
        main()

    mock_instance.ftp_file_copy_get.assert_called_once_with(
        "/remote/test.txt", "/local/test.txt"
    )
    mock_instance.exit_json.assert_called_once_with(
        msg="FTP get with checksum",
        changed=True,
        failed=False,
    )


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule"
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_get_ftp_without_checksum(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = build_params(action="get", protocol="ftp", checksum=False)
    mock_instance.ftp_file_copy_get_without_checksum.return_value = (
        "FTP get without checksum",
        True,
    )

    with patch("sys.exit"):
        main()

    mock_instance.ftp_file_copy_get_without_checksum.assert_called_once_with(
        "/remote/test.txt", "/local/test.txt"
    )
    mock_instance.exit_json.assert_called_once_with(
        msg="FTP get without checksum",
        changed=True,
        failed=False,
    )


# ---- TRANSFER_FILENAME TEST CASE ----


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule"
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_transfer_filename_put(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = build_params(transfer_filename="renamed.txt")
    mock_instance.scp_file_copy_put.return_value = ("Renamed put OK", True)

    with patch("sys.exit"):
        main()

    mock_instance.scp_file_copy_put.assert_called_once_with(
        "/local/test.txt", "/remote/renamed.txt"
    )
    mock_instance.exit_json.assert_called_once_with(
        msg="Renamed put OK",
        changed=True,
        failed=False,
    )


# ---- EDGE CASES ----


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule"
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
def test_invalid_action(mock_junos_module):
    mock_instance = mock_junos_module.return_value
    mock_instance.params = build_params(action="delete")  # Invalid action

    with patch("sys.exit"):
        main()

    # This will likely not raise, but will skip both branches
    mock_instance.exit_json.assert_called_once_with(msg="", changed=False, failed=False)