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

.. _ansible_collections.oracle.oci.oci_network_ip_sec_connection_tunnel_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_network_ip_sec_connection_tunnel -- Manage an IpSecConnectionTunnel resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 2.37.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_network_ip_sec_connection_tunnel`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to update an IpSecConnectionTunnel resource in Oracle Cloud Infrastructure


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
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-bgp_session_config"></div>
                    <b>bgp_session_config</b>
                    <a class="ansibleOptionLink" href="#parameter-bgp_session_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-bgp_session_config/customer_bgp_asn"></div>
                    <b>customer_bgp_asn</b>
                    <a class="ansibleOptionLink" href="#parameter-bgp_session_config/customer_bgp_asn" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The BGP ASN of the network on the CPE end of the BGP session. Can be a 2-byte or 4-byte ASN. Uses &quot;asplain&quot; format.</div>
                                            <div>If you are switching the tunnel from using BGP dynamic routing to static routing, the `customerBgpAsn` must be null.</div>
                                            <div>Example: `12345` (2-byte) or `1587232876` (4-byte)</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-bgp_session_config/customer_interface_ip"></div>
                    <b>customer_interface_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-bgp_session_config/customer_interface_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The IP address for the CPE end of the inside tunnel interface.</div>
                                            <div>If the tunnel&#x27;s `routing` attribute is set to `BGP` (see <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/datatypes/UpdateIPSecConnectionTunnelDetails'>UpdateIPSecConnectionTunnelDetails</a>), this IP address is used for the tunnel&#x27;s BGP session.</div>
                                            <div>If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel.</div>
                                            <div>The value must be a /30 or /31.</div>
                                            <div>If you are switching the tunnel from using BGP dynamic routing to static routing and want to remove the value for `customerInterfaceIp`, you can set the value to an empty string.</div>
                                            <div>Example: `10.0.0.5/31`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-bgp_session_config/customer_interface_ipv6"></div>
                    <b>customer_interface_ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-bgp_session_config/customer_interface_ipv6" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The IPv6 address for the CPE end of the inside tunnel interface. This IP address is optional.</div>
                                            <div>If the tunnel&#x27;s `routing` attribute is set to `BGP` (see <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/'>IPSecConnectionTunnel</a>), this IP address is used for the tunnel&#x27;s BGP session.</div>
                                            <div>If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel.</div>
                                            <div>Only subnet masks from /64 up to /127 are allowed.</div>
                                            <div>Example: `2001:db8::1/64`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-bgp_session_config/oracle_interface_ip"></div>
                    <b>oracle_interface_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-bgp_session_config/oracle_interface_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The IP address for the Oracle end of the inside tunnel interface.</div>
                                            <div>If the tunnel&#x27;s `routing` attribute is set to `BGP` (see <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/datatypes/UpdateIPSecConnectionTunnelDetails'>UpdateIPSecConnectionTunnelDetails</a>), this IP address is used for the tunnel&#x27;s BGP session.</div>
                                            <div>If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel.</div>
                                            <div>The value must be a /30 or /31.</div>
                                            <div>If you are switching the tunnel from using BGP dynamic routing to static routing and want to remove the value for `oracleInterfaceIp`, you can set the value to an empty string.</div>
                                            <div>Example: `10.0.0.4/31`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-bgp_session_config/oracle_interface_ipv6"></div>
                    <b>oracle_interface_ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-bgp_session_config/oracle_interface_ipv6" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The IPv6 address for the Oracle end of the inside tunnel interface. This IP address is optional.</div>
                                            <div>If the tunnel&#x27;s `routing` attribute is set to `BGP` (see <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/'>IPSecConnectionTunnel</a>), this IP address is used for the tunnel&#x27;s BGP session.</div>
                                            <div>If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel.</div>
                                            <div>Only subnet masks from /64 up to /127 are allowed.</div>
                                            <div>Example: `2001:db8::1/64`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                            <div>Required for update when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>This parameter is updatable when <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-dpd_config"></div>
                    <b>dpd_config</b>
                    <a class="ansibleOptionLink" href="#parameter-dpd_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-dpd_config/dpd_mode"></div>
                    <b>dpd_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-dpd_config/dpd_mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>INITIATE_AND_RESPOND</li>
                                                                                                                                                                                                <li>RESPOND_ONLY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>dpd mode</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-dpd_config/dpd_timeout_in_sec"></div>
                    <b>dpd_timeout_in_sec</b>
                    <a class="ansibleOptionLink" href="#parameter-dpd_config/dpd_timeout_in_sec" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>DPD Timeout in seconds.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-encryption_domain_config"></div>
                    <b>encryption_domain_config</b>
                    <a class="ansibleOptionLink" href="#parameter-encryption_domain_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-encryption_domain_config/cpe_traffic_selector"></div>
                    <b>cpe_traffic_selector</b>
                    <a class="ansibleOptionLink" href="#parameter-encryption_domain_config/cpe_traffic_selector" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Lists IPv4 or IPv6-enabled subnets in your on-premises network.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-encryption_domain_config/oracle_traffic_selector"></div>
                    <b>oracle_traffic_selector</b>
                    <a class="ansibleOptionLink" href="#parameter-encryption_domain_config/oracle_traffic_selector" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Lists IPv4 or IPv6-enabled subnets in your Oracle tenancy.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ike_version"></div>
                    <b>ike_version</b>
                    <a class="ansibleOptionLink" href="#parameter-ike_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>V1</li>
                                                                                                                                                                                                <li>V2</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Internet Key Exchange protocol version.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ipsc_id"></div>
                    <b>ipsc_id</b>
                    <a class="ansibleOptionLink" href="#parameter-ipsc_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the IPSec connection.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-nat_translation_enabled"></div>
                    <b>nat_translation_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-nat_translation_enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ENABLED</li>
                                                                                                                                                                                                <li>DISABLED</li>
                                                                                                                                                                                                <li>AUTO</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether NAT-T Enabled on the tunnel</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-oracle_initiation"></div>
                    <b>oracle_initiation</b>
                    <a class="ansibleOptionLink" href="#parameter-oracle_initiation" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>INITIATOR_OR_RESPONDER</li>
                                                                                                                                                                                                <li>RESPONDER_ONLY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether Oracle side is the initiator for negotiation.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-phase_one_config"></div>
                    <b>phase_one_config</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_one_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-phase_one_config/authentication_algorithm"></div>
                    <b>authentication_algorithm</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_one_config/authentication_algorithm" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SHA2_384</li>
                                                                                                                                                                                                <li>SHA2_256</li>
                                                                                                                                                                                                <li>SHA1_96</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Phase one authentication algorithm supported during tunnel negotiation.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-phase_one_config/diffie_helman_group"></div>
                    <b>diffie_helman_group</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_one_config/diffie_helman_group" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>GROUP2</li>
                                                                                                                                                                                                <li>GROUP5</li>
                                                                                                                                                                                                <li>GROUP14</li>
                                                                                                                                                                                                <li>GROUP19</li>
                                                                                                                                                                                                <li>GROUP20</li>
                                                                                                                                                                                                <li>GROUP24</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Phase One Diffie Hellman group supported during tunnel negotiation.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-phase_one_config/encryption_algorithm"></div>
                    <b>encryption_algorithm</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_one_config/encryption_algorithm" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>AES_256_CBC</li>
                                                                                                                                                                                                <li>AES_192_CBC</li>
                                                                                                                                                                                                <li>AES_128_CBC</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Phase one encryption algorithm supported during tunnel negotiation.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-phase_one_config/is_custom_phase_one_config"></div>
                    <b>is_custom_phase_one_config</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_one_config/is_custom_phase_one_config" title="Permalink to this option"></a>
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
                                            <div>Indicates whether custom phase one configuration is enabled.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-phase_one_config/lifetime_in_seconds"></div>
                    <b>lifetime_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_one_config/lifetime_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>IKE session key lifetime in seconds for IPSec phase one.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-phase_two_config"></div>
                    <b>phase_two_config</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_two_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-phase_two_config/authentication_algorithm"></div>
                    <b>authentication_algorithm</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_two_config/authentication_algorithm" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>HMAC_SHA2_256_128</li>
                                                                                                                                                                                                <li>HMAC_SHA1_128</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Phase two authentication algorithm supported during tunnel negotiation.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-phase_two_config/encryption_algorithm"></div>
                    <b>encryption_algorithm</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_two_config/encryption_algorithm" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>AES_256_GCM</li>
                                                                                                                                                                                                <li>AES_192_GCM</li>
                                                                                                                                                                                                <li>AES_128_GCM</li>
                                                                                                                                                                                                <li>AES_256_CBC</li>
                                                                                                                                                                                                <li>AES_192_CBC</li>
                                                                                                                                                                                                <li>AES_128_CBC</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Phase two encryption algorithm supported during tunnel negotiation.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-phase_two_config/is_custom_phase_two_config"></div>
                    <b>is_custom_phase_two_config</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_two_config/is_custom_phase_two_config" title="Permalink to this option"></a>
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
                                            <div>Indicates whether custom phase two configuration is enabled.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-phase_two_config/is_pfs_enabled"></div>
                    <b>is_pfs_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_two_config/is_pfs_enabled" title="Permalink to this option"></a>
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
                                            <div>Indicates whether perfect forward secrecy (PFS) is enabled.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-phase_two_config/lifetime_in_seconds"></div>
                    <b>lifetime_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_two_config/lifetime_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Lifetime in seconds for IPSec phase two.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-phase_two_config/pfs_dh_group"></div>
                    <b>pfs_dh_group</b>
                    <a class="ansibleOptionLink" href="#parameter-phase_two_config/pfs_dh_group" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>GROUP2</li>
                                                                                                                                                                                                <li>GROUP5</li>
                                                                                                                                                                                                <li>GROUP14</li>
                                                                                                                                                                                                <li>GROUP19</li>
                                                                                                                                                                                                <li>GROUP20</li>
                                                                                                                                                                                                <li>GROUP24</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Diffie-Hellman group used for PFS.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-routing"></div>
                    <b>routing</b>
                    <a class="ansibleOptionLink" href="#parameter-routing" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>BGP</li>
                                                                                                                                                                                                <li>STATIC</li>
                                                                                                                                                                                                <li>POLICY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of routing to use for this tunnel (either BGP dynamic routing or static routing).</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The state of the IpSecConnectionTunnel.</div>
                                            <div>Use <em>state=present</em> to update an existing an IpSecConnectionTunnel.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-tunnel_id"></div>
                    <b>tunnel_id</b>
                    <a class="ansibleOptionLink" href="#parameter-tunnel_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the tunnel.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-wait"></div>
                    <b>wait</b>
                    <a class="ansibleOptionLink" href="#parameter-wait" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to wait for create or delete operation to complete.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-wait_timeout"></div>
                    <b>wait_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-wait_timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Time, in seconds, to wait when <em>wait=yes</em>. Defaults to 1200 for most of the services but some services might have a longer wait timeout.</div>
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

    
    - name: Update ip_sec_connection_tunnel
      oci_network_ip_sec_connection_tunnel:
        # required
        ipsc_id: "ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx"
        tunnel_id: "ocid1.tunnel.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        display_name: display_name_example
        routing: BGP
        ike_version: V1
        bgp_session_config:
          # optional
          oracle_interface_ip: oracle_interface_ip_example
          customer_interface_ip: customer_interface_ip_example
          oracle_interface_ipv6: oracle_interface_ipv6_example
          customer_interface_ipv6: customer_interface_ipv6_example
          customer_bgp_asn: customer_bgp_asn_example
        encryption_domain_config:
          # optional
          oracle_traffic_selector: [ "oracle_traffic_selector_example" ]
          cpe_traffic_selector: [ "cpe_traffic_selector_example" ]

    - name: Update ip_sec_connection_tunnel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_network_ip_sec_connection_tunnel:
        # required
        ipsc_id: "ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example

        # optional
        routing: BGP
        ike_version: V1
        bgp_session_config:
          # optional
          oracle_interface_ip: oracle_interface_ip_example
          customer_interface_ip: customer_interface_ip_example
          oracle_interface_ipv6: oracle_interface_ipv6_example
          customer_interface_ipv6: customer_interface_ipv6_example
          customer_bgp_asn: customer_bgp_asn_example
        encryption_domain_config:
          # optional
          oracle_traffic_selector: [ "oracle_traffic_selector_example" ]
          cpe_traffic_selector: [ "cpe_traffic_selector_example" ]





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel"></div>
                    <b>ip_sec_connection_tunnel</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the IpSecConnectionTunnel resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;bgp_session_info&#x27;: {&#x27;bgp_ipv6_state&#x27;: &#x27;UP&#x27;, &#x27;bgp_state&#x27;: &#x27;UP&#x27;, &#x27;customer_bgp_asn&#x27;: &#x27;customer_bgp_asn_example&#x27;, &#x27;customer_interface_ip&#x27;: &#x27;customer_interface_ip_example&#x27;, &#x27;customer_interface_ipv6&#x27;: &#x27;customer_interface_ipv6_example&#x27;, &#x27;oracle_bgp_asn&#x27;: &#x27;oracle_bgp_asn_example&#x27;, &#x27;oracle_interface_ip&#x27;: &#x27;oracle_interface_ip_example&#x27;, &#x27;oracle_interface_ipv6&#x27;: &#x27;oracle_interface_ipv6_example&#x27;}, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;cpe_ip&#x27;: &#x27;cpe_ip_example&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;encryption_domain_config&#x27;: {&#x27;cpe_traffic_selector&#x27;: [], &#x27;oracle_traffic_selector&#x27;: []}, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;ike_version&#x27;: &#x27;V1&#x27;, &#x27;lifecycle_state&#x27;: &#x27;PROVISIONING&#x27;, &#x27;routing&#x27;: &#x27;BGP&#x27;, &#x27;status&#x27;: &#x27;UP&#x27;, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_status_updated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;vpn_ip&#x27;: &#x27;vpn_ip_example&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/bgp_session_info"></div>
                    <b>bgp_session_info</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/bgp_session_info" title="Permalink to this return value"></a>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/bgp_session_info/bgp_ipv6_state"></div>
                    <b>bgp_ipv6_state</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/bgp_session_info/bgp_ipv6_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The state of the BGP IPv6 session.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">UP</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/bgp_session_info/bgp_state"></div>
                    <b>bgp_state</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/bgp_session_info/bgp_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The state of the BGP session.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">UP</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/bgp_session_info/customer_bgp_asn"></div>
                    <b>customer_bgp_asn</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/bgp_session_info/customer_bgp_asn" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>If the tunnel&#x27;s `routing` attribute is set to `BGP` (see <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/'>IPSecConnectionTunnel</a>), this ASN is required and used for the tunnel&#x27;s BGP session. This is the ASN of the network on the CPE end of the BGP session. Can be a 2-byte or 4-byte ASN. Uses &quot;asplain&quot; format.</div>
                                            <div>If the tunnel uses static routing, the `customerBgpAsn` must be null.</div>
                                            <div>Example: `12345` (2-byte) or `1587232876` (4-byte)</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">customer_bgp_asn_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/bgp_session_info/customer_interface_ip"></div>
                    <b>customer_interface_ip</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/bgp_session_info/customer_interface_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The IP address for the CPE end of the inside tunnel interface.</div>
                                            <div>If the tunnel&#x27;s `routing` attribute is set to `BGP` (see <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/'>IPSecConnectionTunnel</a>), this IP address is required and used for the tunnel&#x27;s BGP session.</div>
                                            <div>If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP address so you can troubleshoot or monitor the tunnel.</div>
                                            <div>The value must be a /30 or /31.</div>
                                            <div>Example: `10.0.0.5/31`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">customer_interface_ip_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/bgp_session_info/customer_interface_ipv6"></div>
                    <b>customer_interface_ipv6</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/bgp_session_info/customer_interface_ipv6" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The IPv6 address for the CPE end of the inside tunnel interface. This IP address is optional.</div>
                                            <div>If the tunnel&#x27;s `routing` attribute is set to `BGP` (see <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/'>IPSecConnectionTunnel</a>), this IP address is used for the tunnel&#x27;s BGP session.</div>
                                            <div>If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel.</div>
                                            <div>Only subnet masks from /64 up to /127 are allowed.</div>
                                            <div>Example: `2001:db8::1/64`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">customer_interface_ipv6_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/bgp_session_info/oracle_bgp_asn"></div>
                    <b>oracle_bgp_asn</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/bgp_session_info/oracle_bgp_asn" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Oracle BGP ASN.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">oracle_bgp_asn_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/bgp_session_info/oracle_interface_ip"></div>
                    <b>oracle_interface_ip</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/bgp_session_info/oracle_interface_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The IP address for the Oracle end of the inside tunnel interface.</div>
                                            <div>If the tunnel&#x27;s `routing` attribute is set to `BGP` (see <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/'>IPSecConnectionTunnel</a>), this IP address is required and used for the tunnel&#x27;s BGP session.</div>
                                            <div>If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP address so you can troubleshoot or monitor the tunnel.</div>
                                            <div>The value must be a /30 or /31.</div>
                                            <div>Example: `10.0.0.4/31`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">oracle_interface_ip_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/bgp_session_info/oracle_interface_ipv6"></div>
                    <b>oracle_interface_ipv6</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/bgp_session_info/oracle_interface_ipv6" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The IPv6 address for the Oracle end of the inside tunnel interface. This IP address is optional.</div>
                                            <div>If the tunnel&#x27;s `routing` attribute is set to `BGP` (see <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/'>IPSecConnectionTunnel</a>), this IP address is used for the tunnel&#x27;s BGP session.</div>
                                            <div>If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or monitor the tunnel.</div>
                                            <div>Only subnet masks from /64 up to /127 are allowed.</div>
                                            <div>Example: `2001:db8::1/64`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">oracle_interface_ipv6_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment containing the tunnel.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/cpe_ip"></div>
                    <b>cpe_ip</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/cpe_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The IP address of the CPE&#x27;s VPN headend.</div>
                                            <div>Example: `203.0.113.22`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">cpe_ip_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/display_name" title="Permalink to this return value"></a>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/encryption_domain_config"></div>
                    <b>encryption_domain_config</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/encryption_domain_config" title="Permalink to this return value"></a>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/encryption_domain_config/cpe_traffic_selector"></div>
                    <b>cpe_traffic_selector</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/encryption_domain_config/cpe_traffic_selector" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Lists IPv4 or IPv6-enabled subnets in your on-premises network.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/encryption_domain_config/oracle_traffic_selector"></div>
                    <b>oracle_traffic_selector</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/encryption_domain_config/oracle_traffic_selector" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Lists IPv4 or IPv6-enabled subnets in your Oracle tenancy.</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the tunnel.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/ike_version"></div>
                    <b>ike_version</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/ike_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Internet Key Exchange protocol version.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">V1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The tunnel&#x27;s lifecycle state.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PROVISIONING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/routing"></div>
                    <b>routing</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/routing" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of routing used for this tunnel (either BGP dynamic routing or static routing).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">BGP</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/status" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The status of the tunnel based on IPSec protocol characteristics.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">UP</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the IPSec connection tunnel was created, in the format defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>.</div>
                                            <div>Example: `2016-08-25T21:10:29.600Z`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/time_status_updated"></div>
                    <b>time_status_updated</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/time_status_updated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>When the status of the tunnel last changed, in the format defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>.</div>
                                            <div>Example: `2016-08-25T21:10:29.600Z`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ip_sec_connection_tunnel/vpn_ip"></div>
                    <b>vpn_ip</b>
                    <a class="ansibleOptionLink" href="#return-ip_sec_connection_tunnel/vpn_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The IP address of Oracle&#x27;s VPN headend.</div>
                                            <div>Example: `203.0.113.21`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">vpn_ip_example</div>
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

