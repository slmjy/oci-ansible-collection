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
module: oci_integration_instance
short_description: Manage an IntegrationInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an IntegrationInstance resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Integration Instance.
    - "This resource has the following action operations in the M(oracle.oci.oci_integration_instance_actions) module: change_compartment,
      change_integration_instance_network_endpoint, start, stop."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - Integration Instance Identifier.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - Compartment Identifier.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    integration_instance_type:
        description:
            - Standard or Enterprise type
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "STANDARD"
            - "ENTERPRISE"
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name,
              type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to
              namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    is_byol:
        description:
            - Bring your own license.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    idcs_at:
        description:
            - IDCS Authentication token. This is required for all realms with IDCS. Its optional as its not required for non IDCS realms.
        type: str
    message_packs:
        description:
            - The number of configured message packs
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    is_visual_builder_enabled:
        description:
            - Visual Builder is enabled or not.
            - This parameter is updatable.
        type: bool
    custom_endpoint:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            hostname:
                description:
                    - A custom hostname to be used for the integration instance URL, in FQDN format.
                    - This parameter is updatable.
                type: str
                required: true
            certificate_secret_id:
                description:
                    - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                      All certificates should be stored in a single base64 encoded secret
                      Note the update will fail if this is not a valid certificate.
                    - This parameter is updatable.
                type: str
    alternate_custom_endpoints:
        description:
            - A list of alternate custom endpoints to be used for the integration instance URL
              (contact Oracle for alternateCustomEndpoints availability for a specific instance).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            hostname:
                description:
                    - A custom hostname to be used for the integration instance URL, in FQDN format.
                    - This parameter is updatable.
                type: str
                required: true
            certificate_secret_id:
                description:
                    - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                      All certificates should be stored in a single base64 encoded secret
                      Note the update will fail if this is not a valid certificate.
                    - This parameter is updatable.
                type: str
    consumption_model:
        description:
            - Optional parameter specifying which entitlement to use for billing purposes. Only required if the account possesses more than one entitlement.
        type: str
        choices:
            - "UCM"
            - "GOV"
            - "OIC4SAAS"
    is_file_server_enabled:
        description:
            - The file server is enabled or not.
            - This parameter is updatable.
        type: bool
    network_endpoint_details:
        description:
            - ""
        type: dict
        suboptions:
            network_endpoint_type:
                description:
                    - The type of network endpoint.
                type: str
                choices:
                    - "PUBLIC"
                required: true
            allowlisted_http_ips:
                description:
                    - Source IP addresses or IP address ranges ingress rules.
                type: list
                elements: str
            allowlisted_http_vcns:
                description:
                    - Virtual Cloud Networks allowed to access this network endpoint.
                type: list
                elements: dict
                suboptions:
                    id:
                        description:
                            - The Virtual Cloud Network OCID.
                        type: str
                        required: true
                    allowlisted_ips:
                        description:
                            - Source IP addresses or IP address ranges ingress rules.
                        type: list
                        elements: str
            is_integration_vcn_allowlisted:
                description:
                    - The Integration service's VCN is allow-listed to allow integrations to call back into other integrations
                type: bool
    integration_instance_id:
        description:
            - Unique Integration Instance identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the IntegrationInstance.
            - Use I(state=present) to create or update an IntegrationInstance.
            - Use I(state=absent) to delete an IntegrationInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create integration_instance
  oci_integration_instance:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    integration_instance_type: STANDARD
    is_byol: true
    message_packs: 56

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    idcs_at: idcs_at_example
    is_visual_builder_enabled: true
    custom_endpoint:
      # required
      hostname: hostname_example

      # optional
      certificate_secret_id: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
    alternate_custom_endpoints:
    - # required
      hostname: hostname_example

      # optional
      certificate_secret_id: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
    consumption_model: UCM
    is_file_server_enabled: true
    network_endpoint_details:
      # required
      network_endpoint_type: PUBLIC

      # optional
      allowlisted_http_ips: [ "allowlisted_http_ips_example" ]
      allowlisted_http_vcns:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        allowlisted_ips: [ "allowlisted_ips_example" ]
      is_integration_vcn_allowlisted: true

- name: Update integration_instance
  oci_integration_instance:
    # required
    integration_instance_id: "ocid1.integrationinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    integration_instance_type: STANDARD
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_byol: true
    message_packs: 56
    is_visual_builder_enabled: true
    custom_endpoint:
      # required
      hostname: hostname_example

      # optional
      certificate_secret_id: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
    alternate_custom_endpoints:
    - # required
      hostname: hostname_example

      # optional
      certificate_secret_id: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
    is_file_server_enabled: true

- name: Update integration_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_integration_instance:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    integration_instance_type: STANDARD
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_byol: true
    message_packs: 56
    is_visual_builder_enabled: true
    custom_endpoint:
      # required
      hostname: hostname_example

      # optional
      certificate_secret_id: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
    alternate_custom_endpoints:
    - # required
      hostname: hostname_example

      # optional
      certificate_secret_id: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
    is_file_server_enabled: true

- name: Delete integration_instance
  oci_integration_instance:
    # required
    integration_instance_id: "ocid1.integrationinstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete integration_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_integration_instance:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
