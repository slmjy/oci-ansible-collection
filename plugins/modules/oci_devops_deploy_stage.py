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
module: oci_devops_deploy_stage
short_description: Manage a DeployStage resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DeployStage resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new deployment stage.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    description:
        description:
            - Optional description about the deployment stage.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    deploy_stage_type:
        description:
            - Deployment stage type.
            - Required for create using I(state=present), update using I(state=present) with deploy_stage_id present.
        type: str
        choices:
            - "MANUAL_APPROVAL"
            - "WAIT"
            - "OKE_DEPLOYMENT"
            - "LOAD_BALANCER_TRAFFIC_SHIFT"
            - "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT"
            - "INVOKE_FUNCTION"
            - "DEPLOY_FUNCTION"
    deploy_pipeline_id:
        description:
            - The OCID of a pipeline.
            - Required for create using I(state=present).
        type: str
    deploy_stage_predecessor_collection:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'OKE_DEPLOYMENT', 'DEPLOY_FUNCTION', 'MANUAL_APPROVAL',
              'LOAD_BALANCER_TRAFFIC_SHIFT', 'WAIT', 'INVOKE_FUNCTION']
        type: dict
        suboptions:
            items:
                description:
                    - A list of stage predecessors for a stage.
                    - Required when deploy_stage_type is 'MANUAL_APPROVAL'
                type: list
                elements: dict
                required: true
                suboptions:
                    id:
                        description:
                            - The OCID of the predecessor stage. If a stage is the first stage in the pipeline, then the ID is the pipeline's OCID.
                            - Required when deploy_stage_type is 'MANUAL_APPROVAL'
                        type: str
                        required: true
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    approval_policy:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'MANUAL_APPROVAL'
            - Required when deploy_stage_type is 'MANUAL_APPROVAL'
        type: dict
        suboptions:
            approval_policy_type:
                description:
                    - Approval policy type.
                type: str
                choices:
                    - "COUNT_BASED_APPROVAL"
                required: true
            number_of_approvals_required:
                description:
                    - A minimum number of approvals required for stage to proceed.
                type: int
                required: true
    wait_criteria:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'WAIT'
            - Required when deploy_stage_type is 'WAIT'
        type: dict
        suboptions:
            wait_type:
                description:
                    - Wait criteria type.
                type: str
                choices:
                    - "ABSOLUTE_WAIT"
                required: true
            wait_duration:
                description:
                    - The absolute wait duration. An ISO 8601 formatted duration string. Minimum waitDuration should be 5 seconds. Maximum waitDuration can be
                      up to 2 days.
                type: str
                required: true
    oke_cluster_deploy_environment_id:
        description:
            - Kubernetes cluster environment OCID for deployment.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'OKE_DEPLOYMENT'
            - Required when deploy_stage_type is 'OKE_DEPLOYMENT'
        type: str
    kubernetes_manifest_deploy_artifact_ids:
        description:
            - List of Kubernetes manifest artifact OCIDs, the manifests should not include any job resource.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'OKE_DEPLOYMENT'
            - Required when deploy_stage_type is 'OKE_DEPLOYMENT'
        type: list
        elements: str
    namespace:
        description:
            - Default namespace to be used for Kubernetes deployment when not specified in the manifest.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'OKE_DEPLOYMENT'
        type: str
    rollback_policy:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'OKE_DEPLOYMENT', 'LOAD_BALANCER_TRAFFIC_SHIFT']
        type: dict
        suboptions:
            policy_type:
                description:
                    - Specifies type of the deployment stage rollback policy.
                type: str
                choices:
                    - "NO_STAGE_ROLLBACK_POLICY"
                    - "AUTOMATED_STAGE_ROLLBACK_POLICY"
                required: true
    blue_backend_ips:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
            - Required when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
        type: dict
        suboptions:
            items:
                description:
                    - The IP address of the backend server. A server could be a compute instance or a load balancer.
                    - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
                type: list
                elements: str
    green_backend_ips:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
            - Required when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
        type: dict
        suboptions:
            items:
                description:
                    - The IP address of the backend server. A server could be a compute instance or a load balancer.
                    - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
                type: list
                elements: str
    traffic_shift_target:
        description:
            - Specifies the target or destination backend set.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
            - Required when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
        type: str
    rollout_policy:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'LOAD_BALANCER_TRAFFIC_SHIFT']
            - Required when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'LOAD_BALANCER_TRAFFIC_SHIFT']
        type: dict
        suboptions:
            batch_count:
                description:
                    - Specifies number of batches for this stage.
                    - Required when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT', 'LOAD_BALANCER_TRAFFIC_SHIFT']
                type: int
            batch_delay_in_seconds:
                description:
                    - Specifies delay in seconds between batches. The default delay is 1 minute.
                    - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE',
                      'COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT', 'LOAD_BALANCER_TRAFFIC_SHIFT']
                type: int
            ramp_limit_percent:
                description:
                    - Indicates the criteria to stop.
                    - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
                type: float
            policy_type:
                description:
                    - The type of policy used for rolling out a deployment stage.
                type: str
                choices:
                    - "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE"
                    - "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT"
            batch_percentage:
                description:
                    - The percentage that will be used to determine how many instances will be deployed concurrently.
                    - Required when policy_type is 'COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE'
                type: int
    load_balancer_config:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'LOAD_BALANCER_TRAFFIC_SHIFT']
            - Required when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
        type: dict
        suboptions:
            load_balancer_id:
                description:
                    - The OCID of the load balancer.
                    - Required when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
                type: str
                required: true
            listener_name:
                description:
                    - Name of the load balancer listener.
                    - Required when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
                type: str
                required: true
            backend_port:
                description:
                    - Listen port for the backend server.
                    - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
                type: int
    compute_instance_group_deploy_environment_id:
        description:
            - A compute instance group environment OCID for rolling deployment.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT'
            - Required when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT'
        type: str
    deployment_spec_deploy_artifact_id:
        description:
            - The OCID of the artifact that contains the deployment specification.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT'
            - Required when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT'
        type: str
    deploy_artifact_ids:
        description:
            - Additional file artifact OCIDs.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT'
        type: list
        elements: str
    failure_policy:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT'
        type: dict
        suboptions:
            policy_type:
                description:
                    - Specifies if the failure instance size is given by absolute number or by percentage.
                type: str
                choices:
                    - "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE"
                    - "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT"
                required: true
            failure_percentage:
                description:
                    - The failure percentage threshold, which when reached or exceeded sets the stage as FAILED. Percentage is computed as the ceiling value of
                      the number of failed instances over the total count of the instances in the group.
                    - Required when policy_type is 'COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE'
                type: int
            failure_count:
                description:
                    - The threshold count of failed instances in the group, which when reached or exceeded sets the stage as FAILED.
                    - Required when policy_type is 'COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT'
                type: int
    function_deploy_environment_id:
        description:
            - Function environment OCID.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['DEPLOY_FUNCTION', 'INVOKE_FUNCTION']
            - Required when deploy_stage_type is one of ['DEPLOY_FUNCTION', 'INVOKE_FUNCTION']
        type: str
    deploy_artifact_id:
        description:
            - Optional binary artifact OCID user may provide to this stage.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'INVOKE_FUNCTION'
        type: str
    is_async:
        description:
            - A boolean flag specifies whether this stage executes asynchronously.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'INVOKE_FUNCTION'
            - Required when deploy_stage_type is 'INVOKE_FUNCTION'
        type: bool
    is_validation_enabled:
        description:
            - A boolean flag specifies whether the invoked function should be validated.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'INVOKE_FUNCTION'
            - Required when deploy_stage_type is 'INVOKE_FUNCTION'
        type: bool
    docker_image_deploy_artifact_id:
        description:
            - A Docker image artifact OCID.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'DEPLOY_FUNCTION'
            - Required when deploy_stage_type is 'DEPLOY_FUNCTION'
        type: str
    config:
        description:
            - User provided key and value pair configuration, which is assigned through constants or parameter.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'DEPLOY_FUNCTION'
        type: dict
    max_memory_in_mbs:
        description:
            - Maximum usable memory for the Function (in MB).
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'DEPLOY_FUNCTION'
        type: int
    function_timeout_in_seconds:
        description:
            - Timeout for execution of the Function. Value in seconds.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'DEPLOY_FUNCTION'
        type: int
    deploy_stage_id:
        description:
            - Unique stage identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DeployStage.
            - Use I(state=present) to create or update a DeployStage.
            - Use I(state=absent) to delete a DeployStage.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create deploy_stage with deploy_stage_type = MANUAL_APPROVAL
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: MANUAL_APPROVAL
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    approval_policy:
      # required
      approval_policy_type: COUNT_BASED_APPROVAL
      number_of_approvals_required: 56

