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
module: oci_blockstorage_boot_volume_actions
short_description: Perform actions on a BootVolume resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BootVolume resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a boot volume into a different compartment within the same tenancy.
      For information about moving resources between compartments,
      see L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    boot_volume_id:
        description:
            - The OCID of the boot volume.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the boot volume to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the BootVolume.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on boot_volume
  oci_blockstorage_boot_volume_actions:
    # required
    boot_volume_id: "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
boot_volume:
    description:
        - Details of the BootVolume resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain of the boot volume.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment that contains the boot volume.
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
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {}
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
                - The boot volume's Oracle ID (OCID).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        image_id:
            description:
                - The image OCID used to create the boot volume.
            returned: on success
            type: str
            sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        is_hydrated:
            description:
                - Specifies whether the boot volume's data has finished copying
                  from the source boot volume or boot volume backup.
            returned: on success
            type: bool
            sample: true
        vpus_per_gb:
            description:
                - The number of volume performance units (VPUs) that will be applied to this boot volume per GB,
                  representing the Block Volume service's elastic performance options.
                  See L(Block Volume Elastic Performance,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeelasticperformance.htm) for more
                  information.
                - "Allowed values:"
                - " * `10`: Represents Balanced option."
                - " * `20`: Represents Higher Performance option."
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of a boot volume.
            returned: on success
            type: str
            sample: PROVISIONING
        size_in_gbs:
            description:
                - The size of the boot volume in GBs.
            returned: on success
            type: int
            sample: 56
        size_in_mbs:
            description:
                - The size of the volume in MBs. The value must be a multiple of 1024.
                  This field is deprecated. Please use sizeInGBs.
            returned: on success
            type: int
            sample: 56
        source_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: bootVolume
                id:
                    description:
                        - The OCID of the boot volume.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the boot volume was created. Format defined
                  by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        volume_group_id:
            description:
                - The OCID of the source volume group.
            returned: on success
            type: str
            sample: "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_id:
            description:
                - The OCID of the Key Management master encryption key assigned to the boot volume.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        is_auto_tune_enabled:
            description:
                - Specifies whether the auto-tune performance is enabled for this boot volume.
            returned: on success
            type: bool
            sample: true
        auto_tuned_vpus_per_gb:
            description:
                - The number of Volume Performance Units per GB that this boot volume is effectively tuned to when it's idle.
            returned: on success
            type: int
            sample: 56
        boot_volume_replicas:
            description:
                - The list of boot volume replicas of this boot volume
            returned: on success
            type: complex
            contains:
                display_name:
                    description:
                        - A user-friendly name. Does not have to be unique, and it's changeable.
                          Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: display_name_example
                boot_volume_replica_id:
                    description:
                        - The boot volume replica's Oracle ID (OCID).
                    returned: on success
                    type: str
                    sample: "ocid1.bootvolumereplica.oc1..xxxxxxEXAMPLExxxxxx"
                availability_domain:
                    description:
                        - The availability domain of the boot volume replica.
                        - "Example: `Uocm:PHX-AD-1`"
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
        "is_hydrated": true,
        "vpus_per_gb": 56,
        "lifecycle_state": "PROVISIONING",
        "size_in_gbs": 56,
        "size_in_mbs": 56,
        "source_details": {
            "type": "bootVolume",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "volume_group_id": "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "is_auto_tune_enabled": true,
        "auto_tuned_vpus_per_gb": 56,
        "boot_volume_replicas": [{
            "display_name": "display_name_example",
            "boot_volume_replica_id": "ocid1.bootvolumereplica.oc1..xxxxxxEXAMPLExxxxxx",
            "availability_domain": "Uocm:PHX-AD-1"
        }]
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
    from oci.core import BlockstorageClient
    from oci.core.models import ChangeBootVolumeCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BootVolumeActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "boot_volume_id"

    def get_module_resource_id(self):
        return self.module.params.get("boot_volume_id")

    def get_get_fn(self):
        return self.client.get_boot_volume

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_boot_volume,
            boot_volume_id=self.module.params.get("boot_volume_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeBootVolumeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_boot_volume_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                boot_volume_id=self.module.params.get("boot_volume_id"),
                change_boot_volume_compartment_details=action_details,
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


BootVolumeActionsHelperCustom = get_custom_class("BootVolumeActionsHelperCustom")


class ResourceHelper(BootVolumeActionsHelperCustom, BootVolumeActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            boot_volume_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="boot_volume",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
