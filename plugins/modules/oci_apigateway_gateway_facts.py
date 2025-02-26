#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_apigateway_gateway_facts
short_description: Fetches details about one or multiple Gateway resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Gateway resources in Oracle Cloud Infrastructure
    - Returns a list of gateways.
    - If I(gateway_id) is specified, the details of a single Gateway will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    gateway_id:
        description:
            - The ocid of the gateway.
            - Required to get a specific gateway.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ocid of the compartment in which to list resources.
            - Required to list multiple gateways.
        type: str
    certificate_id:
        description:
            - Filter gateways by the certificate ocid.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state.
            - "Example: `SUCCEEDED`"
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'. The default order depends on the sortBy value.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`).
              Default order for `timeCreated` is descending. Default order for
              `displayName` is ascending. The `displayName` sort order is case
              sensitive.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific gateway
  oci_apigateway_gateway_facts:
    # required
    gateway_id: "ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx"

- name: List gateways
  oci_apigateway_gateway_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
gateways:
    description:
        - List of Gateway resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
                - "Example: `My new resource`"
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
                  resource is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint_type:
            description:
                - Gateway endpoint type. `PUBLIC` will have a public ip address assigned to it, while `PRIVATE` will only be
                  accessible on a private IP address on the subnet.
                - "Example: `PUBLIC` or `PRIVATE`"
            returned: on success
            type: str
            sample: PUBLIC
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet in which
                  related resources are created.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        network_security_group_ids:
            description:
                - An array of Network Security Groups OCIDs associated with this API Gateway.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The time this resource was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time this resource was last updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the gateway.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a
                  resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        hostname:
            description:
                - The hostname for APIs deployed on the gateway.
            returned: on success
            type: str
            sample: hostname_example
        certificate_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: str
            sample: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
        ip_addresses:
            description:
                - An array of IP addresses associated with the gateway.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                ip_address:
                    description:
                        - An IP address.
                    returned: on success
                    type: str
                    sample: ip_address_example
        response_cache_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Type of the Response Cache.
                    returned: on success
                    type: str
                    sample: EXTERNAL_RESP_CACHE
                servers:
                    description:
                        - The set of cache store members to connect to. At present only a single server is supported.
                    returned: on success
                    type: complex
                    contains:
                        host:
                            description:
                                - Hostname or IP address (IPv4 only) where the cache store is running.
                            returned: on success
                            type: str
                            sample: host_example
                        port:
                            description:
                                - The port the cache store is exposed on.
                            returned: on success
                            type: int
                            sample: 56
                authentication_secret_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Vault Service secret resource.
                    returned: on success
                    type: str
                    sample: "ocid1.authenticationsecret.oc1..xxxxxxEXAMPLExxxxxx"
                authentication_secret_version_number:
                    description:
                        - The version number of the authentication secret to use.
                    returned: on success
                    type: int
                    sample: 56
                is_ssl_enabled:
                    description:
                        - Defines if the connection should be over SSL.
                    returned: on success
                    type: bool
                    sample: true
                is_ssl_verify_disabled:
                    description:
                        - Defines whether or not to uphold SSL verification.
                    returned: on success
                    type: bool
                    sample: true
                connect_timeout_in_ms:
                    description:
                        - Defines the timeout for establishing a connection with the Response Cache.
                    returned: on success
                    type: int
                    sample: 56
                read_timeout_in_ms:
                    description:
                        - Defines the timeout for reading data from the Response Cache.
                    returned: on success
                    type: int
                    sample: 56
                send_timeout_in_ms:
                    description:
                        - Defines the timeout for transmitting data to the Response Cache.
                    returned: on success
                    type: int
                    sample: 56
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair
                  with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "endpoint_type": "PUBLIC",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "network_security_group_ids": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "hostname": "hostname_example",
        "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_addresses": [{
            "ip_address": "ip_address_example"
        }],
        "response_cache_details": {
            "type": "EXTERNAL_RESP_CACHE",
            "servers": [{
                "host": "host_example",
                "port": 56
            }],
            "authentication_secret_id": "ocid1.authenticationsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "authentication_secret_version_number": 56,
            "is_ssl_enabled": true,
            "is_ssl_verify_disabled": true,
            "connect_timeout_in_ms": 56,
            "read_timeout_in_ms": 56,
            "send_timeout_in_ms": 56
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.apigateway import GatewayClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayGatewayFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "gateway_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_gateway, gateway_id=self.module.params.get("gateway_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "certificate_id",
            "display_name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_gateways,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ApigatewayGatewayFactsHelperCustom = get_custom_class(
    "ApigatewayGatewayFactsHelperCustom"
)


class ResourceFactsHelper(
    ApigatewayGatewayFactsHelperCustom, ApigatewayGatewayFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            gateway_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            certificate_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="gateway",
        service_client_class=GatewayClient,
        namespace="apigateway",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(gateways=result)


if __name__ == "__main__":
    main()
