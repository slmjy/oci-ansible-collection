.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na

.. Anchors

.. _ansible_collections.oracle.oci.oci_compute_management_instance_configuration_actions_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_compute_management_instance_configuration_actions -- Perform actions on an InstanceConfiguration resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 2.37.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_compute_management_instance_configuration_actions`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Perform actions on an InstanceConfiguration resource in Oracle Cloud Infrastructure
- For *action=change_compartment*, moves an instance configuration into a different compartment within the same tenancy. For information about moving resources between compartments, see `Moving Resources to a Different Compartment <https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes>`_. When you move an instance configuration to a different compartment, associated resources such as instance pools are not moved. **Important:** Most of the properties for an existing instance configuration, including the compartment, cannot be modified after you create the instance configuration. Although you can move an instance configuration to a different compartment, you will not be able to use the instance configuration to manage instance pools in the new compartment. If you want to update an instance configuration to point to a different compartment, you should instead create a new instance configuration in the target compartment using `CreateInstanceConfiguration <https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/InstanceConfiguration/CreateInstanceConfiguration>`_.
- For *action=launch*, launches an instance from an instance configuration. If the instance configuration does not include all of the parameters that are required to launch an instance, such as the availability domain and subnet ID, you must provide these parameters when you launch an instance from the instance configuration. For more information, see the `InstanceConfiguration <https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/InstanceConfiguration/>`_ resource.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 3.6
- Python SDK for Oracle Cloud Infrastructure https://oracle-cloud-infrastructure-python-sdk.readthedocs.io


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>change_compartment</li>
                                                                                                                                                                                                <li>launch</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to perform on the InstanceConfiguration.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-api_user"></div>
                    <b>api_user</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_ID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user&#x27;s OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-api_user_fingerprint"></div>
                    <b>api_user_fingerprint</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user_fingerprint" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair&#x27;s fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-api_user_key_file"></div>
                    <b>api_user_key_file</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user_key_file" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Full path and filename of the private key (in PEM format). If not set, then the value of the OCI_USER_KEY_FILE variable, if any, is used. This option is required if the private key is not specified through a configuration file (See <code>config_file_location</code>). If the key is encrypted with a pass-phrase, the <code>api_user_key_pass_phrase</code> option must also be provided.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-api_user_key_pass_phrase"></div>
                    <b>api_user_key_pass_phrase</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user_key_pass_phrase" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Passphrase used by the key referenced in <code>api_user_key_file</code>, if it is encrypted. If not set, then the value of the OCI_USER_KEY_PASS_PHRASE variable, if any, is used. This option is required if the key passphrase is not specified through a configuration file (See <code>config_file_location</code>).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-auth_type"></div>
                    <b>auth_type</b>
                    <a class="ansibleOptionLink" href="#parameter-auth_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>api_key</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>instance_principal</li>
                                                                                                                                                                                                <li>instance_obo_user</li>
                                                                                                                                                                                                <li>resource_principal</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes"></div>
                    <b>block_volumes</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable only for <em>action=launch</em>.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/attach_details"></div>
                    <b>attach_details</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/attach_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/attach_details/device"></div>
                    <b>device</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/attach_details/device" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The device name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/attach_details/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/attach_details/display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/attach_details/is_pv_encryption_in_transit_enabled"></div>
                    <b>is_pv_encryption_in_transit_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/attach_details/is_pv_encryption_in_transit_enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to enable in-transit encryption for the data volume&#x27;s paravirtualized attachment. The default value is false.</div>
                                            <div>Applicable when type is &#x27;paravirtualized&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/attach_details/is_read_only"></div>
                    <b>is_read_only</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/attach_details/is_read_only" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether the attachment should be created in read-only mode.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/attach_details/is_shareable"></div>
                    <b>is_shareable</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/attach_details/is_shareable" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether the attachment should be created in shareable mode. If an attachment is created in shareable mode, then other instances can attach the same volume, provided that they also create their attachments in shareable mode. Only certain volume types can be attached in shareable mode. Defaults to false if not specified.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/attach_details/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/attach_details/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>iscsi</li>
                                                                                                                                                                                                <li>paravirtualized</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of volume. The only supported values are &quot;iscsi&quot; and &quot;paravirtualized&quot;.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/attach_details/use_chap"></div>
                    <b>use_chap</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/attach_details/use_chap" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to use CHAP authentication for the volume attachment. Defaults to false.</div>
                                            <div>Applicable when type is &#x27;iscsi&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details"></div>
                    <b>create_details</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details/availability_domain"></div>
                    <b>availability_domain</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details/availability_domain" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The availability domain of the volume.</div>
                                            <div>Example: `Uocm:PHX-AD-1`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details/backup_policy_id"></div>
                    <b>backup_policy_id</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details/backup_policy_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>If provided, specifies the ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be assigned.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details/compartment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the compartment that contains the volume.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details/defined_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Operations&quot;: {&quot;CostCenter&quot;: &quot;42&quot;}}`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details/display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details/freeform_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details/kms_key_id"></div>
                    <b>kms_key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details/kms_key_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the Key Management key to assign as the master encryption key for the volume.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details/size_in_gbs"></div>
                    <b>size_in_gbs</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details/size_in_gbs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The size of the volume in GBs.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details/source_details"></div>
                    <b>source_details</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details/source_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details/source_details/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details/source_details/id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the volume backup.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details/source_details/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details/source_details/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>volumeBackup</li>
                                                                                                                                                                                                <li>volume</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/create_details/vpus_per_gb"></div>
                    <b>vpus_per_gb</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/create_details/vpus_per_gb" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service&#x27;s elastic performance options. See <a href='https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeelasticperformance.htm'>Block Volume Elastic Performance</a> for more information.</div>
                                            <div>Allowed values:</div>
                                            <div>* `0`: Represents Lower Cost option.</div>
                                            <div>* `10`: Represents Balanced option.</div>
                                            <div>* `20`: Represents Higher Performance option.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-block_volumes/volume_id"></div>
                    <b>volume_id</b>
                    <a class="ansibleOptionLink" href="#parameter-block_volumes/volume_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the volume.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-compartment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment to move the instance configuration to.</div>
                                            <div>Required for <em>action=change_compartment</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-config_file_location"></div>
                    <b>config_file_location</b>
                    <a class="ansibleOptionLink" href="#parameter-config_file_location" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Path to configuration file. If not set then the value of the OCI_CONFIG_FILE environment variable, if any, is used. Otherwise, defaults to ~/.oci/config.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-config_profile_name"></div>
                    <b>config_profile_name</b>
                    <a class="ansibleOptionLink" href="#parameter-config_profile_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-instance_configuration_id"></div>
                    <b>instance_configuration_id</b>
                    <a class="ansibleOptionLink" href="#parameter-instance_configuration_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the instance configuration.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-instance_type"></div>
                    <b>instance_type</b>
                    <a class="ansibleOptionLink" href="#parameter-instance_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>compute</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of instance details. Supported instanceType is compute</div>
                                            <div>Required for <em>action=launch</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details"></div>
                    <b>launch_details</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable only for <em>action=launch</em>.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/agent_config"></div>
                    <b>agent_config</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/agent_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/agent_config/are_all_plugins_disabled"></div>
                    <b>are_all_plugins_disabled</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/agent_config/are_all_plugins_disabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether Oracle Cloud Agent can run all the available plugins. This includes the management and monitoring plugins.</div>
                                            <div>To get a list of available plugins, use the <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins'>ListInstanceagentAvailablePlugins</a> operation in the Oracle Cloud Agent API. For more information about the available plugins, see <a href='https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm'>Managing Plugins with Oracle Cloud Agent</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/agent_config/is_management_disabled"></div>
                    <b>is_management_disabled</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/agent_config/is_management_disabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether Oracle Cloud Agent can run all the available management plugins. Default value is false (management plugins are enabled).</div>
                                            <div>These are the management plugins: OS Management Service Agent and Compute Instance Run Command.</div>
                                            <div>The management plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object.</div>
                                            <div>- If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of the per-plugin configuration. - If `isManagementDisabled` is false, all of the management plugins are enabled. You can optionally disable individual management plugins by providing a value in the `pluginsConfig` object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/agent_config/is_monitoring_disabled"></div>
                    <b>is_monitoring_disabled</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/agent_config/is_monitoring_disabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the monitoring plugins. Default value is false (monitoring plugins are enabled).</div>
                                            <div>These are the monitoring plugins: Compute Instance Monitoring and Custom Logs Monitoring.</div>
                                            <div>The monitoring plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object.</div>
                                            <div>- If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of the per-plugin configuration. - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig` object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/agent_config/plugins_config"></div>
                    <b>plugins_config</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/agent_config/plugins_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration of plugins associated with this instance.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/agent_config/plugins_config/desired_state"></div>
                    <b>desired_state</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/agent_config/plugins_config/desired_state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ENABLED</li>
                                                                                                                                                                                                <li>DISABLED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether the plugin should be enabled or disabled.</div>
                                            <div>To enable the monitoring and management plugins, the `isMonitoringDisabled` and `isManagementDisabled` attributes must also be set to false.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/agent_config/plugins_config/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/agent_config/plugins_config/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The plugin name. To get a list of available plugins, use the <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins'>ListInstanceagentAvailablePlugins</a> operation in the Oracle Cloud Agent API. For more information about the available plugins, see <a href='https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm'>Managing Plugins with Oracle Cloud Agent</a>.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/availability_config"></div>
                    <b>availability_config</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/availability_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/availability_config/recovery_action"></div>
                    <b>recovery_action</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/availability_config/recovery_action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>RESTORE_INSTANCE</li>
                                                                                                                                                                                                <li>STOP_INSTANCE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The lifecycle state for an instance when it is recovered after infrastructure maintenance. * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event. If the instance was running, it is automatically rebooted. This is the default action when a value is not set. * `STOP_INSTANCE` - The instance is recovered in the stopped state.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/availability_domain"></div>
                    <b>availability_domain</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/availability_domain" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The availability domain of the instance.</div>
                                            <div>Example: `Uocm:PHX-AD-1`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/capacity_reservation_id"></div>
                    <b>capacity_reservation_id</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/capacity_reservation_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the compute capacity reservation this instance is launched under.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/compartment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the compartment containing the instance. Instances created from instance configurations are placed in the same compartment as the instance that was used to create the instance configuration.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/create_vnic_details"></div>
                    <b>create_vnic_details</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/create_vnic_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/create_vnic_details/assign_private_dns_record"></div>
                    <b>assign_private_dns_record</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/create_vnic_details/assign_private_dns_record" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/'>CreateVnicDetails</a> for more information.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/create_vnic_details/assign_public_ip"></div>
                    <b>assign_public_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/create_vnic_details/assign_public_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/'>CreateVnicDetails</a> for more information.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/create_vnic_details/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/create_vnic_details/defined_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Operations&quot;: {&quot;CostCenter&quot;: &quot;42&quot;}}`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/create_vnic_details/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/create_vnic_details/display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/create_vnic_details/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/create_vnic_details/freeform_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/create_vnic_details/hostname_label"></div>
                    <b>hostname_label</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/create_vnic_details/hostname_label" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The hostname for the VNIC&#x27;s primary private IP. See the `hostnameLabel` attribute of <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/CreateVnicDetails/'>CreateVnicDetails</a> for more information.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/create_vnic_details/nsg_ids"></div>
                    <b>nsg_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/create_vnic_details/nsg_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more information about NSGs, see <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/'>NetworkSecurityGroup</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/create_vnic_details/private_ip"></div>
                    <b>private_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/create_vnic_details/private_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A private IP address of your choice to assign to the VNIC. See the `privateIp` attribute of <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/CreateVnicDetails/'>CreateVnicDetails</a> for more information.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/create_vnic_details/skip_source_dest_check"></div>
                    <b>skip_source_dest_check</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/create_vnic_details/skip_source_dest_check" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether the source/destination check is disabled on the VNIC. See the `skipSourceDestCheck` attribute of <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/CreateVnicDetails/'>CreateVnicDetails</a> for more information.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/create_vnic_details/subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/create_vnic_details/subnet_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the subnet to create the VNIC in. See the `subnetId` attribute of <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/CreateVnicDetails/'>CreateVnicDetails</a> for more information.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/dedicated_vm_host_id"></div>
                    <b>dedicated_vm_host_id</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/dedicated_vm_host_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of dedicated VM host.</div>
                                            <div>Dedicated VM hosts can be used when launching individual instances from an instance configuration. They cannot be used to launch instance pools.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/defined_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Operations&quot;: {&quot;CostCenter&quot;: &quot;42&quot;}}`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/extended_metadata"></div>
                    <b>extended_metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/extended_metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object.</div>
                                            <div>They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only).</div>
                                            <div>The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/fault_domain"></div>
                    <b>fault_domain</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/fault_domain" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains.</div>
                                            <div>If you do not specify the fault domain, the system selects one for you.</div>
                                            <div>To get a list of fault domains, use the <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/FaultDomain/ListFaultDomains'>ListFaultDomains</a> operation in the Identity and Access Management Service API.</div>
                                            <div>Example: `FAULT-DOMAIN-1`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/freeform_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/instance_options"></div>
                    <b>instance_options</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/instance_options" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/instance_options/are_legacy_imds_endpoints_disabled"></div>
                    <b>are_legacy_imds_endpoints_disabled</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/instance_options/are_legacy_imds_endpoints_disabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to disable the legacy (/v1) instance metadata service endpoints. Customers who have migrated to /v2 should set this to true for added security. Default is false.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/ipxe_script"></div>
                    <b>ipxe_script</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/ipxe_script" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This is an advanced option.</div>
                                            <div>When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process.</div>
                                            <div>If you want more control over the boot process, you can provide your own custom iPXE script that will run when the instance boots; however, you should be aware that the same iPXE script will run every time an instance boots; not only after the initial LaunchInstance call.</div>
                                            <div>The default iPXE script connects to the instance&#x27;s local boot volume over iSCSI and performs a network boot. If you use a custom iPXE script and want to network-boot from the instance&#x27;s local boot volume over iSCSI the same way as the default iPXE script, you should use the following iSCSI IP address: 169.254.0.2, and boot volume IQN: iqn.2015-02.oracle.boot.</div>
                                            <div>For more information about the Bring Your Own Image feature of Oracle Cloud Infrastructure, see <a href='https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm'>Bring Your Own Image</a>.</div>
                                            <div>For more information about iPXE, see http://ipxe.org.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/is_pv_encryption_in_transit_enabled"></div>
                    <b>is_pv_encryption_in_transit_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/is_pv_encryption_in_transit_enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to enable in-transit encryption for the data volume&#x27;s paravirtualized attachment. The default value is false.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/launch_mode"></div>
                    <b>launch_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/launch_mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>NATIVE</li>
                                                                                                                                                                                                <li>EMULATED</li>
                                                                                                                                                                                                <li>PARAVIRTUALIZED</li>
                                                                                                                                                                                                <li>CUSTOM</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are: * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images. * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers. * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/launch_options"></div>
                    <b>launch_options</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/launch_options" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/launch_options/boot_volume_type"></div>
                    <b>boot_volume_type</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/launch_options/boot_volume_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ISCSI</li>
                                                                                                                                                                                                <li>SCSI</li>
                                                                                                                                                                                                <li>IDE</li>
                                                                                                                                                                                                <li>VFIO</li>
                                                                                                                                                                                                <li>PARAVIRTUALIZED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Emulation type for the boot volume. * `ISCSI` - ISCSI attached block storage device. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data volumes on platform images. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on platform images.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/launch_options/firmware"></div>
                    <b>firmware</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/launch_options/firmware" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>BIOS</li>
                                                                                                                                                                                                <li>UEFI_64</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Firmware used to boot VM. Select the option that matches your operating system. * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating systems that boot using MBR style bootloaders. * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the default for platform images.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/launch_options/is_consistent_volume_naming_enabled"></div>
                    <b>is_consistent_volume_naming_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/launch_options/is_consistent_volume_naming_enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to enable consistent volume naming feature. Defaults to false.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/launch_options/is_pv_encryption_in_transit_enabled"></div>
                    <b>is_pv_encryption_in_transit_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/launch_options/is_pv_encryption_in_transit_enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Deprecated. Instead use `isPvEncryptionInTransitEnabled` in <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/datatypes/InstanceConfigurationLaunchInstanceDetails'>InstanceConfigurationLaunchInstanceDetails</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/launch_options/network_type"></div>
                    <b>network_type</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/launch_options/network_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>E1000</li>
                                                                                                                                                                                                <li>VFIO</li>
                                                                                                                                                                                                <li>PARAVIRTUALIZED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Emulation type for the physical network interface card (NIC). * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver. * `VFIO` - Direct attached Virtual Function network controller. This is the networking type when you launch an instance using hardware-assisted (SR-IOV) networking. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/launch_options/remote_data_volume_type"></div>
                    <b>remote_data_volume_type</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/launch_options/remote_data_volume_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ISCSI</li>
                                                                                                                                                                                                <li>SCSI</li>
                                                                                                                                                                                                <li>IDE</li>
                                                                                                                                                                                                <li>VFIO</li>
                                                                                                                                                                                                <li>PARAVIRTUALIZED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Emulation type for volume. * `ISCSI` - ISCSI attached block storage device. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data volumes on platform images. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on platform images.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/metadata"></div>
                    <b>metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance.</div>
                                            <div>A metadata service runs on every launched instance. The service is an HTTP endpoint listening on 169.254.169.254. You can use the service to:</div>
                                            <div>* Provide information to <a href='https://cloudinit.readthedocs.org/en/latest/'>Cloud-Init</a> to be used for various system initialization tasks.</div>
                                            <div>* Get information about the instance, including the custom metadata that you provide when you launch the instance.</div>
                                            <div>**Providing Cloud-Init Metadata**</div>
                                            <div>You can use the following metadata key names to provide information to Cloud-Init:</div>
                                            <div>**&quot;ssh_authorized_keys&quot;** - Provide one or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for the default user on the instance. Use a newline character to separate multiple keys. The SSH keys must be in the format necessary for the `authorized_keys` file, as shown in the example below.</div>
                                            <div>**&quot;user_data&quot;** - Provide your own base64-encoded data to be used by Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For information about how to take advantage of user data, see the <a href='http://cloudinit.readthedocs.org/en/latest/topics/format.html'>Cloud-Init Documentation</a>.</div>
                                            <div>**Metadata Example**</div>
                                            <div>&quot;metadata&quot; : { &quot;quake_bot_level&quot; : &quot;Severe&quot;, &quot;ssh_authorized_keys&quot; : &quot;ssh-rsa &lt;your_public_SSH_key&gt;== rsa-key-20160227&quot;, &quot;user_data&quot; : &quot;&lt;your_public_SSH_key&gt;==&quot; } **Getting Metadata on the Instance**</div>
                                            <div>To get information about your instance, connect to the instance using SSH and issue any of the following GET requests:</div>
                                            <div>curl -H &quot;Authorization: Bearer Oracle&quot; http://169.254.169.254/opc/v2/instance/ curl -H &quot;Authorization: Bearer Oracle&quot; http://169.254.169.254/opc/v2/instance/metadata/ curl -H &quot;Authorization: Bearer Oracle&quot; http://169.254.169.254/opc/v2/instance/metadata/&lt;any-key-name&gt;</div>
                                            <div>You&#x27;ll get back a response that includes all the instance information; only the metadata information; or the metadata information for the specified key name, respectively.</div>
                                            <div>The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/platform_config"></div>
                    <b>platform_config</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/platform_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/platform_config/is_measured_boot_enabled"></div>
                    <b>is_measured_boot_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/platform_config/is_measured_boot_enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether the Measured Boot feature is enabled on the instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/platform_config/is_secure_boot_enabled"></div>
                    <b>is_secure_boot_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/platform_config/is_secure_boot_enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether Secure Boot is enabled on the instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/platform_config/is_trusted_platform_module_enabled"></div>
                    <b>is_trusted_platform_module_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/platform_config/is_trusted_platform_module_enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether the Trusted Platform Module (TPM) is enabled on the instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/platform_config/numa_nodes_per_socket"></div>
                    <b>numa_nodes_per_socket</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/platform_config/numa_nodes_per_socket" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>NPS0</li>
                                                                                                                                                                                                <li>NPS1</li>
                                                                                                                                                                                                <li>NPS2</li>
                                                                                                                                                                                                <li>NPS4</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The number of NUMA nodes per socket.</div>
                                            <div>Applicable when type is &#x27;AMD_MILAN_BM&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/platform_config/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/platform_config/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>AMD_MILAN_BM</li>
                                                                                                                                                                                                <li>INTEL_VM</li>
                                                                                                                                                                                                <li>AMD_ROME_BM</li>
                                                                                                                                                                                                <li>INTEL_SKYLAKE_BM</li>
                                                                                                                                                                                                <li>AMD_VM</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of platform being configured.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/preemptible_instance_config"></div>
                    <b>preemptible_instance_config</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/preemptible_instance_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/preemptible_instance_config/preemption_action"></div>
                    <b>preemption_action</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/preemptible_instance_config/preemption_action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/preemptible_instance_config/preemption_action/preserve_boot_volume"></div>
                    <b>preserve_boot_volume</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/preemptible_instance_config/preemption_action/preserve_boot_volume" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated. Defaults to false if not specified.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/preemptible_instance_config/preemption_action/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/preemptible_instance_config/preemption_action/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>TERMINATE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of action to run when the instance is interrupted for eviction.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/preferred_maintenance_action"></div>
                    <b>preferred_maintenance_action</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/preferred_maintenance_action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>LIVE_MIGRATE</li>
                                                                                                                                                                                                <li>REBOOT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The preferred maintenance action for an instance. The default is LIVE_MIGRATE, if live migration is supported. * `LIVE_MIGRATE` - Run maintenance using a live migration. * `REBOOT` - Run maintenance using a reboot.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/shape"></div>
                    <b>shape</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/shape" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.</div>
                                            <div>You can enumerate all available shapes by calling <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/Shape/ListShapes'>ListShapes</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/shape_config"></div>
                    <b>shape_config</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/shape_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/shape_config/baseline_ocpu_utilization"></div>
                    <b>baseline_ocpu_utilization</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/shape_config/baseline_ocpu_utilization" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>BASELINE_1_8</li>
                                                                                                                                                                                                <li>BASELINE_1_2</li>
                                                                                                                                                                                                <li>BASELINE_1_1</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.</div>
                                            <div>The following values are supported: - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU. - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU. - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/shape_config/memory_in_gbs"></div>
                    <b>memory_in_gbs</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/shape_config/memory_in_gbs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The total amount of memory available to the instance, in gigabytes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/shape_config/ocpus"></div>
                    <b>ocpus</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/shape_config/ocpus" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The total number of OCPUs available to the instance.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/source_details"></div>
                    <b>source_details</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/source_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/source_details/boot_volume_id"></div>
                    <b>boot_volume_id</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/source_details/boot_volume_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the boot volume used to boot the instance.</div>
                                            <div>Applicable when source_type is &#x27;bootVolume&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/source_details/boot_volume_size_in_gbs"></div>
                    <b>boot_volume_size_in_gbs</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/source_details/boot_volume_size_in_gbs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The size of the boot volume in GBs. The minimum value is 50 GB and the maximum value is 32,768 GB (32 TB).</div>
                                            <div>Applicable when source_type is &#x27;image&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/source_details/image_id"></div>
                    <b>image_id</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/source_details/image_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the image used to boot the instance.</div>
                                            <div>Applicable when source_type is &#x27;image&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_details/source_details/source_type"></div>
                    <b>source_type</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_details/source_details/source_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>image</li>
                                                                                                                                                                                                <li>bootVolume</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The source type for the instance. Use `image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-region"></div>
                    <b>region</b>
                    <a class="ansibleOptionLink" href="#parameter-region" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics"></div>
                    <b>secondary_vnics</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable only for <em>action=launch</em>.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/create_vnic_details"></div>
                    <b>create_vnic_details</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/create_vnic_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/create_vnic_details/assign_private_dns_record"></div>
                    <b>assign_private_dns_record</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/create_vnic_details/assign_private_dns_record" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether the VNIC should be assigned a private DNS record. See the `assignPrivateDnsRecord` attribute of <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/'>CreateVnicDetails</a> for more information.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/create_vnic_details/assign_public_ip"></div>
                    <b>assign_public_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/create_vnic_details/assign_public_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/'>CreateVnicDetails</a> for more information.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/create_vnic_details/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/create_vnic_details/defined_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Operations&quot;: {&quot;CostCenter&quot;: &quot;42&quot;}}`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/create_vnic_details/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/create_vnic_details/display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/create_vnic_details/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/create_vnic_details/freeform_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/create_vnic_details/hostname_label"></div>
                    <b>hostname_label</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/create_vnic_details/hostname_label" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The hostname for the VNIC&#x27;s primary private IP. See the `hostnameLabel` attribute of <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/CreateVnicDetails/'>CreateVnicDetails</a> for more information.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/create_vnic_details/nsg_ids"></div>
                    <b>nsg_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/create_vnic_details/nsg_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more information about NSGs, see <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/'>NetworkSecurityGroup</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/create_vnic_details/private_ip"></div>
                    <b>private_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/create_vnic_details/private_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A private IP address of your choice to assign to the VNIC. See the `privateIp` attribute of <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/CreateVnicDetails/'>CreateVnicDetails</a> for more information.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/create_vnic_details/skip_source_dest_check"></div>
                    <b>skip_source_dest_check</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/create_vnic_details/skip_source_dest_check" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether the source/destination check is disabled on the VNIC. See the `skipSourceDestCheck` attribute of <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/CreateVnicDetails/'>CreateVnicDetails</a> for more information.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/create_vnic_details/subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/create_vnic_details/subnet_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the subnet to create the VNIC in. See the `subnetId` attribute of <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/CreateVnicDetails/'>CreateVnicDetails</a> for more information.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-secondary_vnics/nic_index"></div>
                    <b>nic_index</b>
                    <a class="ansibleOptionLink" href="#parameter-secondary_vnics/nic_index" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-tenancy"></div>
                    <b>tenancy</b>
                    <a class="ansibleOptionLink" href="#parameter-tenancy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Attributes


