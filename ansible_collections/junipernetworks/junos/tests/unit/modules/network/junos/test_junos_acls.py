# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from ansible_collections.juniper.device.plugins.modules import junos_acls
from ansible_collections.junipernetworks.junos.tests.unit.modules.utils import set_module_args

from .junos_module import TestJunosModule


class TestJunosAclsModule(TestJunosModule):
    module = junos_acls

    def test_junos_acls_parsed_single_prefix_list_normalized(self):
        parsed_str = """
            <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
                <configuration>
                    <firewall>
                        <family>
                            <inet>
                                <filter>
                                    <name>ALL-ATTRS-ACL</name>
                                    <term>
                                        <name>t40-src-prefix-list</name>
                                        <from>
                                            <source-prefix-list>TRUSTED-SOURCES</source-prefix-list>
                                            <destination-prefix-list>DEST-TRUSTED</destination-prefix-list>
                                            <destination-address>
                                                <name>10.10.10.0/24</name>
                                            </destination-address>
                                            <protocol>tcp</protocol>
                                        </from>
                                        <then>
                                            <accept/>
                                        </then>
                                    </term>
                                </filter>
                            </inet>
                        </family>
                    </firewall>
                </configuration>
            </rpc-reply>
        """

        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)

        ace = result["parsed"][0]["acls"][0]["aces"][0]
        self.assertEqual(ace["source"]["prefix_list"], [{"name": "TRUSTED-SOURCES"}])
        self.assertEqual(ace["destination"]["prefix_list"], [{"name": "DEST-TRUSTED"}])

    def test_junos_acls_parsed_multiple_prefix_lists_preserved(self):
        parsed_str = """
            <rpc-reply message-id="urn:uuid:ad0f3f68-bd5a-4e15-8f5e-012345678901">
                <configuration>
                    <firewall>
                        <family>
                            <inet>
                                <filter>
                                    <name>ALL-ATTRS-ACL</name>
                                    <term>
                                        <name>t41-src-prefix-list</name>
                                        <from>
                                            <source-prefix-list>TRUSTED-SOURCES-1</source-prefix-list>
                                            <source-prefix-list>TRUSTED-SOURCES-2</source-prefix-list>
                                            <destination-prefix-list>DEST-TRUSTED-1</destination-prefix-list>
                                            <destination-prefix-list>DEST-TRUSTED-2</destination-prefix-list>
                                            <destination-address>
                                                <name>10.20.20.0/24</name>
                                            </destination-address>
                                            <protocol>tcp</protocol>
                                        </from>
                                        <then>
                                            <accept/>
                                        </then>
                                    </term>
                                </filter>
                            </inet>
                        </family>
                    </firewall>
                </configuration>
            </rpc-reply>
        """

        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)

        ace = result["parsed"][0]["acls"][0]["aces"][0]
        self.assertEqual(
            ace["source"]["prefix_list"],
            [{"name": "TRUSTED-SOURCES-1"}, {"name": "TRUSTED-SOURCES-2"}],
        )
        self.assertEqual(
            ace["destination"]["prefix_list"],
            [{"name": "DEST-TRUSTED-1"}, {"name": "DEST-TRUSTED-2"}],
        )