- name: Create deploy_stage with deploy_stage_type = WAIT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: WAIT
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    wait_criteria:
      # required
      wait_type: ABSOLUTE_WAIT
      wait_duration: wait_duration_example

- name: Create deploy_stage with deploy_stage_type = OKE_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_DEPLOYMENT
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
    namespace: namespace_example
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY

- name: Create deploy_stage with deploy_stage_type = LOAD_BALANCER_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: LOAD_BALANCER_TRAFFIC_SHIFT
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    blue_backend_ips:
      # optional
      items: [ "items_example" ]
    green_backend_ips:
      # optional
      items: [ "items_example" ]
    traffic_shift_target: traffic_shift_target_example
    rollout_policy:
      # required
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE
      batch_percentage: 56

      # optional
      batch_delay_in_seconds: 56
    load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56

- name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    rollout_policy:
      # required
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE
      batch_percentage: 56

      # optional
      batch_delay_in_seconds: 56
    load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
    failure_policy:
      # required
      policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
      failure_percentage: 56

- name: Create deploy_stage with deploy_stage_type = INVOKE_FUNCTION
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: INVOKE_FUNCTION
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_id: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    is_async: true
    is_validation_enabled: true

- name: Create deploy_stage with deploy_stage_type = DEPLOY_FUNCTION
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: DEPLOY_FUNCTION
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    docker_image_deploy_artifact_id: "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    config: null
    max_memory_in_mbs: 56
    function_timeout_in_seconds: 56

