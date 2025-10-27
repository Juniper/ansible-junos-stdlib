#
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The junos security_policies fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from copy import deepcopy

from ansible.module_utils._text import to_bytes
from ansible.module_utils.basic import missing_required_lib
from ansible.module_utils.six import string_types
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.juniper.device.plugins.module_utils.network.junos.argspec.security_policies.security_policies import (
    Security_policiesArgs,
)


try:
    from lxml import etree

    HAS_LXML = True
except ImportError:
    HAS_LXML = False

try:
    import xmltodict

    HAS_XMLTODICT = True
except ImportError:
    HAS_XMLTODICT = False


class Security_policiesFacts(object):
    """The junos security_policies fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Security_policiesArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def _get_xml_dict(self, xml_root):
        if not HAS_XMLTODICT:
            self._module.fail_json(msg=missing_required_lib("xmltodict"))
        xml_dict = xmltodict.parse(
            etree.tostring(xml_root),
            dict_constructor=dict,
        )
        return xml_dict

    def _get_device_data(self, connection, config_filters):
        """
        :param connection:
        :param config_filter:
        :return:
        """
        return connection.get_configuration(filter=config_filters)

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for security_polices
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not HAS_LXML:
            self._module.fail_json(msg="lxml is not installed.")

        if not data:
            config_filter = """
                    <configuration>
                        <security>
                            <policies>
                            </policies>
                        </security>
                    </configuration>
                    """
            data = self._get_device_data(connection, config_filter)

        # split the config into instances of the resource
        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace"),
            )
        objs = {}
        resources = data.xpath("configuration/security/policies")
        for resource in resources:
            if resource is not None:
                xml = self._get_xml_dict(resource)
                objs = self.render_config(self.generated_spec, xml)

        facts = {"security_policies": {}}
        if objs:
            params = utils.validate_config(
                self.argument_spec,
                {"config": objs},
            )

            facts["security_policies"] = utils.remove_empties(params["config"])

        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        security_policies_config = {}

        # Parse facts for security policies
        conf = conf.get("policies") or {}

        if "policy" in conf:
            security_policies_config["from_zones"] = []
            from_zone_dict = {}
            zone_pairs = conf.get("policy")
            if isinstance(zone_pairs, dict):
                temp = zone_pairs
                zone_pairs = []
                zone_pairs.append(temp)
            for zone_pair_policies in zone_pairs:
                if zone_pair_policies["from-zone-name"] not in from_zone_dict:
                    from_zone_dict[zone_pair_policies["from-zone-name"]] = {}
                    from_zone_dict[zone_pair_policies["from-zone-name"]]["name"] = (
                        zone_pair_policies["from-zone-name"]
                    )
                    from_zone_dict[zone_pair_policies["from-zone-name"]]["to_zones"] = {}

                from_zone = from_zone_dict[zone_pair_policies["from-zone-name"]]

                from_zone["to_zones"][zone_pair_policies["to-zone-name"]] = {}
                to_zone = from_zone["to_zones"][zone_pair_policies["to-zone-name"]]

                to_zone["name"] = zone_pair_policies["to-zone-name"]
                to_zone["policies"] = self.parse_policies(
                    zone_pair_policies["policy"],
                )

            for from_zone in from_zone_dict.values():
                from_zone["to_zones"] = list(from_zone["to_zones"].values())
                security_policies_config["from_zones"].append(from_zone)

        if "global" in conf:
            global_policies = conf.get("global")
            global_policies = global_policies.get("policy")
            security_policies_config["global"] = {}
            security_policies_config["global"]["policies"] = self.parse_policies(global_policies)

        return security_policies_config

    def parse_policies(self, policies):
        policy_list = []

        if isinstance(policies, dict):
            temp = policies
            policies = []
            policies.append(temp)

        for policy in policies:
            tmp_policy = {}

            # parse name of policy
            tmp_policy["name"] = policy["name"]

            # parse match criteria of security policy
            tmp_policy["match"] = {}

            match = tmp_policy["match"]
            policy_match = policy["match"]

            match["source_address"] = {}
            if isinstance(policy_match["source-address"], string_types):
                policy_match["source-address"] = [
                    policy_match["source-address"],
                ]
            for source_address in policy_match["source-address"]:
                if source_address == "any-ipv6":
                    match["source_address"]["any_ipv6"] = True
                elif source_address == "any-ipv4":
                    match["source_address"]["any_ipv4"] = True
                elif source_address == "any":
                    match["source_address"]["any"] = True
                else:
                    if "addresses" not in match["source_address"]:
                        match["source_address"]["addresses"] = []
                    match["source_address"]["addresses"].append(source_address)

            if "source-address-excluded" in policy_match:
                match["source_address_excluded"] = True

            match["destination_address"] = {}
            if isinstance(policy_match["destination-address"], string_types):
                policy_match["destination-address"] = [
                    policy_match["destination-address"],
                ]
            for destination_address in policy_match["destination-address"]:
                if destination_address == "any-ipv6":
                    match["destination_address"]["any_ipv6"] = True
                elif destination_address == "any-ipv4":
                    match["destination_address"]["any_ipv4"] = True
                elif destination_address == "any":
                    match["destination_address"]["any"] = True
                else:
                    if "addresses" not in match["destination_address"]:
                        match["destination_address"]["addresses"] = []
                    match["destination_address"]["addresses"].append(
                        destination_address,
                    )

            if "destination-address-excluded" in policy_match:
                match["destination_address_excluded"] = True

            match["application"] = {}
            if policy_match["application"] == "any":
                match["application"]["any"] = True
            else:
                if isinstance(policy_match["application"], string_types):
                    policy_match["application"] = [policy_match["application"]]
                match["application"]["names"] = policy_match["application"]

            if "source-end-user-profile" in policy_match:
                match["source_end_user_profile"] = policy_match["source-end-user-profile"][
                    "source-end-user-profile-name"
                ]

            if "source-identity" in policy_match:
                if isinstance(policy_match["source-identity"], string_types):
                    policy_match["source-identity"] = [
                        policy_match["source-identity"],
                    ]
                match["source_identity"] = {}
                for source_identity in policy_match["source-identity"]:
                    if source_identity == "any":
                        match["source_identity"]["any"] = True
                    elif "authenticated-user" == source_identity:
                        match["source_identity"]["authenticated_user"] = True
                    elif "unauthenticated-user" == source_identity:
                        match["source_identity"]["unauthenticated_user"] = True
                    elif "unknown-user" == source_identity:
                        match["source_identity"]["unknown_user"] = True
                    else:
                        if "names" not in match["source_identity"]:
                            match["source_identity"]["names"] = []
                        match["source_identity"]["names"].append(
                            source_identity,
                        )

            if "url-category" in policy_match:
                if isinstance(policy_match["url-category"], string_types):
                    policy_match["url-category"] = [
                        policy_match["url-category"],
                    ]
                match["url_category"] = {}
                for url_category in policy_match["url-category"]:
                    if url_category == "any":
                        match["url_category"]["any"] = True
                    elif url_category == "none":
                        match["url_category"]["none"] = True
                    else:
                        if "names" not in match["url_category"]:
                            match["url_category"]["names"] = []
                        match["url_category"]["names"].append(url_category)

            if "dynamic-application" in policy_match:
                if isinstance(
                    policy_match["dynamic-application"],
                    string_types,
                ):
                    policy_match["dynamic-application"] = [
                        policy_match["dynamic-application"],
                    ]
                match["dynamic_application"] = {}
                for dynamic_application in policy_match["dynamic-application"]:
                    if dynamic_application == "any":
                        match["dynamic_application"]["any"] = True
                    elif dynamic_application == "none":
                        match["dynamic_application"]["none"] = True
                    else:
                        if "names" not in match["dynamic_application"]:
                            match["dynamic_application"]["names"] = []
                        match["dynamic_application"]["names"].append(
                            dynamic_application,
                        )
            # end of match criteria parsing

            # parse match action of security policy
            tmp_policy["then"] = {}
            action = tmp_policy["then"]
            policy_action = policy["then"]

            if "count" in policy_action:
                action["count"] = True

            if "log" in policy_action:
                action["log"] = {}
                if "session-close" in policy_action["log"]:
                    action["log"]["session_close"] = True
                if "session-init" in policy_action["log"]:
                    action["log"]["session_init"] = True

            if "deny" in policy_action:
                action["deny"] = True

            if "reject" in policy_action:
                action["reject"] = {}
                reject = action["reject"]
                policy_reject = policy_action["reject"] or {}
                reject["enable"] = True

                if "profile" in policy_reject:
                    reject["profile"] = policy_reject["profile"]
                if "ssl-proxy" in policy_reject:
                    policy_reject["ssl-proxy"] = policy_reject["ssl-proxy"] or {}
                    reject["ssl_proxy"] = {}
                    reject["ssl_proxy"]["enable"] = True
                    if "profile-name" in policy_reject["ssl-proxy"]:
                        reject["ssl_proxy"]["profile_name"] = policy_reject["ssl-proxy"][
                            "profile-name"
                        ]

            if "permit" in policy_action:
                action["permit"] = {}
                permit = action["permit"]
                policy_permit = policy_action["permit"] or {}

                if "application-services" in policy_permit:
                    permit["application_services"] = {}
                    application_services = permit["application_services"]
                    policy_application_services = policy_permit["application-services"] or {}

                    if "advanced-anti-malware-policy" in policy_application_services:
                        application_services["advanced_anti_malware_policy"] = (
                            policy_application_services["advanced-anti-malware-policy"]
                        )
                    if "application-traffic-control" in policy_application_services:
                        application_services["application_traffic_control_rule_set"] = (
                            policy_application_services["application-traffic-control"]["rule-set"]
                        )
                    if "gprs-gtp-profile" in policy_application_services:
                        application_services["gprs_gtp_profile"] = policy_application_services[
                            "gprs-gtp-profile"
                        ]
                    if "gprs-sctp-profile" in policy_application_services:
                        application_services["gprs_sctp_profile"] = policy_application_services[
                            "gprs-sctp-profile"
                        ]
                    if "icap-redirect" in policy_application_services:
                        application_services["icap_redirect"] = policy_application_services[
                            "icap-redirect"
                        ]
                    if "idp" in policy_application_services:
                        application_services["idp"] = True
                    if "idp-policy" in policy_application_services:
                        application_services["idp_policy"] = policy_application_services[
                            "idp-policy"
                        ]
                    if "redirect-wx" in policy_application_services:
                        application_services["redirect_wx"] = True
                    if "reverse-redirect-wx" in policy_application_services:
                        application_services["reverse_redirect_wx"] = True
                    if "security-intelligence-policy" in policy_application_services:
                        application_services["security_intelligence_policy"] = (
                            policy_application_services["security-intelligence-policy"]
                        )
                    if "ssl-proxy" in policy_application_services:
                        application_services["ssl_proxy"] = {}
                        application_services["ssl_proxy"]["enable"] = True
                        if (
                            policy_application_services["ssl-proxy"]
                            and "profile-name" in policy_application_services["ssl-proxy"]
                        ):
                            application_services["ssl_proxy"]["profile_name"] = (
                                policy_application_services["ssl-proxy"]["profile-name"]
                            )
                    if "uac-policy" in policy_application_services:
                        application_services["uac_policy"] = {}
                        application_services["uac_policy"]["enable"] = True
                        if (
                            policy_application_services["uac-policy"]
                            and "captive-portal" in policy_application_services["uac-policy"]
                        ):
                            application_services["uac_policy"]["captive_portal"] = (
                                policy_application_services["uac-policy"]["captive-portal"]
                            )
                    if "utm-policy" in policy_application_services:
                        application_services["utm_policy"] = policy_application_services[
                            "utm-policy"
                        ]

                if "destination-address" in policy_permit:
                    permit["destination_address"] = policy_permit["destination-address"]

                if "firewall-authentication" in policy_permit:
                    permit["firewall_authentication"] = {}
                    f_a = permit["firewall_authentication"]
                    policy_f_a = policy_permit["firewall-authentication"] or {}

                    if "pass-through" in policy_f_a:
                        f_a["pass_through"] = {}
                        if "access-profile" in policy_f_a["pass-through"]:
                            f_a["pass_through"]["access_profile"] = policy_f_a["pass-through"][
                                "access-profile"
                            ]
                        if "auth-only-browser" in policy_f_a["pass-through"]:
                            f_a["pass_through"]["auth_only_browser"] = True
                        if "auth-user-agent" in policy_f_a["pass-through"]:
                            f_a["pass_through"]["auth_user_agent"] = policy_f_a["pass-through"][
                                "auth-user-agent"
                            ]
                        if "client-match" in policy_f_a["pass-through"]:
                            f_a["pass_through"]["client_match"] = policy_f_a["pass-through"][
                                "client-match"
                            ]
                        if "ssl-termination-profile" in policy_f_a["pass-through"]:
                            f_a["pass_through"]["ssl_termination_profile"] = policy_f_a[
                                "pass-through"
                            ]["ssl-termination-profile"]
                        if "web-redirect" in policy_f_a["pass-through"]:
                            f_a["pass_through"]["web_redirect"] = True
                        if "web-redirect-to-https" in policy_f_a["pass-through"]:
                            f_a["pass_through"]["web_redirect_to_https"] = True

                    if "push-to-identity-management" in policy_f_a:
                        f_a["push_to_identity_management"] = True

                    if "user-firewall" in policy_f_a:
                        f_a["user_firewall"] = {}
                        if "access-profile" in policy_f_a["user-firewall"]:
                            f_a["user_firewall"]["access_profile"] = policy_f_a["user-firewall"][
                                "access-profile"
                            ]
                        if "auth-only-browser" in policy_f_a["user-firewall"]:
                            f_a["user_firewall"]["auth_only_browser"] = True
                        if "auth-user-agent" in policy_f_a["user-firewall"]:
                            f_a["user_firewall"]["auth_user_agent"] = policy_f_a["user-firewall"][
                                "auth-user-agent"
                            ]
                        if "domain" in policy_f_a["user-firewall"]:
                            f_a["user_firewall"]["domain"] = policy_f_a["user-firewall"]["domain"]
                        if "ssl-termination-profile" in policy_f_a["user-firewall"]:
                            f_a["user_firewall"]["ssl_termination_profile"] = policy_f_a[
                                "user-firewall"
                            ]["ssl-termination-profile"]
                        if "web-redirect" in policy_f_a["user-firewall"]:
                            f_a["user_firewall"]["web_redirect"] = True
                        if "web-redirect-to-https" in policy_f_a["user-firewall"]:
                            f_a["user_firewall"]["web_redirect_to_https"] = True

                    if "web-authentication" in policy_f_a:
                        f_a["web_authentication"] = []
                        if isinstance(
                            policy_f_a["web-authentication"]["client-match"],
                            str,
                        ):
                            temp = policy_f_a["web-authentication"]["client-match"]
                            policy_f_a["web-authentication"]["client-match"] = []
                            policy_f_a["web-authentication"]["client-match"].append(temp)
                        f_a["web_authentication"] = policy_f_a["web-authentication"]["client-match"]

                if "tcp-options" in policy_permit:
                    permit["tcp_options"] = {}
                    tcp_options = permit["tcp_options"]
                    policy_tcp_options = policy_permit["tcp-options"] or {}

                    if "initial-tcp-mss" in policy_tcp_options:
                        tcp_options["initial_tcp_mss"] = policy_permit["tcp-options"][
                            "initial-tcp-mss"
                        ]
                    if "reverse-tcp-mss" in policy_tcp_options:
                        tcp_options["reverse_tcp_mss"] = policy_permit["tcp-options"][
                            "reverse-tcp-mss"
                        ]
                    if "sequence-check-required" in policy_tcp_options:
                        tcp_options["sequence_check_required"] = True
                    if "syn-check-required" in policy_tcp_options:
                        tcp_options["syn_check_required"] = True
                    if "window-scale" in policy_tcp_options:
                        tcp_options["window_scale"] = True

                if "tunnel" in policy_permit:
                    permit["tunnel"] = {}
                    policy_permit["tunnel"] = policy_permit["tunnel"] or {}
                    if "ipsec-vpn" in policy_permit["tunnel"]:
                        permit["tunnel"]["ipsec_vpn"] = policy_permit["tunnel"]["ipsec-vpn"]
                    if "pair-policy" in policy_permit["tunnel"]:
                        permit["tunnel"]["pair_policy"] = policy_permit["tunnel"]["pair-policy"]

            # end of match action parsing

            # parse description of security policy
            if "description" in policy:
                tmp_policy["description"] = policy["description"]

            # parse scheduler name of security policy
            if "scheduler-name" in policy:
                tmp_policy["scheduler_name"] = policy["scheduler-name"]

            test = utils.remove_empties(tmp_policy)
            policy_list.append(test)

        return policy_list
