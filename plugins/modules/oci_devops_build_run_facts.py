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
module: oci_devops_build_run_facts
short_description: Fetches details about one or multiple BuildRun resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BuildRun resources in Oracle Cloud Infrastructure
    - Returns a list of build run summary.
    - If I(build_run_id) is specified, the details of a single BuildRun will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    build_run_id:
        description:
            - Unique build run identifier.
            - Required to get a specific build_run.
        type: str
        aliases: ["id"]
    build_pipeline_id:
        description:
            - Unique build pipeline identifier.
        type: str
    project_id:
        description:
            - unique project identifier
        type: str
    compartment_id:
        description:
            - The OCID of the compartment in which to list resources.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only build runs that matches the given lifecycle state.
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "FAILED"
            - "SUCCEEDED"
            - "CANCELING"
            - "CANCELED"
    sort_order:
        description:
            - The sort order to use. Use either ascending or descending.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is
              ascending. If no value is specified, then the default time created value is considered.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific build_run
  oci_devops_build_run_facts:
    # required
    build_run_id: "ocid1.buildrun.oc1..xxxxxxEXAMPLExxxxxx"

- name: List build_runs
  oci_devops_build_run_facts:

    # optional
    build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: ACCEPTED
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
build_runs:
    description:
        - List of BuildRun resources
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
                - Build run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment where the build is running.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        project_id:
            description:
                - The OCID of the DevOps project.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        build_pipeline_id:
            description:
                - The OCID of the build pipeline.
            returned: on success
            type: str
            sample: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
        build_run_source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                source_type:
                    description:
                        - The source from which the build run is triggered.
                    returned: on success
                    type: str
                    sample: MANUAL
                trigger_id:
                    description:
                        - The trigger that invoked the build run.
                    returned: on success
                    type: str
                    sample: "ocid1.trigger.oc1..xxxxxxEXAMPLExxxxxx"
                trigger_info:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        display_name:
                            description:
                                - Name for Trigger.
                            returned: on success
                            type: str
                            sample: display_name_example
                        actions:
                            description:
                                - The list of actions that are to be performed for this Trigger
                            returned: on success
                            type: complex
                            contains:
                                type:
                                    description:
                                        - The type of action that will be taken. Allowed value is TRIGGER_BUILD_PIPELINE.
                                    returned: on success
                                    type: str
                                    sample: TRIGGER_BUILD_PIPELINE
                                filter:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        trigger_source:
                                            description:
                                                - Source of the trigger. Allowed values are, GITHUB and GITLAB.
                                            returned: on success
                                            type: str
                                            sample: DEVOPS_CODE_REPOSITORY
                                        events:
                                            description:
                                                - The events only support PUSH.
                                            returned: on success
                                            type: list
                                            sample: []
                                        include:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                head_ref:
                                                    description:
                                                        - Branch for push event.
                                                    returned: on success
                                                    type: str
                                                    sample: head_ref_example
                                                base_ref:
                                                    description:
                                                        - The target branch for pull requests; not applicable for push requests.
                                                    returned: on success
                                                    type: str
                                                    sample: base_ref_example
                                build_pipeline_id:
                                    description:
                                        - The OCID of the build pipeline to be triggered.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
                repository_id:
                    description:
                        - The DevOps code repository identifier that invoked the build run.
                    returned: on success
                    type: str
                    sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
        build_run_arguments:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of arguments provided at the time of running the build.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - "Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$.
                                  Example: 'Build_Pipeline_param' is not same as 'build_pipeline_Param'"
                            returned: on success
                            type: str
                            sample: name_example
                        value:
                            description:
                                - Value of the argument.
                            returned: on success
                            type: str
                            sample: value_example
        time_created:
            description:
                - The time the build run was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the build run was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the build run.
            returned: on success
            type: str
            sample: ACCEPTED
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        build_run_progress:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                time_started:
                    description:
                        - The time the build run started. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_finished:
                    description:
                        - The time the build run finished. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                build_pipeline_stage_run_progress:
                    description:
                        - Map of stage OCIDs to build pipeline stage run progress model.
                    returned: on success
                    type: complex
                    contains:
                        stage_display_name:
                            description:
                                - Build Run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: stage_display_name_example
                        build_pipeline_stage_type:
                            description:
                                - Stage types.
                            returned: on success
                            type: str
                            sample: BUILD
                        build_pipeline_stage_id:
                            description:
                                - The stage OCID.
                            returned: on success
                            type: str
                            sample: "ocid1.buildpipelinestage.oc1..xxxxxxEXAMPLExxxxxx"
                        time_started:
                            description:
                                - The time the stage started executing. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_finished:
                            description:
                                - The time the stage finished executing. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        status:
                            description:
                                - The current status of the stage.
                            returned: on success
                            type: str
                            sample: ACCEPTED
                        build_pipeline_stage_predecessors:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - A list of build pipeline stage predecessors for a stage.
                                    returned: on success
                                    type: complex
                                    contains:
                                        id:
                                            description:
                                                - The ID of the predecessor stage. If a stage is the first stage in the pipeline, then the ID is the pipeline's
                                                  ID.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        actual_build_runner_shape:
                            description:
                                - Name of Build Runner shape where this Build Stage is running.
                            returned: on success
                            type: str
                            sample: actual_build_runner_shape_example
                        actual_build_runner_shape_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                ocpus:
                                    description:
                                        - The total number of OCPUs set for the instance.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                memory_in_gbs:
                                    description:
                                        - The total amount of memory set for the instance in gigabytes.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                        image:
                            description:
                                - Image name for the Build Environment
                            returned: on success
                            type: str
                            sample: OL7_X86_64_STANDARD_10
                        build_spec_file:
                            description:
                                - The path to the build specification file for this Environment. The default location if not specified is build_spec.yaml
                            returned: on success
                            type: str
                            sample: build_spec_file_example
                        stage_execution_timeout_in_seconds:
                            description:
                                - Timeout for the Build Stage Execution. Value in seconds.
                            returned: on success
                            type: int
                            sample: 56
                        build_source_collection:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - Collection of build sources. In case of UPDATE operation, replaces existing build sources list. Merging with existing
                                          build sources is not supported.
                                    returned: on success
                                    type: complex
                                    contains:
                                        name:
                                            description:
                                                - Name of the build source. This must be unique within a build source collection. The name can be used by
                                                  customers to locate the working directory pertinent to this repository.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        connection_type:
                                            description:
                                                - The type of source provider.
                                            returned: on success
                                            type: str
                                            sample: GITHUB
                                        repository_url:
                                            description:
                                                - URL for the repository.
                                            returned: on success
                                            type: str
                                            sample: repository_url_example
                                        branch:
                                            description:
                                                - Branch name.
                                            returned: on success
                                            type: str
                                            sample: branch_example
                                        repository_id:
                                            description:
                                                - The DevOps code repository ID.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
                                        connection_id:
                                            description:
                                                - Connection identifier pertinent to GitHub source provider.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
                        primary_build_source:
                            description:
                                - Name of the BuildSource in which the build_spec.yml file need to be located. If not specified, the 1st entry in the
                                  BuildSource collection will be chosen as Primary.
                            returned: on success
                            type: str
                            sample: primary_build_source_example
                        steps:
                            description:
                                - The details about all the steps in a Build stage
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - Name of the step.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                state:
                                    description:
                                        - State of the step.
                                    returned: on success
                                    type: str
                                    sample: WAITING
                                time_started:
                                    description:
                                        - Time when the step started.
                                    returned: on success
                                    type: str
                                    sample: "2013-10-20T19:20:30+01:00"
                                time_finished:
                                    description:
                                        - Time when the step finished.
                                    returned: on success
                                    type: str
                                    sample: "2013-10-20T19:20:30+01:00"
                        exported_variables:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - List of exported variables.
                                    returned: on success
                                    type: complex
                                    contains:
                                        name:
                                            description:
                                                - "Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$."
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        value:
                                            description:
                                                - Value of the argument.
                                            returned: on success
                                            type: str
                                            sample: value_example
                        delivered_artifacts:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - List of artifacts delivered through the Deliver Artifacts stage.
                                    returned: on success
                                    type: complex
                                    contains:
                                        deploy_artifact_id:
                                            description:
                                                - The OCID of the deployment artifact definition.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                                        output_artifact_name:
                                            description:
                                                - Name of the output artifact defined in the build specification file.
                                            returned: on success
                                            type: str
                                            sample: output_artifact_name_example
                                        artifact_type:
                                            description:
                                                - Type of artifact delivered.
                                            returned: on success
                                            type: str
                                            sample: GENERIC_ARTIFACT
                                        artifact_repository_id:
                                            description:
                                                - The OCID of the artifact registry repository used by the DeliverArtifactStage
                                            returned: on success
                                            type: str
                                            sample: "ocid1.artifactrepository.oc1..xxxxxxEXAMPLExxxxxx"
                                        delivered_artifact_id:
                                            description:
                                                - The OCID of the artifact pushed by the Deliver Artifacts stage.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.deliveredartifact.oc1..xxxxxxEXAMPLExxxxxx"
                                        path:
                                            description:
                                                - Path of the repository where artifact was pushed
                                            returned: on success
                                            type: str
                                            sample: path_example
                                        version:
                                            description:
                                                - Version of the artifact pushed
                                            returned: on success
                                            type: str
                                            sample: version_example
                                        delivered_artifact_hash:
                                            description:
                                                - The hash of the container registry artifact pushed by the Deliver Artifacts stage.
                                            returned: on success
                                            type: str
                                            sample: delivered_artifact_hash_example
                                        image_uri:
                                            description:
                                                - The imageUri of the OCIR artifact pushed by the DeliverArtifactStage
                                            returned: on success
                                            type: str
                                            sample: image_uri_example
                        artifact_override_parameters:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - List of artifact override arguments at the time of deployment.
                                    returned: on success
                                    type: complex
                                    contains:
                                        deploy_artifact_id:
                                            description:
                                                - The OCID of the artifact to which this parameter applies.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                                        name:
                                            description:
                                                - Name of the parameter (case-sensitive).
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        value:
                                            description:
                                                - Value of the parameter.
                                            returned: on success
                                            type: str
                                            sample: value_example
                        deployment_id:
                            description:
                                - Identifier of the deployment triggered.
                            returned: on success
                            type: str
                            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        commit_info:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                repository_url:
                    description:
                        - Repository URL.
                    returned: on success
                    type: str
                    sample: repository_url_example
                repository_branch:
                    description:
                        - Name of the repository branch.
                    returned: on success
                    type: str
                    sample: repository_branch_example
                commit_hash:
                    description:
                        - Commit hash pertinent to the repository URL and the specified branch.
                    returned: on success
                    type: str
                    sample: commit_hash_example
        build_outputs:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                exported_variables:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        items:
                            description:
                                - List of exported variables.
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - "Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$."
                                    returned: on success
                                    type: str
                                    sample: name_example
                                value:
                                    description:
                                        - Value of the argument.
                                    returned: on success
                                    type: str
                                    sample: value_example
                delivered_artifacts:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        items:
                            description:
                                - List of artifacts delivered through the Deliver Artifacts stage.
                            returned: on success
                            type: complex
                            contains:
                                deploy_artifact_id:
                                    description:
                                        - The OCID of the deployment artifact definition.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                                output_artifact_name:
                                    description:
                                        - Name of the output artifact defined in the build specification file.
                                    returned: on success
                                    type: str
                                    sample: output_artifact_name_example
                                artifact_type:
                                    description:
                                        - Type of artifact delivered.
                                    returned: on success
                                    type: str
                                    sample: GENERIC_ARTIFACT
                                artifact_repository_id:
                                    description:
                                        - The OCID of the artifact registry repository used by the DeliverArtifactStage
                                    returned: on success
                                    type: str
                                    sample: "ocid1.artifactrepository.oc1..xxxxxxEXAMPLExxxxxx"
                                delivered_artifact_id:
                                    description:
                                        - The OCID of the artifact pushed by the Deliver Artifacts stage.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.deliveredartifact.oc1..xxxxxxEXAMPLExxxxxx"
                                path:
                                    description:
                                        - Path of the repository where artifact was pushed
                                    returned: on success
                                    type: str
                                    sample: path_example
                                version:
                                    description:
                                        - Version of the artifact pushed
                                    returned: on success
                                    type: str
                                    sample: version_example
                                delivered_artifact_hash:
                                    description:
                                        - The hash of the container registry artifact pushed by the Deliver Artifacts stage.
                                    returned: on success
                                    type: str
                                    sample: delivered_artifact_hash_example
                                image_uri:
                                    description:
                                        - The imageUri of the OCIR artifact pushed by the DeliverArtifactStage
                                    returned: on success
                                    type: str
                                    sample: image_uri_example
                artifact_override_parameters:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        items:
                            description:
                                - List of artifact override arguments at the time of deployment.
                            returned: on success
                            type: complex
                            contains:
                                deploy_artifact_id:
                                    description:
                                        - The OCID of the artifact to which this parameter applies.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                                name:
                                    description:
                                        - Name of the parameter (case-sensitive).
                                    returned: on success
                                    type: str
                                    sample: name_example
                                value:
                                    description:
                                        - Value of the parameter.
                                    returned: on success
                                    type: str
                                    sample: value_example
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
        build_run_progress_summary:
            description:
                - ""
                - Returned for list operation
            returned: on success
            type: complex
            contains:
                time_started:
                    description:
                        - The time the build run started. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_finished:
                    description:
                        - The time the build run finished. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "build_pipeline_id": "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx",
        "build_run_source": {
            "source_type": "MANUAL",
            "trigger_id": "ocid1.trigger.oc1..xxxxxxEXAMPLExxxxxx",
            "trigger_info": {
                "display_name": "display_name_example",
                "actions": [{
                    "type": "TRIGGER_BUILD_PIPELINE",
                    "filter": {
                        "trigger_source": "DEVOPS_CODE_REPOSITORY",
                        "events": [],
                        "include": {
                            "head_ref": "head_ref_example",
                            "base_ref": "base_ref_example"
                        }
                    },
                    "build_pipeline_id": "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
                }]
            },
            "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "build_run_arguments": {
            "items": [{
                "name": "name_example",
                "value": "value_example"
            }]
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACCEPTED",
        "lifecycle_details": "lifecycle_details_example",
        "build_run_progress": {
            "time_started": "2013-10-20T19:20:30+01:00",
            "time_finished": "2013-10-20T19:20:30+01:00",
            "build_pipeline_stage_run_progress": {
                "stage_display_name": "stage_display_name_example",
                "build_pipeline_stage_type": "BUILD",
                "build_pipeline_stage_id": "ocid1.buildpipelinestage.oc1..xxxxxxEXAMPLExxxxxx",
                "time_started": "2013-10-20T19:20:30+01:00",
                "time_finished": "2013-10-20T19:20:30+01:00",
                "status": "ACCEPTED",
                "build_pipeline_stage_predecessors": {
                    "items": [{
                        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                    }]
                },
                "actual_build_runner_shape": "actual_build_runner_shape_example",
                "actual_build_runner_shape_config": {
                    "ocpus": 1.2,
                    "memory_in_gbs": 1.2
                },
                "image": "OL7_X86_64_STANDARD_10",
                "build_spec_file": "build_spec_file_example",
                "stage_execution_timeout_in_seconds": 56,
                "build_source_collection": {
                    "items": [{
                        "name": "name_example",
                        "connection_type": "GITHUB",
                        "repository_url": "repository_url_example",
                        "branch": "branch_example",
                        "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
                        "connection_id": "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
                    }]
                },
                "primary_build_source": "primary_build_source_example",
                "steps": [{
                    "name": "name_example",
                    "state": "WAITING",
                    "time_started": "2013-10-20T19:20:30+01:00",
                    "time_finished": "2013-10-20T19:20:30+01:00"
                }],
                "exported_variables": {
                    "items": [{
                        "name": "name_example",
                        "value": "value_example"
                    }]
                },
                "delivered_artifacts": {
                    "items": [{
                        "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                        "output_artifact_name": "output_artifact_name_example",
                        "artifact_type": "GENERIC_ARTIFACT",
                        "artifact_repository_id": "ocid1.artifactrepository.oc1..xxxxxxEXAMPLExxxxxx",
                        "delivered_artifact_id": "ocid1.deliveredartifact.oc1..xxxxxxEXAMPLExxxxxx",
                        "path": "path_example",
                        "version": "version_example",
                        "delivered_artifact_hash": "delivered_artifact_hash_example",
                        "image_uri": "image_uri_example"
                    }]
                },
                "artifact_override_parameters": {
                    "items": [{
                        "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                        "name": "name_example",
                        "value": "value_example"
                    }]
                },
                "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
            }
        },
        "commit_info": {
            "repository_url": "repository_url_example",
            "repository_branch": "repository_branch_example",
            "commit_hash": "commit_hash_example"
        },
        "build_outputs": {
            "exported_variables": {
                "items": [{
                    "name": "name_example",
                    "value": "value_example"
                }]
            },
            "delivered_artifacts": {
                "items": [{
                    "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                    "output_artifact_name": "output_artifact_name_example",
                    "artifact_type": "GENERIC_ARTIFACT",
                    "artifact_repository_id": "ocid1.artifactrepository.oc1..xxxxxxEXAMPLExxxxxx",
                    "delivered_artifact_id": "ocid1.deliveredartifact.oc1..xxxxxxEXAMPLExxxxxx",
                    "path": "path_example",
                    "version": "version_example",
                    "delivered_artifact_hash": "delivered_artifact_hash_example",
                    "image_uri": "image_uri_example"
                }]
            },
            "artifact_override_parameters": {
                "items": [{
                    "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                    "name": "name_example",
                    "value": "value_example"
                }]
            }
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "build_run_progress_summary": {
            "time_started": "2013-10-20T19:20:30+01:00",
            "time_finished": "2013-10-20T19:20:30+01:00"
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BuildRunFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "build_run_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_build_run,
            build_run_id=self.module.params.get("build_run_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "build_pipeline_id",
            "project_id",
            "compartment_id",
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
            self.client.list_build_runs, **optional_kwargs
        )


BuildRunFactsHelperCustom = get_custom_class("BuildRunFactsHelperCustom")


class ResourceFactsHelper(BuildRunFactsHelperCustom, BuildRunFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            build_run_id=dict(aliases=["id"], type="str"),
            build_pipeline_id=dict(type="str"),
            project_id=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "IN_PROGRESS",
                    "FAILED",
                    "SUCCEEDED",
                    "CANCELING",
                    "CANCELED",
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
        resource_type="build_run",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(build_runs=result)


if __name__ == "__main__":
    main()