- name: Update deploy_stage with deploy_stage_type = MANUAL_APPROVAL
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: MANUAL_APPROVAL

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    approval_policy:
      # required
      approval_policy_type: COUNT_BASED_APPROVAL
      number_of_approvals_required: 56

- name: Update deploy_stage with deploy_stage_type = WAIT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: WAIT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    wait_criteria:
      # required
      wait_type: ABSOLUTE_WAIT
      wait_duration: wait_duration_example

- name: Update deploy_stage with deploy_stage_type = OKE_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_DEPLOYMENT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
    namespace: namespace_example
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY

- name: Update deploy_stage with deploy_stage_type = LOAD_BALANCER_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: LOAD_BALANCER_TRAFFIC_SHIFT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    blue_backend_ips:
      # optional
      items: [ "items_example" ]
    green_backend_ips:
      # optional
      items: [ "items_example" ]
    traffic_shift_target: traffic_shift_target_example
    rollout_policy:
      # required
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE
      batch_percentage: 56

      # optional
      batch_delay_in_seconds: 56
    load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56

- name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    rollout_policy:
      # required
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE
      batch_percentage: 56

      # optional
      batch_delay_in_seconds: 56
    load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
    failure_policy:
      # required
      policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
      failure_percentage: 56

- name: Update deploy_stage with deploy_stage_type = INVOKE_FUNCTION
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: INVOKE_FUNCTION

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_id: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    is_async: true
    is_validation_enabled: true

- name: Update deploy_stage with deploy_stage_type = DEPLOY_FUNCTION
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: DEPLOY_FUNCTION

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    docker_image_deploy_artifact_id: "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    config: null
    max_memory_in_mbs: 56
    function_timeout_in_seconds: 56

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = MANUAL_APPROVAL
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: MANUAL_APPROVAL

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    approval_policy:
      # required
      approval_policy_type: COUNT_BASED_APPROVAL
      number_of_approvals_required: 56

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = WAIT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: WAIT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    wait_criteria:
      # required
      wait_type: ABSOLUTE_WAIT
      wait_duration: wait_duration_example

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_DEPLOYMENT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
    namespace: namespace_example
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = LOAD_BALANCER_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: LOAD_BALANCER_TRAFFIC_SHIFT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    blue_backend_ips:
      # optional
      items: [ "items_example" ]
    green_backend_ips:
      # optional
      items: [ "items_example" ]
    traffic_shift_target: traffic_shift_target_example
    rollout_policy:
      # required
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE
      batch_percentage: 56

      # optional
      batch_delay_in_seconds: 56
    load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56