integration_instance:
    description:
        - Details of the IntegrationInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Integration Instance Identifier, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        integration_instance_type:
            description:
                - Standard or Enterprise type
            returned: on success
            type: str
            sample: STANDARD
        time_created:
            description:
                - The time the the IntegrationInstance was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the IntegrationInstance was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the integration instance.
            returned: on success
            type: str
            sample: CREATING
        state_message:
            description:
                - An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: state_message_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name,
                  type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to
                  namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        is_byol:
            description:
                - Bring your own license.
            returned: on success
            type: bool
            sample: true
        instance_url:
            description:
                - The Integration Instance URL.
            returned: on success
            type: str
            sample: instance_url_example
        message_packs:
            description:
                - The number of configured message packs (if any)
            returned: on success
            type: int
            sample: 56
        is_file_server_enabled:
            description:
                - The file server is enabled or not.
            returned: on success
            type: bool
            sample: true
        is_visual_builder_enabled:
            description:
                - VisualBuilder is enabled or not.
            returned: on success
            type: bool
            sample: true
        custom_endpoint:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - A custom hostname to be used for the integration instance URL, in FQDN format.
                    returned: on success
                    type: str
                    sample: hostname_example
                certificate_secret_id:
                    description:
                        - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                    returned: on success
                    type: str
                    sample: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
                certificate_secret_version:
                    description:
                        - The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
                    returned: on success
                    type: int
                    sample: 56
        alternate_custom_endpoints:
            description:
                - A list of alternate custom endpoints used for the integration instance URL.
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - A custom hostname to be used for the integration instance URL, in FQDN format.
                    returned: on success
                    type: str
                    sample: hostname_example
                certificate_secret_id:
                    description:
                        - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                    returned: on success
                    type: str
                    sample: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
                certificate_secret_version:
                    description:
                        - The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
                    returned: on success
                    type: int
                    sample: 56
        consumption_model:
            description:
                - The entitlement used for billing purposes.
            returned: on success
            type: str
            sample: UCM
        network_endpoint_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                network_endpoint_type:
                    description:
                        - The type of network endpoint.
                    returned: on success
                    type: str
                    sample: PUBLIC
                allowlisted_http_ips:
                    description:
                        - Source IP addresses or IP address ranges ingress rules.
                    returned: on success
                    type: list
                    sample: []
                allowlisted_http_vcns:
                    description:
                        - Virtual Cloud Networks allowed to access this network endpoint.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The Virtual Cloud Network OCID.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        allowlisted_ips:
                            description:
                                - Source IP addresses or IP address ranges ingress rules.
                            returned: on success
                            type: list
                            sample: []
                is_integration_vcn_allowlisted:
                    description:
                        - The Integration service's VCN is allow-listed to allow integrations to call back into other integrations
                    returned: on success
                    type: bool
                    sample: true
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "integration_instance_type": "STANDARD",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_byol": true,
        "instance_url": "instance_url_example",
        "message_packs": 56,
        "is_file_server_enabled": true,
        "is_visual_builder_enabled": true,
        "custom_endpoint": {
            "hostname": "hostname_example",
            "certificate_secret_id": "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_secret_version": 56
        },
        "alternate_custom_endpoints": [{
            "hostname": "hostname_example",
            "certificate_secret_id": "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_secret_version": 56
        }],
        "consumption_model": "UCM",
        "network_endpoint_details": {
            "network_endpoint_type": "PUBLIC",
            "allowlisted_http_ips": [],
            "allowlisted_http_vcns": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "allowlisted_ips": []
            }],
            "is_integration_vcn_allowlisted": true
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.integration import IntegrationInstanceClient
    from oci.integration.models import CreateIntegrationInstanceDetails
    from oci.integration.models import UpdateIntegrationInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IntegrationInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "integration_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("integration_instance_id")

    def get_get_fn(self):
        return self.client.get_integration_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_integration_instance,
            integration_instance_id=self.module.params.get("integration_instance_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_integration_instances, **kwargs
        )

    def get_create_model_class(self):
        return CreateIntegrationInstanceDetails

    def get_exclude_attributes(self):
        return ["idcs_at"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_integration_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(create_integration_instance_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateIntegrationInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_integration_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                integration_instance_id=self.module.params.get(
                    "integration_instance_id"
                ),
                update_integration_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_integration_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                integration_instance_id=self.module.params.get(
                    "integration_instance_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


IntegrationInstanceHelperCustom = get_custom_class("IntegrationInstanceHelperCustom")


class ResourceHelper(IntegrationInstanceHelperCustom, IntegrationInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            integration_instance_type=dict(
                type="str", choices=["STANDARD", "ENTERPRISE"]
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            is_byol=dict(type="bool"),
            idcs_at=dict(type="str"),
            message_packs=dict(type="int"),
            is_visual_builder_enabled=dict(type="bool"),
            custom_endpoint=dict(
                type="dict",
                options=dict(
                    hostname=dict(type="str", required=True),
                    certificate_secret_id=dict(type="str"),
                ),
            ),
            alternate_custom_endpoints=dict(
                type="list",
                elements="dict",
                options=dict(
                    hostname=dict(type="str", required=True),
                    certificate_secret_id=dict(type="str"),
                ),
            ),
            consumption_model=dict(type="str", choices=["UCM", "GOV", "OIC4SAAS"]),
            is_file_server_enabled=dict(type="bool"),
            network_endpoint_details=dict(
                type="dict",
                options=dict(
                    network_endpoint_type=dict(
                        type="str", required=True, choices=["PUBLIC"]
                    ),
                    allowlisted_http_ips=dict(type="list", elements="str"),
                    allowlisted_http_vcns=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            id=dict(type="str", required=True),
                            allowlisted_ips=dict(type="list", elements="str"),
                        ),
                    ),
                    is_integration_vcn_allowlisted=dict(type="bool"),
                ),
            ),
            integration_instance_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="integration_instance",
        service_client_class=IntegrationInstanceClient,
        namespace="integration",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
