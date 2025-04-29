from unittest.mock import MagicMock, patch

import pytest

from lxml import etree

from ansible_collections.juniper.device.plugins.modules.command import main


# Mock the necessary functions and classes
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_command_text(mock_junos_module):
    # Set up the mock module instance
    mock_instance = mock_junos_module.return_value
    mock_instance.params = {
        "commands": ["show version"],
        "formats": ["text"],
        "return_output": True,
    }
    mock_instance.etree = etree
    mock_instance.pyez_exception = MagicMock()
    mock_instance.logger = MagicMock()
    mock_instance.conn_type = "local"
    mock_instance.dev = MagicMock()

    # Create a mock response that mimics the expected structure
    mock_response = etree.Element("rpc-reply")
    mock_response.text = "Output text"
    mock_instance.dev.rpc.return_value = mock_response

    # Run the main function
    with patch("sys.exit") as mock_exit:
        main()

        # Assertions to check if the main function behaves as expected
        mock_instance.fail_json.assert_not_called()
        mock_instance.exit_json.assert_called_once_with(
            command="show version",
            format="text",
            msg="The command executed successfully.",
            changed=False,
            failed=False,
            stdout="Output text",
            stdout_lines=["Output text"],
        )


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_command_xml(mock_junos_module):
    # Set up the mock module instance
    mock_instance = mock_junos_module.return_value
    mock_instance.params = {
        "commands": ["show configuration"],
        "formats": ["xml"],
        "return_output": True,
    }
    mock_instance.etree = etree
    mock_instance.pyez_exception = MagicMock()
    mock_instance.logger = MagicMock()
    mock_instance.conn_type = "local"
    mock_instance.dev = MagicMock()

    # Mock the parse_ignore_warning_option method to return None
    mock_instance.parse_ignore_warning_option.return_value = None

    # Create a mock XML response
    mock_xml_response = etree.Element("rpc-reply")
    sub_element = etree.SubElement(mock_xml_response, "configuration-information")
    sub_element.text = "Sample configuration information"
    mock_instance.dev.rpc.return_value = mock_xml_response

    # Create the same Element object used in the test
    command_element = etree.Element("command", format="xml")

    with patch.object(etree, "Element", return_value=command_element):
        # Run the main function
        with patch("sys.exit") as mock_exit:
            main()

            # Prepare expected XML output
            expected_xml_output = etree.tostring(
                mock_xml_response,
                pretty_print=True,
                encoding="unicode",
            )

            # Assertions to check if the main function behaves as expected
            mock_instance.fail_json.assert_not_called()
            mock_instance.exit_json.assert_called_once_with(
                command="show configuration",
                format="xml",
                msg="The command executed successfully.",
                changed=False,
                failed=False,
                stdout=expected_xml_output,
                stdout_lines=expected_xml_output.splitlines(),
                parsed_output=mock_instance.jxmlease.parse_etree(mock_xml_response),
            )
            mock_instance.dev.rpc.assert_called_once_with(
                command_element,
                ignore_warning=None,
                normalize=True,
            )


# Mock the necessary functions and classes
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_multiple_commands_text(mock_junos_module):
    # Set up the mock module instance
    mock_instance = mock_junos_module.return_value
    mock_instance.params = {
        "commands": ["show version", "show interfaces"],
        "formats": ["text", "text"],
        "return_output": True,
    }
    mock_instance.etree = etree
    mock_instance.pyez_exception = MagicMock()
    mock_instance.logger = MagicMock()
    mock_instance.conn_type = "local"
    mock_instance.dev = MagicMock()

    # Create mock responses for text format
    mock_response_version = etree.Element("rpc-reply")
    mock_response_version.text = "Junos version information"
    mock_response_interfaces = etree.Element("rpc-reply")
    mock_response_interfaces.text = "Interface information"

    def mock_rpc(rpc, ignore_warning=None, normalize=True):
        if rpc.text == "show version":
            return mock_response_version
        elif rpc.text == "show interfaces":
            return mock_response_interfaces

    mock_instance.dev.rpc.side_effect = mock_rpc

    with patch("sys.exit") as mock_exit:
        main()

        # Prepare expected outputs
        expected_version_output = mock_response_version.text
        expected_interfaces_output = mock_response_interfaces.text

        # Assertions to check if the main function behaves as expected
        mock_instance.fail_json.assert_not_called()
        mock_instance.exit_json.assert_called_once_with(
            results=[
                {
                    "command": "show version",
                    "format": "text",
                    "msg": "The command executed successfully.",
                    "changed": False,
                    "failed": False,
                    "stdout": expected_version_output,
                    "stdout_lines": expected_version_output.splitlines(),
                },
                {
                    "command": "show interfaces",
                    "format": "text",
                    "msg": "The command executed successfully.",
                    "changed": False,
                    "failed": False,
                    "stdout": expected_interfaces_output,
                    "stdout_lines": expected_interfaces_output.splitlines(),
                },
            ],
            changed=False,
            failed=False,
        )
        assert mock_instance.dev.rpc.call_count == 2