- name: >
    Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
    with deploy_stage_type = COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    rollout_policy:
      # required
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE
      batch_percentage: 56

      # optional
      batch_delay_in_seconds: 56
    load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
    failure_policy:
      # required
      policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
      failure_percentage: 56

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = INVOKE_FUNCTION
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: INVOKE_FUNCTION

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_id: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    is_async: true
    is_validation_enabled: true

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = DEPLOY_FUNCTION
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: DEPLOY_FUNCTION

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    docker_image_deploy_artifact_id: "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    config: null
    max_memory_in_mbs: 56
    function_timeout_in_seconds: 56

- name: Delete deploy_stage
  oci_devops_deploy_stage:
    # required
    deploy_stage_id: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_deploy_stage:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
deploy_stage:
    description:
        - Details of the DeployStage resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Optional description about the deployment stage.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        project_id:
            description:
                - The OCID of a project.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_pipeline_id:
            description:
                - The OCID of a pipeline.
            returned: on success
            type: str
            sample: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type:
            description:
                - Deployment stage type.
            returned: on success
            type: str
            sample: WAIT
        time_created:
            description:
                - Time the deployment stage was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time the deployment stage was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the deployment stage.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        deploy_stage_predecessor_collection:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - A list of stage predecessors for a stage.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The OCID of the predecessor stage. If a stage is the first stage in the pipeline, then the ID is the pipeline's OCID.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\":
                  \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        compute_instance_group_deploy_environment_id:
            description:
                - A compute instance group environment OCID for rolling deployment.
            returned: on success
            type: str
            sample: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_spec_deploy_artifact_id:
            description:
                - The OCID of the artifact that contains the deployment specification.
            returned: on success
            type: str
            sample: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_ids:
            description:
                - Additional file artifact OCIDs.
            returned: on success
            type: list
            sample: []
        rollout_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                policy_type:
                    description:
                        - The type of policy used for rolling out a deployment stage.
                    returned: on success
                    type: str
                    sample: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT
                batch_delay_in_seconds:
                    description:
                        - The duration of delay between batch rollout. The default delay is 1 minute.
                    returned: on success
                    type: int
                    sample: 56
                batch_count:
                    description:
                        - The number that will be used to determine how many instances will be deployed concurrently.
                    returned: on success
                    type: int
                    sample: 56
                batch_percentage:
                    description:
                        - The percentage that will be used to determine how many instances will be deployed concurrently.
                    returned: on success
                    type: int
                    sample: 56
                ramp_limit_percent:
                    description:
                        - Indicates the criteria to stop.
                    returned: on success
                    type: float
                    sample: 3.4
        rollback_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                policy_type:
                    description:
                        - Specifies type of the deployment stage rollback policy.
                    returned: on success
                    type: str
                    sample: AUTOMATED_STAGE_ROLLBACK_POLICY
        failure_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                policy_type:
                    description:
                        - Specifies if the failure instance size is given by absolute number or by percentage.
                    returned: on success
                    type: str
                    sample: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT
                failure_count:
                    description:
                        - The threshold count of failed instances in the group, which when reached or exceeded sets the stage as FAILED.
                    returned: on success
                    type: int
                    sample: 56
                failure_percentage:
                    description:
                        - The failure percentage threshold, which when reached or exceeded sets the stage as FAILED. Percentage is computed as the ceiling value
                          of the number of failed instances over the total count of the instances in the group.
                    returned: on success
                    type: int
                    sample: 56
        load_balancer_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                load_balancer_id:
                    description:
                        - The OCID of the load balancer.
                    returned: on success
                    type: str
                    sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                listener_name:
                    description:
                        - Name of the load balancer listener.
                    returned: on success
                    type: str
                    sample: listener_name_example
                backend_port:
                    description:
                        - Listen port for the backend server.
                    returned: on success
                    type: int
                    sample: 56
        function_deploy_environment_id:
            description:
                - Function environment OCID.
            returned: on success
            type: str
            sample: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        docker_image_deploy_artifact_id:
            description:
                - A Docker image artifact OCID.
            returned: on success
            type: str
            sample: "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        config:
            description:
                - User provided key and value pair configuration, which is assigned through constants or parameter.
            returned: on success
            type: dict
            sample: {}
        max_memory_in_mbs:
            description:
                - Maximum usable memory for the Function (in MB).
            returned: on success
            type: int
            sample: 56
        function_timeout_in_seconds:
            description:
                - Timeout for execution of the Function. Value in seconds.
            returned: on success
            type: int
            sample: 56
        deploy_artifact_id:
            description:
                - Optional binary artifact OCID user may provide to this stage.
            returned: on success
            type: str
            sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        is_async:
            description:
                - A boolean flag specifies whether this stage executes asynchronously.
            returned: on success
            type: bool
            sample: true
        is_validation_enabled:
            description:
                - A boolean flag specifies whether the invoked function must be validated.
            returned: on success
            type: bool
            sample: true
        blue_backend_ips:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - The IP address of the backend server. A server could be a compute instance or a load balancer.
                    returned: on success
                    type: list
                    sample: []
        green_backend_ips:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - The IP address of the backend server. A server could be a compute instance or a load balancer.
                    returned: on success
                    type: list
                    sample: []
        traffic_shift_target:
            description:
                - Specifies the target or destination backend set.
            returned: on success
            type: str
            sample: AUTO_SELECT
        approval_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                approval_policy_type:
                    description:
                        - Approval policy type.
                    returned: on success
                    type: str
                    sample: COUNT_BASED_APPROVAL
                number_of_approvals_required:
                    description:
                        - A minimum number of approvals required for stage to proceed.
                    returned: on success
                    type: int
                    sample: 56
        oke_cluster_deploy_environment_id:
            description:
                - Kubernetes cluster environment OCID for deployment.
            returned: on success
            type: str
            sample: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        kubernetes_manifest_deploy_artifact_ids:
            description:
                - List of Kubernetes manifest artifact OCIDs, the manifests should not include any job resource.
            returned: on success
            type: list
            sample: []
        namespace:
            description:
                - Default Namespace to be used for Kubernetes deployment when not specified in the manifest.
            returned: on success
            type: str
            sample: namespace_example
        wait_criteria:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                wait_type:
                    description:
                        - Wait criteria type.
                    returned: on success
                    type: str
                    sample: ABSOLUTE_WAIT
                wait_duration:
                    description:
                        - The absolute wait duration. An ISO 8601 formatted duration string. Minimum waitDuration should be 5 seconds. Maximum waitDuration can
                          be up to 2 days.
                    returned: on success
                    type: str
                    sample: wait_duration_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_pipeline_id": "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_stage_type": "WAIT",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "deploy_stage_predecessor_collection": {
            "items": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "compute_instance_group_deploy_environment_id": "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_spec_deploy_artifact_id": "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_artifact_ids": [],
        "rollout_policy": {
            "policy_type": "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT",
            "batch_delay_in_seconds": 56,
            "batch_count": 56,
            "batch_percentage": 56,
            "ramp_limit_percent": 3.4
        },
        "rollback_policy": {
            "policy_type": "AUTOMATED_STAGE_ROLLBACK_POLICY"
        },
        "failure_policy": {
            "policy_type": "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT",
            "failure_count": 56,
            "failure_percentage": 56
        },
        "load_balancer_config": {
            "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "listener_name": "listener_name_example",
            "backend_port": 56
        },
        "function_deploy_environment_id": "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx",
        "docker_image_deploy_artifact_id": "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx",
        "config": {},
        "max_memory_in_mbs": 56,
        "function_timeout_in_seconds": 56,
        "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
        "is_async": true,
        "is_validation_enabled": true,
        "blue_backend_ips": {
            "items": []
        },
        "green_backend_ips": {
            "items": []
        },
        "traffic_shift_target": "AUTO_SELECT",
        "approval_policy": {
            "approval_policy_type": "COUNT_BASED_APPROVAL",
            "number_of_approvals_required": 56
        },
        "oke_cluster_deploy_environment_id": "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx",
        "kubernetes_manifest_deploy_artifact_ids": [],
        "namespace": "namespace_example",
        "wait_criteria": {
            "wait_type": "ABSOLUTE_WAIT",
            "wait_duration": "wait_duration_example"
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
    from oci.devops import DevopsClient
    from oci.devops.models import CreateDeployStageDetails
    from oci.devops.models import UpdateDeployStageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeployStageHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "deploy_stage_id"

    def get_module_resource_id(self):
        return self.module.params.get("deploy_stage_id")

    def get_get_fn(self):
        return self.client.get_deploy_stage

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_stage,
            deploy_stage_id=self.module.params.get("deploy_stage_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["deploy_pipeline_id", "display_name"]

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
            self.client.list_deploy_stages, **kwargs
        )

    def get_create_model_class(self):
        return CreateDeployStageDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_deploy_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(create_deploy_stage_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDeployStageDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_deploy_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deploy_stage_id=self.module.params.get("deploy_stage_id"),
                update_deploy_stage_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_deploy_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deploy_stage_id=self.module.params.get("deploy_stage_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DeployStageHelperCustom = get_custom_class("DeployStageHelperCustom")


class ResourceHelper(DeployStageHelperCustom, DeployStageHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            deploy_stage_type=dict(
                type="str",
                choices=[
                    "MANUAL_APPROVAL",
                    "WAIT",
                    "OKE_DEPLOYMENT",
                    "LOAD_BALANCER_TRAFFIC_SHIFT",
                    "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT",
                    "INVOKE_FUNCTION",
                    "DEPLOY_FUNCTION",
                ],
            ),
            deploy_pipeline_id=dict(type="str"),
            deploy_stage_predecessor_collection=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(id=dict(type="str", required=True)),
                    )
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            approval_policy=dict(
                type="dict",
                options=dict(
                    approval_policy_type=dict(
                        type="str", required=True, choices=["COUNT_BASED_APPROVAL"]
                    ),
                    number_of_approvals_required=dict(type="int", required=True),
                ),
            ),
            wait_criteria=dict(
                type="dict",
                options=dict(
                    wait_type=dict(
                        type="str", required=True, choices=["ABSOLUTE_WAIT"]
                    ),
                    wait_duration=dict(type="str", required=True),
                ),
            ),
            oke_cluster_deploy_environment_id=dict(type="str"),
            kubernetes_manifest_deploy_artifact_ids=dict(type="list", elements="str"),
            namespace=dict(type="str"),
            rollback_policy=dict(
                type="dict",
                options=dict(
                    policy_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "NO_STAGE_ROLLBACK_POLICY",
                            "AUTOMATED_STAGE_ROLLBACK_POLICY",
                        ],
                    )
                ),
            ),
            blue_backend_ips=dict(
                type="dict", options=dict(items=dict(type="list", elements="str"))
            ),
            green_backend_ips=dict(
                type="dict", options=dict(items=dict(type="list", elements="str"))
            ),
            traffic_shift_target=dict(type="str"),
            rollout_policy=dict(
                type="dict",
                options=dict(
                    batch_count=dict(type="int"),
                    batch_delay_in_seconds=dict(type="int"),
                    ramp_limit_percent=dict(type="float"),
                    policy_type=dict(
                        type="str",
                        choices=[
                            "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE",
                            "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT",
                        ],
                    ),
                    batch_percentage=dict(type="int"),
                ),
            ),
            load_balancer_config=dict(
                type="dict",
                options=dict(
                    load_balancer_id=dict(type="str", required=True),
                    listener_name=dict(type="str", required=True),
                    backend_port=dict(type="int"),
                ),
            ),
            compute_instance_group_deploy_environment_id=dict(type="str"),
            deployment_spec_deploy_artifact_id=dict(type="str"),
            deploy_artifact_ids=dict(type="list", elements="str"),
            failure_policy=dict(
                type="dict",
                options=dict(
                    policy_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE",
                            "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT",
                        ],
                    ),
                    failure_percentage=dict(type="int"),
                    failure_count=dict(type="int"),
                ),
            ),
            function_deploy_environment_id=dict(type="str"),
            deploy_artifact_id=dict(type="str"),
            is_async=dict(type="bool"),
            is_validation_enabled=dict(type="bool"),
            docker_image_deploy_artifact_id=dict(type="str"),
            config=dict(type="dict"),
            max_memory_in_mbs=dict(type="int"),
            function_timeout_in_seconds=dict(type="int"),
            deploy_stage_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deploy_stage",
        service_client_class=DevopsClient,
        namespace="devops",
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
