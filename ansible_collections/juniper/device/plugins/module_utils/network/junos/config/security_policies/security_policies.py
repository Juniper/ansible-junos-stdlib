#
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos_security_policies class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    build_child_xml_node,
    build_root_xml_node,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    remove_empties,
)

from ansible_collections.juniper.device.plugins.module_utils.network.junos.facts.facts import (
    Facts,
)
from ansible_collections.juniper.device.plugins.module_utils.network.junos.junos import (
    commit_configuration,
    discard_changes,
    load_config,
    locked_config,
    tostring,
)


class Security_policies(ConfigBase):
    """
    The junos_security_policies class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["security_policies"]

    def __init__(self, module):
        super(Security_policies, self).__init__(module)

    def get_security_policies_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        security_policies_facts = facts["ansible_network_resources"].get(
            "security_policies",
        )
        if not security_policies_facts:
            return {}
        return security_policies_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}

        warnings = list()

        if self.state in self.ACTION_STATES or self.state == "purged":
            existing_security_policies_facts = self.get_security_policies_facts()
        else:
            existing_security_policies_facts = {}
        if self.state == "gathered":
            existing_security_policies_facts = self.get_security_policies_facts()
            result["gathered"] = existing_security_policies_facts

        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_security_policies_facts(
                data=running_config,
            )

        elif self.state == "rendered":
            config_xmls = self.set_config(existing_security_policies_facts)
            if config_xmls:
                result["rendered"] = config_xmls

        else:
            diff = None
            config_xmls = self.set_config(existing_security_policies_facts)
            with locked_config(self._module):
                diff = load_config(self._module, config_xmls, [])

                commit = not self._module.check_mode
                if diff:
                    if commit:
                        commit_configuration(self._module)
                    else:
                        discard_changes(self._module)
                    result["changed"] = True

                    if self._module._diff:
                        result["diff"] = {"prepared": diff}

            result["commands"] = config_xmls

            changed_security_policies_facts = self.get_security_policies_facts()

            result["before"] = existing_security_policies_facts
            if result["changed"]:
                result["after"] = changed_security_policies_facts

            result["warnings"] = warnings
        return result

    def set_config(self, existing_security_policies_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_security_policies_facts
        resp = self.set_state(want, have)
        return resp

    def set_state(self, want, have):
        """Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        self.root = build_root_xml_node("security")
        state = self._module.params["state"]
        if state in ("merged", "replaced", "rendered", "overridden") and not want:
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    state,
                ),
            )
        config_xmls = []
        if state == "overridden":
            config_xmls = self._state_overridden(want, have)
        elif state == "deleted":
            config_xmls = self._state_deleted(want, have)
        elif state in ("merged", "rendered"):
            config_xmls = self._state_merged(want, have)
        elif state == "replaced":
            config_xmls = self._state_replaced(want, have)
        for xml in config_xmls:
            self.root.append(xml)
        return tostring(self.root)

    def _state_replaced(self, want, have):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        security_policies_xml = []
        security_policies_xml.extend(self._state_deleted(want, have))
        security_policies_xml.extend(self._state_merged(want, have))
        return security_policies_xml

    def _state_overridden(self, want, have):
        """The command generator when state is overridden

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        security_policies_xml = []
        security_policies_xml.extend(self._state_deleted(want, have))
        security_policies_xml.extend(self._state_merged(want, have))
        return security_policies_xml

    def _state_merged(self, want, _have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        security_policies_xml = []
        want = remove_empties(want)
        security_policies_node = build_root_xml_node("policies")

        def build_policies(node, policies):
            for policy in policies:
                policy_node = build_child_xml_node(node, "policy")

                build_child_xml_node(policy_node, "name", policy["name"])

                if "description" in policy:
                    build_child_xml_node(
                        policy_node,
                        "description",
                        policy["description"],
                    )

                if "scheduler_name" in policy:
                    build_child_xml_node(
                        policy_node,
                        "scheduler-name",
                        policy["scheduler_name"],
                    )

                # add match criteria node
                match_node = build_child_xml_node(policy_node, "match")
                match = policy["match"]

                for source_address in match["source_address"]:
                    if source_address == "any_ipv6":
                        build_child_xml_node(
                            match_node,
                            "source-address",
                            "any-ipv6",
                        )
                    elif source_address == "any_ipv4":
                        build_child_xml_node(
                            match_node,
                            "source-address",
                            "any-ipv4",
                        )
                    elif source_address == "any":
                        build_child_xml_node(
                            match_node,
                            "source-address",
                            "any",
                        )
                    elif source_address == "addresses":
                        for address in match["source_address"]["addresses"]:
                            build_child_xml_node(
                                match_node,
                                "source-address",
                                address,
                            )

                if "source_address_excluded" in match:
                    build_child_xml_node(match_node, "source-address-excluded")

                for destination_address in match["destination_address"]:
                    if destination_address == "any_ipv6":
                        build_child_xml_node(
                            match_node,
                            "destination-address",
                            "any-ipv6",
                        )
                    elif destination_address == "any_ipv4":
                        build_child_xml_node(
                            match_node,
                            "destination-address",
                            "any-ipv4",
                        )
                    elif destination_address == "any":
                        build_child_xml_node(
                            match_node,
                            "destination-address",
                            "any",
                        )
                    elif destination_address == "addresses":
                        for address in match["destination_address"]["addresses"]:
                            build_child_xml_node(
                                match_node,
                                "destination-address",
                                address,
                            )
                    else:
                        pass

                if "destination_address_excluded" in match:
                    build_child_xml_node(
                        match_node,
                        "destination-address-excluded",
                    )

                for application in match["application"]:
                    if application == "any":
                        build_child_xml_node(match_node, "application", "any")
                    elif application == "names":
                        for name in match["application"]["names"]:
                            build_child_xml_node(
                                match_node,
                                "application",
                                name,
                            )

                if "source_end_user_profile" in match:
                    build_child_xml_node(
                        match_node,
                        "source-end-user-profile",
                        match["source_end_user_profile"],
                    )

                if "source_identity" in match:
                    source_identities = match["source_identity"]
                    for source_identity in source_identities:
                        if source_identity == "any":
                            build_child_xml_node(
                                match_node,
                                "source-identity",
                                "any",
                            )
                        if source_identity == "authenticated_user":
                            build_child_xml_node(
                                match_node,
                                "source-identity",
                                "authenticated-user",
                            )
                        if source_identity == "unauthenticated_user":
                            build_child_xml_node(
                                match_node,
                                "source-identity",
                                "unauthenticated-user",
                            )
                        if source_identity == "unknown_user":
                            build_child_xml_node(
                                match_node,
                                "source-identity",
                                "unknown-user",
                            )
                        elif source_identity == "names":
                            for name in match["source_identity"]["names"]:
                                build_child_xml_node(
                                    match_node,
                                    "source-identity",
                                    name,
                                )

                if "url_category" in match:
                    url_categories = match["url_category"]
                    for url_category in url_categories:
                        if url_category == "any":
                            build_child_xml_node(
                                match_node,
                                "url-category",
                                "any",
                            )
                        elif url_category == "none":
                            build_child_xml_node(
                                match_node,
                                "url-category",
                                "none",
                            )
                        elif url_category == "names":
                            for name in match["url_category"]["names"]:
                                build_child_xml_node(
                                    match_node,
                                    "url-category",
                                    name,
                                )

                if "dynamic_application" in match:
                    dynamic_applications = match["dynamic_application"]
                    for dynamic_application in dynamic_applications:
                        if dynamic_application == "any":
                            build_child_xml_node(
                                match_node,
                                "dynamic-application",
                                "any",
                            )
                        elif dynamic_application == "none":
                            build_child_xml_node(
                                match_node,
                                "dynamic-application",
                                "none",
                            )
                        elif dynamic_application == "names":
                            for name in match["dynamic_application"]["names"]:
                                build_child_xml_node(
                                    match_node,
                                    "dynamic-application",
                                    name,
                                )

                # add action node
                then_node = build_child_xml_node(policy_node, "then")
                then = policy["then"]

                if "deny" in then:
                    build_child_xml_node(then_node, "deny")

                if "count" in then:
                    build_child_xml_node(then_node, "count", " ")

                if "log" in then:
                    log_node = build_child_xml_node(then_node, "log")
                    if policy["then"]["log"] and "session_init" in policy["then"]["log"]:
                        build_child_xml_node(log_node, "session-init")
                    if policy["then"]["log"] and "session_close" in policy["then"]["log"]:
                        build_child_xml_node(log_node, "session-close")

                if "reject" in then:
                    reject = then["reject"]
                    reject_node = build_child_xml_node(
                        then_node,
                        "reject",
                        " ",
                    )
                    if reject and "profile" in reject:
                        build_child_xml_node(
                            reject_node,
                            "profile",
                            reject["profile"],
                        )
                    if reject and "ssl_proxy" in reject:
                        ssl_node = build_child_xml_node(
                            reject_node,
                            "ssl-proxy",
                            " ",
                        )
                        if reject["ssl_proxy"] and "profile_name" in reject["ssl_proxy"]:
                            build_child_xml_node(
                                ssl_node,
                                "profile-name",
                                reject["ssl_proxy"]["profile_name"],
                            )

                if "permit" in then:
                    permit_node = build_child_xml_node(then_node, "permit")
                    permit = then["permit"]
                    if "application_services" in permit:
                        application_services = permit["application_services"]
                        application_services_node = build_child_xml_node(
                            permit_node,
                            "application-services",
                        )
                        if "advanced_anti_malware_policy" in application_services:
                            build_child_xml_node(
                                application_services_node,
                                "advanced-anti-malware-policy",
                                application_services["advanced_anti_malware_policy"],
                            )
                        if "application_traffic_control_rule_set" in application_services:
                            application_traffic_control_node = build_child_xml_node(
                                application_services_node,
                                "application-traffic-control",
                            )
                            build_child_xml_node(
                                application_traffic_control_node,
                                "rule-set",
                                application_services["application_traffic_control_rule_set"],
                            )
                        if "gprs_gtp_profile" in application_services:
                            build_child_xml_node(
                                application_services_node,
                                "gprs-gtp-profile",
                                application_services["gprs_gtp_profile"],
                            )
                        if "gprs_sctp_profile" in application_services:
                            build_child_xml_node(
                                application_services_node,
                                "gprs-sctp-profile",
                                application_services["gprs_sctp_profile"],
                            )
                        if "icap_redirect" in application_services:
                            build_child_xml_node(
                                application_services_node,
                                "icap-redirect",
                                application_services["icap_redirect"],
                            )
                        if "idp" in application_services:
                            build_child_xml_node(
                                application_services_node,
                                "idp",
                            )
                        if "idp_policy" in application_services:
                            build_child_xml_node(
                                application_services_node,
                                "idp-policy",
                                application_services["idp_policy"],
                            )
                        if "redirect_wx" in application_services:
                            build_child_xml_node(
                                application_services_node,
                                "redirect-wx",
                            )
                        if "reverse_redirect_wx" in application_services:
                            build_child_xml_node(
                                application_services_node,
                                "reverse-redirect-wx",
                            )
                        if "security_intelligence_policy" in application_services:
                            build_child_xml_node(
                                application_services_node,
                                "security-intelligence-policy",
                                application_services["security_intelligence_policy"],
                            )
                        if "ssl_proxy" in application_services:
                            ssl_node = build_child_xml_node(
                                application_services_node,
                                "ssl-proxy",
                                " ",
                            )
                            if (
                                application_services["ssl_proxy"]
                                and "profile_name" in application_services["ssl_proxy"]
                            ):
                                build_child_xml_node(
                                    ssl_node,
                                    "profile-name",
                                    application_services["ssl_proxy"]["profile_name"],
                                )
                        if "uac_policy" in application_services:
                            uac_node = build_child_xml_node(
                                application_services_node,
                                "uac-policy",
                                " ",
                            )
                            if (
                                application_services["uac_policy"]
                                and "captive_portal" in application_services["uac_policy"]
                            ):
                                build_child_xml_node(
                                    uac_node,
                                    "captive-portal",
                                    application_services["uac_policy"]["captive_portal"],
                                )
                        if "utm_policy" in application_services:
                            build_child_xml_node(
                                application_services_node,
                                "utm-policy",
                                application_services["utm_policy"],
                            )
                    if "destination_address" in permit:
                        permit_destination_address_node = build_child_xml_node(
                            permit_node,
                            "destination-address",
                        )
                        if permit["destination_address"] == "drop-untranslated":
                            build_child_xml_node(
                                permit_destination_address_node,
                                "drop-untranslated",
                            )
                        if permit["destination_address"] == "drop-translated":
                            build_child_xml_node(
                                permit_destination_address_node,
                                "drop-translated",
                            )
                    if "firewall_authentication" in permit:
                        f_a_node = build_child_xml_node(
                            permit_node,
                            "firewall-authentication",
                        )
                        f_a = permit["firewall_authentication"]
                        if "pass_through" in f_a:
                            pass_through_node = build_child_xml_node(
                                f_a_node,
                                "pass-through",
                                " ",
                            )
                            if "access_profile" in f_a["pass_through"]:
                                build_child_xml_node(
                                    pass_through_node,
                                    "access-profile",
                                    f_a["pass_through"]["access_profile"],
                                )
                            if "auth_only_browser" in f_a["pass_through"]:
                                build_child_xml_node(
                                    pass_through_node,
                                    "auth-only-browser",
                                    " ",
                                )
                            if "auth_user_agent" in f_a["pass_through"]:
                                if (
                                    f_a["pass_through"]["auth_user_agent"]
                                    and f_a["pass_through"]["auth_user_agent"] is not True
                                ):
                                    build_child_xml_node(
                                        pass_through_node,
                                        "auth-user-agent",
                                        f_a["pass_through"]["auth_user_agent"],
                                    )
                                else:
                                    build_child_xml_node(
                                        pass_through_node,
                                        "auth-user-agent",
                                        " ",
                                    )

                            if "client_match" in f_a["pass_through"]:
                                build_child_xml_node(
                                    pass_through_node,
                                    "client-match",
                                    f_a["pass_through"]["client_match"],
                                )
                            if "ssl_termination_profile" in f_a["pass_through"]:
                                build_child_xml_node(
                                    pass_through_node,
                                    "ssl-termination-profile",
                                    f_a["pass_through"]["ssl_termination_profile"],
                                )
                            if "web_redirect" in f_a["pass_through"]:
                                build_child_xml_node(
                                    pass_through_node,
                                    "web-redirect",
                                )
                            if "web_redirect_to_https" in f_a["pass_through"]:
                                build_child_xml_node(
                                    pass_through_node,
                                    "web-redirect-to-https",
                                )
                        if "push_to_identity_management" in f_a:
                            build_child_xml_node(
                                f_a_node,
                                "push-to-identity-management",
                            )
                        if "user_firewall" in f_a:
                            user_firewall_node = build_child_xml_node(
                                f_a_node,
                                "user-firewall",
                                " ",
                            )
                            if "access_profile" in f_a["user_firewall"]:
                                build_child_xml_node(
                                    user_firewall_node,
                                    "access-profile",
                                    f_a["user_firewall"]["access_profile"],
                                )
                            if "auth_only_browser" in f_a["user_firewall"]:
                                if (
                                    f_a["pass_through"]["auth_user_agent"]
                                    and f_a["pass_through"]["auth_user_agent"] is not True
                                ):
                                    build_child_xml_node(
                                        pass_through_node,
                                        "auth-user-agent",
                                        f_a["pass_through"]["auth_user_agent"],
                                    )
                                else:
                                    build_child_xml_node(
                                        pass_through_node,
                                        "auth-user-agent",
                                        " ",
                                    )
                            if "domain" in f_a["user_firewall"]:
                                build_child_xml_node(
                                    user_firewall_node,
                                    "domain",
                                    f_a["user_firewall"]["domain"],
                                )
                            if "ssl_termination_profile" in f_a["user_firewall"]:
                                build_child_xml_node(
                                    user_firewall_node,
                                    "ssl-termination-profile",
                                    f_a["user_firewall"]["ssl_termination_profile"],
                                )
                            if "web_redirect" in f_a["user_firewall"]:
                                build_child_xml_node(
                                    user_firewall_node,
                                    "web-redirect",
                                    " ",
                                )
                            if "web_redirect_to_https" in f_a["user_firewall"]:
                                build_child_xml_node(
                                    user_firewall_node,
                                    "web-redirect-to-https",
                                    " ",
                                )

                        if "web_authentication" in f_a:
                            web_authentication_node = build_child_xml_node(
                                f_a_node,
                                "web-authentication",
                                " ",
                            )
                            for client_match in f_a["web_authentication"]:
                                build_child_xml_node(
                                    web_authentication_node,
                                    "client-match",
                                    client_match,
                                )

                    if "tcp_options" in permit:
                        tcp_options_node = build_child_xml_node(
                            permit_node,
                            "tcp-options",
                            " ",
                        )
                        tcp_options = permit["tcp_options"]
                        if "initial_tcp_mss" in tcp_options:
                            build_child_xml_node(
                                tcp_options_node,
                                "initial-tcp-mss",
                                tcp_options["initial_tcp_mss"],
                            )
                        if "reverse_tcp_mss" in tcp_options:
                            build_child_xml_node(
                                tcp_options_node,
                                "reverse-tcp-mss",
                                tcp_options["reverse_tcp_mss"],
                            )
                        if "sequence_check_required" in tcp_options:
                            build_child_xml_node(
                                tcp_options_node,
                                "sequence-check-required",
                            )
                        if "syn_check_required" in tcp_options:
                            build_child_xml_node(
                                tcp_options_node,
                                "syn-check-required",
                            )
                        if "window_scale" in tcp_options:
                            build_child_xml_node(
                                tcp_options_node,
                                "window-scale",
                            )

                    if "tunnel" in permit:
                        tunnel_node = build_child_xml_node(
                            permit_node,
                            "tunnel",
                            " ",
                        )
                        if "ipsec_vpn" in permit["tunnel"]:
                            build_child_xml_node(tunnel_node, "ipsec-vpn")
                        if "pair_policy" in permit["tunnel"]:
                            build_child_xml_node(tunnel_node, "pair-policy")

        # add zone-pair policies
        if "from_zones" in want.keys():
            from_zones = want.get("from_zones")
            for from_zone in from_zones:
                for to_zone in from_zone["to_zones"]:
                    policy_node = build_child_xml_node(
                        security_policies_node,
                        "policy",
                    )
                    build_child_xml_node(
                        policy_node,
                        "from-zone-name",
                        from_zone["name"],
                    )
                    build_child_xml_node(
                        policy_node,
                        "to-zone-name",
                        to_zone["name"],
                    )
                    build_policies(policy_node, to_zone["policies"])

        # add global policies
        if "global" in want.keys():
            global_node = build_child_xml_node(
                security_policies_node,
                "global",
            )
            global_policies = want.get("global").get("policies")
            build_policies(global_node, global_policies)

        if security_policies_node is not None:
            security_policies_xml.append(security_policies_node)
        return security_policies_xml

    def _state_deleted(self, _want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        security_policies_xml = []
        security_policies_root = None
        delete = {"delete": "delete"}
        if have is not None:
            security_policies_root = build_child_xml_node(
                self.root,
                "policies",
                None,
                delete,
            )

        if security_policies_root is not None:
            security_policies_xml.append(security_policies_root)
        return security_policies_xml