# Mock the necessary functions and classes
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_command_dest(mock_junos_module):
    # Set up the mock module instance
    mock_instance = mock_junos_module.return_value
    mock_instance.params = {
        "commands": ["show version"],
        "formats": ["text"],
        "return_output": True,
        "dest": "/tmp/show_version_output.txt",
    }
    mock_instance.etree = etree
    mock_instance.pyez_exception = MagicMock()
    mock_instance.logger = MagicMock()
    mock_instance.conn_type = "local"
    mock_instance.dev = MagicMock()

    # Create a mock response that mimics the expected structure
    mock_response = etree.Element("rpc-reply")
    mock_response.text = "Output text"
    mock_instance.dev.rpc.return_value = mock_response

    # Mock the save_text_output method to ensure it is called with the correct parameters
    with patch.object(mock_instance, "save_text_output") as mock_save_text_output:
        # Run the main function
        with patch("sys.exit") as mock_exit:
            main()

            # Assertions to check if the main function behaves as expected
            mock_instance.fail_json.assert_not_called()
            mock_instance.exit_json.assert_called_once_with(
                command="show version",
                format="text",
                msg="The command executed successfully.",
                changed=False,
                failed=False,
                stdout="Output text",
                stdout_lines=["Output text"],
            )
            mock_save_text_output.assert_called_once_with(
                "show version",
                "text",
                "Output text",
            )


# Updated Unit Test for `dest_dir` Parameter


@patch(
    "ansible_collections.juniper.device.plugins.module_utils.configuration.MIN_JXMLEASE_VERSION",
    new="1.0.0",
)
@patch(
    "ansible_collections.juniper.device.plugins.module_utils.juniper_junos_common.JuniperJunosModule",
)
def test_command_dest_dir(mock_junos_module):
    # Set up the mock module instance
    mock_instance = mock_junos_module.return_value
    mock_instance.params = {
        "commands": ["show version"],
        "formats": ["text"],
        "return_output": True,
        "dest_dir": "/tmp",
    }
    mock_instance.etree = etree
    mock_instance.pyez_exception = MagicMock()
    mock_instance.logger = MagicMock()
    mock_instance.conn_type = "local"
    mock_instance.dev = MagicMock()

    # Create a mock response that mimics the expected structure
    mock_response = etree.Element("rpc-reply")
    mock_response.text = "Output text"
    mock_instance.dev.rpc.return_value = mock_response

    # Mock the save_text_output method to ensure it is called with the correct parameters
    with patch.object(mock_instance, "save_text_output") as mock_save_text_output:
        # Run the main function
        with patch("sys.exit") as mock_exit:
            main()

            # Assertions to check if the main function behaves as expected
            mock_instance.fail_json.assert_not_called()
            mock_instance.exit_json.assert_called_once_with(
                command="show version",
                format="text",
                msg="The command executed successfully.",
                changed=False,
                failed=False,
                stdout="Output text",
                stdout_lines=["Output text"],
            )
            mock_save_text_output.assert_called_once_with(
                "show version",
                "text",
                "Output text",
            )


if __name__ == "__main__":
    pytest.main([__file__])
