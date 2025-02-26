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
module: oci_generic_artifacts_content_generic_artifact_facts
short_description: Fetches details about a GenericArtifact resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a GenericArtifact resource in Oracle Cloud Infrastructure
    - Gets the specified artifact's content.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
        type: str
        required: true
    artifact_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the artifact.
            - "Example: `ocid1.genericartifact.oc1..exampleuniqueID`"
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific generic_artifact
  oci_generic_artifacts_content_generic_artifact_facts:
    # required
    dest: /tmp/myfile
    artifact_id: "ocid1.artifact.oc1..xxxxxxEXAMPLExxxxxx"

"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.generic_artifacts_content import GenericArtifactsContentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GenericArtifactFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "artifact_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_generic_artifact_content,
            artifact_id=self.module.params.get("artifact_id"),
        )

    def get(self):
        response = self.get_resource().data
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None


GenericArtifactFactsHelperCustom = get_custom_class("GenericArtifactFactsHelperCustom")


class ResourceFactsHelper(
    GenericArtifactFactsHelperCustom, GenericArtifactFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dest=dict(type="str", required=True),
            artifact_id=dict(aliases=["id"], type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="generic_artifact",
        service_client_class=GenericArtifactsContentClient,
        namespace="generic_artifacts_content",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(generic_artifact=result)


if __name__ == "__main__":
    main()
