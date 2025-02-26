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
module: oci_network_cross_connect_group_actions
short_description: Perform actions on a CrossConnectGroup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a CrossConnectGroup resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a cross-connect group into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    cross_connect_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cross-connect group.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
              cross-connect group to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the CrossConnectGroup.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on cross_connect_group
  oci_network_cross_connect_group_actions:
    # required
    cross_connect_group_id: "ocid1.crossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
cross_connect_group:
    description:
        - Details of the CrossConnectGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the cross-connect group.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The cross-connect group's Oracle ID (OCID).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The cross-connect group's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        customer_reference_name:
            description:
                - A reference name or identifier for the physical fiber connection that this cross-connect
                  group uses.
            returned: on success
            type: str
            sample: customer_reference_name_example
        time_created:
            description:
                - The date and time the cross-connect group was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        macsec_properties:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                state:
                    description:
                        - Indicates whether or not MACsec is enabled.
                    returned: on success
                    type: str
                    sample: ENABLED
                primary_key:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        connectivity_association_name_secret_id:
                            description:
                                - Secret L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity
                                  association Key Name (CKN) of this MACsec key.
                            returned: on success
                            type: str
                            sample: "ocid1.connectivityassociationnamesecret.oc1..xxxxxxEXAMPLExxxxxx"
                        connectivity_association_name_secret_version:
                            description:
                                - The secret version of the connectivity association name secret in Vault.
                            returned: on success
                            type: int
                            sample: 56
                        connectivity_association_key_secret_id:
                            description:
                                - Secret L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity
                                  Association Key (CAK) of this MACsec key.
                            returned: on success
                            type: str
                            sample: "ocid1.connectivityassociationkeysecret.oc1..xxxxxxEXAMPLExxxxxx"
                        connectivity_association_key_secret_version:
                            description:
                                - The secret version of the `connectivityAssociationKey` secret in Vault.
                            returned: on success
                            type: int
                            sample: 56
                encryption_cipher:
                    description:
                        - Type of encryption cipher suite to use for the MACsec connection.
                    returned: on success
                    type: str
                    sample: AES128_GCM
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "customer_reference_name": "customer_reference_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "macsec_properties": {
            "state": "ENABLED",
            "primary_key": {
                "connectivity_association_name_secret_id": "ocid1.connectivityassociationnamesecret.oc1..xxxxxxEXAMPLExxxxxx",
                "connectivity_association_name_secret_version": 56,
                "connectivity_association_key_secret_id": "ocid1.connectivityassociationkeysecret.oc1..xxxxxxEXAMPLExxxxxx",
                "connectivity_association_key_secret_version": 56
            },
            "encryption_cipher": "AES128_GCM"
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import ChangeCrossConnectGroupCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CrossConnectGroupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "cross_connect_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("cross_connect_group_id")

    def get_get_fn(self):
        return self.client.get_cross_connect_group

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cross_connect_group,
            cross_connect_group_id=self.module.params.get("cross_connect_group_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCrossConnectGroupCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_cross_connect_group_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cross_connect_group_id=self.module.params.get("cross_connect_group_id"),
                change_cross_connect_group_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


CrossConnectGroupActionsHelperCustom = get_custom_class(
    "CrossConnectGroupActionsHelperCustom"
)


class ResourceHelper(
    CrossConnectGroupActionsHelperCustom, CrossConnectGroupActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            cross_connect_group_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="cross_connect_group",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
