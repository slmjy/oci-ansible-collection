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
module: oci_resource_manager_job_logs_content_facts
short_description: Fetches details about a JobLogsContent resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a JobLogsContent resource in Oracle Cloud Infrastructure
    - Returns a raw log file for the specified job. The raw log file contains console log entries in text format. The maximum number of entries in a file is
      100,000.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    job_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific job_logs_content
  oci_resource_manager_job_logs_content_facts:
    # required
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
job_logs_content:
    description:
        - JobLogsContent resource
    returned: on success
    type: str
    sample: "sample"
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.resource_manager import ResourceManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class JobLogsContentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "job_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_job_logs_content, job_id=self.module.params.get("job_id"),
        )


JobLogsContentFactsHelperCustom = get_custom_class("JobLogsContentFactsHelperCustom")


class ResourceFactsHelper(
    JobLogsContentFactsHelperCustom, JobLogsContentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(job_id=dict(aliases=["id"], type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="job_logs_content",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(job_logs_content=result)


if __name__ == "__main__":
    main()