.. Notes

Notes
-----

.. note::
   - For OCI python sdk configuration, please refer to https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/configuration.html

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Perform action change_compartment on instance_configuration
      oci_compute_management_instance_configuration_actions:
        # required
        instance_configuration_id: "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        action: change_compartment

    - name: Perform action launch on instance_configuration with instance_type = compute
      oci_compute_management_instance_configuration_actions:
        # required
        instance_type: compute

        # optional
        block_volumes:
        - # optional
          attach_details:
            # required
            type: iscsi

            # optional
            display_name: display_name_example
            is_read_only: true
            device: device_example
            is_shareable: true
            use_chap: true
          create_details:
            # optional
            availability_domain: Uocm:PHX-AD-1
            backup_policy_id: "ocid1.backuppolicy.oc1..xxxxxxEXAMPLExxxxxx"
            compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
            defined_tags: {'Operations': {'CostCenter': 'US'}}
            display_name: display_name_example
            freeform_tags: {'Department': 'Finance'}
            kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
            vpus_per_gb: 56
            size_in_gbs: 56
            source_details:
              # required
              type: volumeBackup

              # optional
              id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
          volume_id: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
        launch_details:
          # optional
          availability_domain: Uocm:PHX-AD-1
          capacity_reservation_id: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
          compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
          create_vnic_details:
            # optional
            assign_public_ip: true
            assign_private_dns_record: true
            defined_tags: {'Operations': {'CostCenter': 'US'}}
            display_name: display_name_example
            freeform_tags: {'Department': 'Finance'}
            hostname_label: hostname_label_example
            nsg_ids: [ "nsg_ids_example" ]
            private_ip: private_ip_example
            skip_source_dest_check: true
            subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
          defined_tags: {'Operations': {'CostCenter': 'US'}}
          display_name: display_name_example
          extended_metadata: null
          freeform_tags: {'Department': 'Finance'}
          ipxe_script: ipxe_script_example
          metadata: null
          shape: shape_example
          shape_config:
            # optional
            ocpus: 3.4
            memory_in_gbs: 3.4
            baseline_ocpu_utilization: BASELINE_1_8
          platform_config:
            # required
            type: AMD_MILAN_BM

            # optional
            is_secure_boot_enabled: true
            is_trusted_platform_module_enabled: true
            is_measured_boot_enabled: true
            numa_nodes_per_socket: NPS0
          source_details:
            # required
            source_type: image

            # optional
            boot_volume_size_in_gbs: 56
            image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
          fault_domain: FAULT-DOMAIN-1
          dedicated_vm_host_id: "ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx"
          launch_mode: NATIVE
          launch_options:
            # optional
            boot_volume_type: ISCSI
            firmware: BIOS
            network_type: E1000
            remote_data_volume_type: ISCSI
            is_pv_encryption_in_transit_enabled: true
            is_consistent_volume_naming_enabled: true
          agent_config:
            # optional
            is_monitoring_disabled: true
            is_management_disabled: true
            are_all_plugins_disabled: true
            plugins_config:
            - # required
              name: name_example
              desired_state: ENABLED
          is_pv_encryption_in_transit_enabled: true
          preferred_maintenance_action: LIVE_MIGRATE
          instance_options:
            # optional
            are_legacy_imds_endpoints_disabled: true
          availability_config:
            # optional
            recovery_action: RESTORE_INSTANCE
          preemptible_instance_config:
            # required
            preemption_action:
              # required
              type: TERMINATE

              # optional
              preserve_boot_volume: true
        secondary_vnics:
        - # optional
          create_vnic_details:
            # optional
            assign_public_ip: true
            assign_private_dns_record: true
            defined_tags: {'Operations': {'CostCenter': 'US'}}
            display_name: display_name_example
            freeform_tags: {'Department': 'Finance'}
            hostname_label: hostname_label_example
            nsg_ids: [ "nsg_ids_example" ]
            private_ip: private_ip_example
            skip_source_dest_check: true
            subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
          display_name: display_name_example
          nic_index: 56





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-instance"></div>
                    <b>instance</b>
                    <a class="ansibleOptionLink" href="#return-instance" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the InstanceConfiguration resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;agent_config&#x27;: {&#x27;are_all_plugins_disabled&#x27;: True, &#x27;is_management_disabled&#x27;: True, &#x27;is_monitoring_disabled&#x27;: True, &#x27;plugins_config&#x27;: [{&#x27;desired_state&#x27;: &#x27;ENABLED&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;}]}, &#x27;availability_config&#x27;: {&#x27;is_live_migration_preferred&#x27;: True, &#x27;recovery_action&#x27;: &#x27;RESTORE_INSTANCE&#x27;}, &#x27;availability_domain&#x27;: &#x27;Uocm:PHX-AD-1&#x27;, &#x27;capacity_reservation_id&#x27;: &#x27;ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;dedicated_vm_host_id&#x27;: &#x27;ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;extended_metadata&#x27;: {}, &#x27;fault_domain&#x27;: &#x27;FAULT-DOMAIN-1&#x27;, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;image_id&#x27;: &#x27;ocid1.image.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;instance_options&#x27;: {&#x27;are_legacy_imds_endpoints_disabled&#x27;: True}, &#x27;ipxe_script&#x27;: &#x27;ipxe_script_example&#x27;, &#x27;launch_mode&#x27;: &#x27;NATIVE&#x27;, &#x27;launch_options&#x27;: {&#x27;boot_volume_type&#x27;: &#x27;ISCSI&#x27;, &#x27;firmware&#x27;: &#x27;BIOS&#x27;, &#x27;is_consistent_volume_naming_enabled&#x27;: True, &#x27;is_pv_encryption_in_transit_enabled&#x27;: True, &#x27;network_type&#x27;: &#x27;E1000&#x27;, &#x27;remote_data_volume_type&#x27;: &#x27;ISCSI&#x27;}, &#x27;lifecycle_state&#x27;: &#x27;MOVING&#x27;, &#x27;metadata&#x27;: {}, &#x27;platform_config&#x27;: {&#x27;is_measured_boot_enabled&#x27;: True, &#x27;is_secure_boot_enabled&#x27;: True, &#x27;is_trusted_platform_module_enabled&#x27;: True, &#x27;numa_nodes_per_socket&#x27;: &#x27;NPS0&#x27;, &#x27;type&#x27;: &#x27;AMD_MILAN_BM&#x27;}, &#x27;preemptible_instance_config&#x27;: {&#x27;preemption_action&#x27;: {&#x27;preserve_boot_volume&#x27;: True, &#x27;type&#x27;: &#x27;TERMINATE&#x27;}}, &#x27;region&#x27;: &#x27;us-phoenix-1&#x27;, &#x27;shape&#x27;: &#x27;shape_example&#x27;, &#x27;shape_config&#x27;: {&#x27;baseline_ocpu_utilization&#x27;: &#x27;BASELINE_1_8&#x27;, &#x27;gpu_description&#x27;: &#x27;gpu_description_example&#x27;, &#x27;gpus&#x27;: 56, &#x27;local_disk_description&#x27;: &#x27;local_disk_description_example&#x27;, &#x27;local_disks&#x27;: 56, &#x27;local_disks_total_size_in_gbs&#x27;: 3.4, &#x27;max_vnic_attachments&#x27;: 56, &#x27;memory_in_gbs&#x27;: 3.4, &#x27;networking_bandwidth_in_gbps&#x27;: 3.4, &#x27;ocpus&#x27;: 3.4, &#x27;processor_description&#x27;: &#x27;processor_description_example&#x27;}, &#x27;source_details&#x27;: {&#x27;boot_volume_id&#x27;: &#x27;ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;boot_volume_size_in_gbs&#x27;: 56, &#x27;image_id&#x27;: &#x27;ocid1.image.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;kms_key_id&#x27;: &#x27;ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;source_type&#x27;: &#x27;bootVolume&#x27;}, &#x27;system_tags&#x27;: {}, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_maintenance_reboot_due&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/agent_config"></div>
                    <b>agent_config</b>
                    <a class="ansibleOptionLink" href="#return-instance/agent_config" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/agent_config/are_all_plugins_disabled"></div>
                    <b>are_all_plugins_disabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/agent_config/are_all_plugins_disabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether Oracle Cloud Agent can run all of the available plugins. This includes the management and monitoring plugins.</div>
                                            <div>For more information about the available plugins, see <a href='https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm'>Managing Plugins with Oracle Cloud Agent</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/agent_config/is_management_disabled"></div>
                    <b>is_management_disabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/agent_config/is_management_disabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether Oracle Cloud Agent can run all the available management plugins.</div>
                                            <div>These are the management plugins: OS Management Service Agent and Compute Instance Run Command.</div>
                                            <div>The management plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object.</div>
                                            <div>- If `isManagementDisabled` is true, all of the management plugins are disabled, regardless of the per-plugin configuration. - If `isManagementDisabled` is false, all of the management plugins are enabled. You can optionally disable individual management plugins by providing a value in the `pluginsConfig` object.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/agent_config/is_monitoring_disabled"></div>
                    <b>is_monitoring_disabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/agent_config/is_monitoring_disabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether Oracle Cloud Agent can gather performance metrics and monitor the instance using the monitoring plugins.</div>
                                            <div>These are the monitoring plugins: Compute Instance Monitoring and Custom Logs Monitoring.</div>
                                            <div>The monitoring plugins are controlled by this parameter and by the per-plugin configuration in the `pluginsConfig` object.</div>
                                            <div>- If `isMonitoringDisabled` is true, all of the monitoring plugins are disabled, regardless of the per-plugin configuration. - If `isMonitoringDisabled` is false, all of the monitoring plugins are enabled. You can optionally disable individual monitoring plugins by providing a value in the `pluginsConfig` object.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/agent_config/plugins_config"></div>
                    <b>plugins_config</b>
                    <a class="ansibleOptionLink" href="#return-instance/agent_config/plugins_config" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The configuration of plugins associated with this instance.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/agent_config/plugins_config/desired_state"></div>
                    <b>desired_state</b>
                    <a class="ansibleOptionLink" href="#return-instance/agent_config/plugins_config/desired_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the plugin should be enabled or disabled.</div>
                                            <div>To enable the monitoring and management plugins, the `isMonitoringDisabled` and `isManagementDisabled` attributes must also be set to false.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ENABLED</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/agent_config/plugins_config/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-instance/agent_config/plugins_config/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The plugin name. To get a list of available plugins, use the <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/instanceagent/20180530/Plugin/ListInstanceagentAvailablePlugins'>ListInstanceagentAvailablePlugins</a> operation in the Oracle Cloud Agent API. For more information about the available plugins, see <a href='https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm'>Managing Plugins with Oracle Cloud Agent</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/availability_config"></div>
                    <b>availability_config</b>
                    <a class="ansibleOptionLink" href="#return-instance/availability_config" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/availability_config/is_live_migration_preferred"></div>
                    <b>is_live_migration_preferred</b>
                    <a class="ansibleOptionLink" href="#return-instance/availability_config/is_live_migration_preferred" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether to live migrate supported VM instances to a healthy physical VM host without disrupting running instances during infrastructure maintenance events. If null, Oracle chooses the best option for migrating the VM during infrastructure maintenance events.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/availability_config/recovery_action"></div>
                    <b>recovery_action</b>
                    <a class="ansibleOptionLink" href="#return-instance/availability_config/recovery_action" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The lifecycle state for an instance when it is recovered after infrastructure maintenance. * `RESTORE_INSTANCE` - The instance is restored to the lifecycle state it was in before the maintenance event. If the instance was running, it is automatically rebooted. This is the default action when a value is not set. * `STOP_INSTANCE` - The instance is recovered in the stopped state.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">RESTORE_INSTANCE</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/availability_domain"></div>
                    <b>availability_domain</b>
                    <a class="ansibleOptionLink" href="#return-instance/availability_domain" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The availability domain the instance is running in.</div>
                                            <div>Example: `Uocm:PHX-AD-1`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Uocm:PHX-AD-1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/capacity_reservation_id"></div>
                    <b>capacity_reservation_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/capacity_reservation_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the compute capacity reservation this instance is launched under. When this field contains an empty string or is null, the instance is not currently in a capacity reservation. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default'>Capacity Reservations</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the compartment that contains the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/dedicated_vm_host_id"></div>
                    <b>dedicated_vm_host_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/dedicated_vm_host_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of dedicated VM host.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-instance/defined_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Operations&quot;: {&quot;CostCenter&quot;: &quot;42&quot;}}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-instance/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/extended_metadata"></div>
                    <b>extended_metadata</b>
                    <a class="ansibleOptionLink" href="#return-instance/extended_metadata" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object.</div>
                                            <div>They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only).</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/fault_domain"></div>
                    <b>fault_domain</b>
                    <a class="ansibleOptionLink" href="#return-instance/fault_domain" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the fault domain the instance is running in.</div>
                                            <div>A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains.</div>
                                            <div>If you do not specify the fault domain, the system selects one for you.</div>
                                            <div>Example: `FAULT-DOMAIN-1`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">FAULT-DOMAIN-1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-instance/freeform_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Department&#x27;: &#x27;Finance&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-instance/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/image_id"></div>
                    <b>image_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/image_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Deprecated. Use `sourceDetails` instead.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.image.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/instance_options"></div>
                    <b>instance_options</b>
                    <a class="ansibleOptionLink" href="#return-instance/instance_options" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/instance_options/are_legacy_imds_endpoints_disabled"></div>
                    <b>are_legacy_imds_endpoints_disabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/instance_options/are_legacy_imds_endpoints_disabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether to disable the legacy (/v1) instance metadata service endpoints. Customers who have migrated to /v2 should set this to true for added security. Default is false.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/ipxe_script"></div>
                    <b>ipxe_script</b>
                    <a class="ansibleOptionLink" href="#return-instance/ipxe_script" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process.</div>
                                            <div>If you want more control over the boot process, you can provide your own custom iPXE script that will run when the instance boots. Be aware that the same iPXE script will run every time an instance boots, not only after the initial LaunchInstance call.</div>
                                            <div>The default iPXE script connects to the instance&#x27;s local boot volume over iSCSI and performs a network boot. If you use a custom iPXE script and want to network-boot from the instance&#x27;s local boot volume over iSCSI the same way as the default iPXE script, use the following iSCSI IP address: 169.254.0.2, and boot volume IQN: iqn.2015-02.oracle.boot.</div>
                                            <div>If your instance boot volume type is paravirtualized, the boot volume is attached to the instance through virtio-scsi and no iPXE script is used. If your instance boot volume type is paravirtualized and you use custom iPXE to network boot into your instance, the primary boot volume is attached as a data volume through virtio-scsi drive.</div>
                                            <div>For more information about the Bring Your Own Image feature of Oracle Cloud Infrastructure, see <a href='https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm'>Bring Your Own Image</a>.</div>
                                            <div>For more information about iPXE, see http://ipxe.org.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ipxe_script_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_mode"></div>
                    <b>launch_mode</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_mode" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are: * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images. * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers. * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NATIVE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options"></div>
                    <b>launch_options</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options/boot_volume_type"></div>
                    <b>boot_volume_type</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options/boot_volume_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Emulation type for the boot volume. * `ISCSI` - ISCSI attached block storage device. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data volumes on platform images. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on platform images.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ISCSI</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options/firmware"></div>
                    <b>firmware</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options/firmware" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Firmware used to boot VM. Select the option that matches your operating system. * `BIOS` - Boot VM using BIOS style firmware. This is compatible with both 32 bit and 64 bit operating systems that boot using MBR style bootloaders. * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems. This is the default for platform images.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">BIOS</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options/is_consistent_volume_naming_enabled"></div>
                    <b>is_consistent_volume_naming_enabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options/is_consistent_volume_naming_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether to enable consistent volume naming feature. Defaults to false.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options/is_pv_encryption_in_transit_enabled"></div>
                    <b>is_pv_encryption_in_transit_enabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options/is_pv_encryption_in_transit_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Deprecated. Instead use `isPvEncryptionInTransitEnabled` in <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/datatypes/LaunchInstanceDetails'>LaunchInstanceDetails</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options/network_type"></div>
                    <b>network_type</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options/network_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Emulation type for the physical network interface card (NIC). * `E1000` - Emulated Gigabit ethernet controller. Compatible with Linux e1000 network driver. * `VFIO` - Direct attached Virtual Function network controller. This is the networking type when you launch an instance using hardware-assisted (SR-IOV) networking. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">E1000</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options/remote_data_volume_type"></div>
                    <b>remote_data_volume_type</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options/remote_data_volume_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Emulation type for volume. * `ISCSI` - ISCSI attached block storage device. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage. This is the default option for local data volumes on platform images. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on platform images.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ISCSI</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-instance/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">MOVING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/metadata"></div>
                    <b>metadata</b>
                    <a class="ansibleOptionLink" href="#return-instance/metadata" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Custom metadata that you provide.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/platform_config"></div>
                    <b>platform_config</b>
                    <a class="ansibleOptionLink" href="#return-instance/platform_config" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/platform_config/is_measured_boot_enabled"></div>
                    <b>is_measured_boot_enabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/platform_config/is_measured_boot_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the Measured Boot feature is enabled on the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/platform_config/is_secure_boot_enabled"></div>
                    <b>is_secure_boot_enabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/platform_config/is_secure_boot_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether Secure Boot is enabled on the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/platform_config/is_trusted_platform_module_enabled"></div>
                    <b>is_trusted_platform_module_enabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/platform_config/is_trusted_platform_module_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the Trusted Platform Module (TPM) is enabled on the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/platform_config/numa_nodes_per_socket"></div>
                    <b>numa_nodes_per_socket</b>
                    <a class="ansibleOptionLink" href="#return-instance/platform_config/numa_nodes_per_socket" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of NUMA nodes per socket (NPS).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NPS0</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/platform_config/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-instance/platform_config/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of platform being configured.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">AMD_MILAN_BM</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/preemptible_instance_config"></div>
                    <b>preemptible_instance_config</b>
                    <a class="ansibleOptionLink" href="#return-instance/preemptible_instance_config" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/preemptible_instance_config/preemption_action"></div>
                    <b>preemption_action</b>
                    <a class="ansibleOptionLink" href="#return-instance/preemptible_instance_config/preemption_action" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/preemptible_instance_config/preemption_action/preserve_boot_volume"></div>
                    <b>preserve_boot_volume</b>
                    <a class="ansibleOptionLink" href="#return-instance/preemptible_instance_config/preemption_action/preserve_boot_volume" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is terminated. Defaults to false if not specified.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/preemptible_instance_config/preemption_action/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-instance/preemptible_instance_config/preemption_action/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of action to run when the instance is interrupted for eviction.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">TERMINATE</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/region"></div>
                    <b>region</b>
                    <a class="ansibleOptionLink" href="#return-instance/region" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The region that contains the availability domain the instance is running in.</div>
                                            <div>For the us-phoenix-1 and us-ashburn-1 regions, `phx` and `iad` are returned, respectively. For all other regions, the full region name is returned.</div>
                                            <div>Examples: `phx`, `eu-frankfurt-1`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">us-phoenix-1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/shape"></div>
                    <b>shape</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance. You can enumerate all available shapes by calling <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Shape/ListShapes'>ListShapes</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">shape_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config"></div>
                    <b>shape_config</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/baseline_ocpu_utilization"></div>
                    <b>baseline_ocpu_utilization</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/baseline_ocpu_utilization" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.</div>
                                            <div>The following values are supported: - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU. - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU. - `BASELINE_1_1` - baseline usage is the entire OCPU. This represents a non-burstable instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">BASELINE_1_8</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/gpu_description"></div>
                    <b>gpu_description</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/gpu_description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A short description of the instance&#x27;s graphics processing unit (GPU).</div>
                                            <div>If the instance does not have any GPUs, this field is `null`.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">gpu_description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/gpus"></div>
                    <b>gpus</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/gpus" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of GPUs available to the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/local_disk_description"></div>
                    <b>local_disk_description</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/local_disk_description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A short description of the local disks available to this instance.</div>
                                            <div>If the instance does not have any local disks, this field is `null`.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">local_disk_description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/local_disks"></div>
                    <b>local_disks</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/local_disks" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of local disks available to the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/local_disks_total_size_in_gbs"></div>
                    <b>local_disks_total_size_in_gbs</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/local_disks_total_size_in_gbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The aggregate size of all local disks, in gigabytes.</div>
                                            <div>If the instance does not have any local disks, this field is `null`.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/max_vnic_attachments"></div>
                    <b>max_vnic_attachments</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/max_vnic_attachments" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum number of VNIC attachments for the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/memory_in_gbs"></div>
                    <b>memory_in_gbs</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/memory_in_gbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The total amount of memory available to the instance, in gigabytes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/networking_bandwidth_in_gbps"></div>
                    <b>networking_bandwidth_in_gbps</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/networking_bandwidth_in_gbps" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The networking bandwidth available to the instance, in gigabits per second.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/ocpus"></div>
                    <b>ocpus</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/ocpus" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The total number of OCPUs available to the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/processor_description"></div>
                    <b>processor_description</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/processor_description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A short description of the instance&#x27;s processor (CPU).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">processor_description_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/source_details"></div>
                    <b>source_details</b>
                    <a class="ansibleOptionLink" href="#return-instance/source_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/source_details/boot_volume_id"></div>
                    <b>boot_volume_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/source_details/boot_volume_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the boot volume used to boot the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/source_details/boot_volume_size_in_gbs"></div>
                    <b>boot_volume_size_in_gbs</b>
                    <a class="ansibleOptionLink" href="#return-instance/source_details/boot_volume_size_in_gbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 32,768 GB (32 TB).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/source_details/image_id"></div>
                    <b>image_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/source_details/image_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the image used to boot the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.image.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/source_details/kms_key_id"></div>
                    <b>kms_key_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/source_details/kms_key_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the Key Management key to assign as the master encryption key for the boot volume.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/source_details/source_type"></div>
                    <b>source_type</b>
                    <a class="ansibleOptionLink" href="#return-instance/source_details/source_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The source type for the instance. Use `image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">bootVolume</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#return-instance/system_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-instance/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the instance was created, in the format defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>.</div>
                                            <div>Example: `2016-08-25T21:10:29.600Z`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-instance/time_maintenance_reboot_due"></div>
                    <b>time_maintenance_reboot_due</b>
                    <a class="ansibleOptionLink" href="#return-instance/time_maintenance_reboot_due" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the instance is expected to be stopped / started,  in the format defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>. After that time if instance hasn&#x27;t been rebooted, Oracle will reboot the instance within 24 hours of the due time. Regardless of how the instance was stopped, the flag will be reset to empty as soon as instance reaches Stopped state. Example: `2018-05-25T21:10:29.600Z`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                    
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Oracle (@oracle)



.. Parsing errors

