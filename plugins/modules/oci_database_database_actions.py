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
module: oci_database_database_actions
short_description: Perform actions on a Database resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Database resource in Oracle Cloud Infrastructure
    - Disables the Database Management service for the database.
    - Enables the Database Management service for an Oracle Database located in Oracle Cloud Infrastructure. This service allows the database to access tools
      including Metrics and Performance hub. Database Management is enabled at the container database (CDB) level.
    - Changes encryption key management from customer-managed, using the L(Vault
      service,https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm), to Oracle-managed.
    - Updates one or more attributes of the Database Management service for the database.
    - Restore a Database based on the request parameters you provide.
    - Creates a new version of an existing L(Vault service,https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm) key.
    - Upgrades the specified Oracle Database instance.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    credential_details:
        description:
            - ""
            - Required for I(action=enable_database_management).
        type: dict
        suboptions:
            user_name:
                description:
                    - The name of the Oracle Database user that will be used to connect to the database.
                type: str
                required: true
            password_secret_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                      L(secret,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
                type: str
                required: true
    private_end_point_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the private endpoint.
            - Required for I(action=enable_database_management).
        type: str
    management_type:
        description:
            - The Database Management type.
            - Applicable only for I(action=enable_database_management)I(action=modify_database_management).
        type: str
        choices:
            - "BASIC"
            - "ADVANCED"
    service_name:
        description:
            - The name of the Oracle Database service that will be used to connect to the database.
            - Required for I(action=enable_database_management).
        type: str
    kms_key_id:
        description:
            - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
            - Required for I(action=migrate_vault_key).
        type: str
    kms_key_version_id:
        description:
            - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key
              versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
            - Applicable only for I(action=migrate_vault_key).
        type: str
    database_scn:
        description:
            - Restores using the backup with the System Change Number (SCN) specified.
            - Applicable only for I(action=restore).
        type: str
    timestamp:
        description:
            - Restores to the timestamp specified.
            - Applicable only for I(action=restore).
        type: str
    latest:
        description:
            - Restores to the last known good state with the least possible data loss.
            - Applicable only for I(action=restore).
        type: bool
    action:
        description:
            - The action to perform on the Database.
        type: str
        required: true
        choices:
            - "disable_database_management"
            - "enable_database_management"
            - "migrate_vault_key"
            - "modify_database_management"
            - "restore"
            - "rotate_vault_key"
            - "precheck"
            - "upgrade"
            - "rollback"
    database_upgrade_source_details:
        description:
            - ""
            - Applicable only for I(action=upgrade).
        type: dict
        suboptions:
            source:
                description:
                    - "The source of the Oracle Database software to be used for the upgrade.
                       - Use `DB_HOME` to specify an existing Database Home to upgrade the database. The database is moved to the target Database Home and makes
                         use of the Oracle Database software version of the target Database Home.
                       - Use `DB_VERSION` to specify a generally-available Oracle Database software version to upgrade the database.
                       - Use `DB_SOFTWARE_IMAGE` to specify a L(database software
                         image,https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/databasesoftwareimage.htm) to upgrade the database."
                type: str
                choices:
                    - "DB_HOME"
                    - "DB_SOFTWARE_IMAGE"
                    - "DB_VERSION"
                required: true
            options:
                description:
                    - "Additional upgrade options supported by DBUA(Database Upgrade Assistant).
                      Example: \\"-upgradeTimezone false -keepEvents\\""
                type: str
            db_home_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home.
                    - Required when source is 'DB_HOME'
                type: str
            database_software_image_id:
                description:
                    - The database software image L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the image to be used to
                      upgrade a database.
                    - Required when source is 'DB_SOFTWARE_IMAGE'
                type: str
            db_version:
                description:
                    - A valid Oracle Database version. To get a list of supported versions, use the L(ListDbVersions,https://docs.cloud.oracle.com/en-
                      us/iaas/api/#/en/database/latest/DbVersionSummary/ListDbVersions) operation.
                    - Required when source is 'DB_VERSION'
                type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action disable_database_management on database
  oci_database_database_actions:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    action: disable_database_management

- name: Perform action enable_database_management on database
  oci_database_database_actions:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    credential_details:
      # required
      user_name: user_name_example
      password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
    private_end_point_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    service_name: service_name_example
    action: enable_database_management

    # optional
    management_type: BASIC

- name: Perform action migrate_vault_key on database
  oci_database_database_actions:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    action: migrate_vault_key

    # optional
    kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action modify_database_management on database
  oci_database_database_actions:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    action: modify_database_management

    # optional
    credential_details:
      # required
      user_name: user_name_example
      password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
    private_end_point_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    management_type: BASIC
    service_name: service_name_example

- name: Perform action restore on database
  oci_database_database_actions:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    action: restore

    # optional
    database_scn: database_scn_example
    timestamp: timestamp_example
    latest: true

- name: Perform action rotate_vault_key on database
  oci_database_database_actions:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    action: rotate_vault_key

- name: Perform action precheck on database
  oci_database_database_actions:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    action: PRECHECK

    # optional
    database_upgrade_source_details:
      # required
      source: DB_HOME
      db_home_id: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      options: options_example

- name: Perform action upgrade on database
  oci_database_database_actions:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    action: PRECHECK

    # optional
    database_upgrade_source_details:
      # required
      source: DB_HOME
      db_home_id: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      options: options_example

- name: Perform action rollback on database
  oci_database_database_actions:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    action: PRECHECK

    # optional
    database_upgrade_source_details:
      # required
      source: DB_HOME
      db_home_id: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      options: options_example

"""

RETURN = """
database:
    description:
        - Details of the Database resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        character_set:
            description:
                - The character set for the database.
            returned: on success
            type: str
            sample: character_set_example
        ncharacter_set:
            description:
                - The national character set for the database.
            returned: on success
            type: str
            sample: ncharacter_set_example
        db_home_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home.
            returned: on success
            type: str
            sample: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"
        db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        vm_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster.
            returned: on success
            type: str
            sample: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
        db_name:
            description:
                - The database name.
            returned: on success
            type: str
            sample: db_name_example
        pdb_name:
            description:
                - The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric
                  characters. Special characters are not permitted. Pluggable database should not be same as database name.
            returned: on success
            type: str
            sample: pdb_name_example
        db_workload:
            description:
                - The database workload type.
            returned: on success
            type: str
            sample: db_workload_example
        db_unique_name:
            description:
                - A system-generated name for the database to ensure uniqueness within an Oracle Data Guard group (a primary database and its standby
                  databases). The unique name cannot be changed.
            returned: on success
            type: str
            sample: db_unique_name_example
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the database.
            returned: on success
            type: str
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the database was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        last_backup_timestamp:
            description:
                - The date and time when the latest database backup was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        db_backup_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                auto_backup_enabled:
                    description:
                        - If set to true, configures automatic backups. If you previously used RMAN or dbcli to configure backups and then you switch to using
                          the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can
                          no longer rely on your previously configured unmanaged backups to work.
                    returned: on success
                    type: bool
                    sample: true
                recovery_window_in_days:
                    description:
                        - Number of days between the current and the earliest point of recoverability covered by automatic backups.
                          This value applies to automatic backups only. After a new automatic backup has been created, Oracle removes old automatic backups that
                          are created before the window.
                          When the value is updated, it is applied to all existing automatic backups.
                    returned: on success
                    type: int
                    sample: 56
                auto_backup_window:
                    description:
                        - Time window selected for initiating automatic backup for the database system. There are twelve available two-hour time windows. If no
                          option is selected, a start time between 12:00 AM to 7:00 AM in the region of the database is automatically chosen. For example, if
                          the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM (inclusive) to 4:00 AM
                          (exclusive).
                        - "Example: `SLOT_TWO`"
                    returned: on success
                    type: str
                    sample: SLOT_ONE
                backup_destination_details:
                    description:
                        - Backup destination details.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of the database backup destination.
                            returned: on success
                            type: str
                            sample: NFS
                        id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        vpc_user:
                            description:
                                - For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery
                                  Appliance.
                            returned: on success
                            type: str
                            sample: vpc_user_example
                        vpc_password:
                            description:
                                - For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.
                            returned: on success
                            type: str
                            sample: example-password
                        internet_proxy:
                            description:
                                - Proxy URL to connect to object store.
                            returned: on success
                            type: str
                            sample: internet_proxy_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        connection_strings:
            description:
                - The Connection strings used to connect to the Oracle Database.
            returned: on success
            type: complex
            contains:
                cdb_default:
                    description:
                        - Host name based CDB Connection String.
                    returned: on success
                    type: str
                    sample: cdb_default_example
                cdb_ip_default:
                    description:
                        - IP based CDB Connection String.
                    returned: on success
                    type: str
                    sample: cdb_ip_default_example
                all_connection_strings:
                    description:
                        - All connection strings to use to connect to the Database.
                    returned: on success
                    type: dict
                    sample: {}
        kms_key_id:
            description:
                - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        source_database_point_in_time_recovery_timestamp:
            description:
                - Point in time recovery timeStamp of the source database at which cloned database system is cloned from the source database system, as
                  described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339)
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        database_software_image_id:
            description:
                - The database software image L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
            returned: on success
            type: str
            sample: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
        is_cdb:
            description:
                - True if the database is a container database.
            returned: on success
            type: bool
            sample: true
        database_management_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                management_status:
                    description:
                        - The status of the Database Management service.
                    returned: on success
                    type: str
                    sample: ENABLING
                management_type:
                    description:
                        - The Database Management type.
                    returned: on success
                    type: str
                    sample: BASIC
        sid_prefix:
            description:
                - Specifies a prefix for the `Oracle SID` of the database to be created.
            returned: on success
            type: str
            sample: sid_prefix_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "character_set": "character_set_example",
        "ncharacter_set": "ncharacter_set_example",
        "db_home_id": "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx",
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "vm_cluster_id": "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "db_name": "db_name_example",
        "pdb_name": "pdb_name_example",
        "db_workload": "db_workload_example",
        "db_unique_name": "db_unique_name_example",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "PROVISIONING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "last_backup_timestamp": "2013-10-20T19:20:30+01:00",
        "db_backup_config": {
            "auto_backup_enabled": true,
            "recovery_window_in_days": 56,
            "auto_backup_window": "SLOT_ONE",
            "backup_destination_details": [{
                "type": "NFS",
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "vpc_user": "vpc_user_example",
                "vpc_password": "example-password",
                "internet_proxy": "internet_proxy_example"
            }]
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "connection_strings": {
            "cdb_default": "cdb_default_example",
            "cdb_ip_default": "cdb_ip_default_example",
            "all_connection_strings": {}
        },
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "source_database_point_in_time_recovery_timestamp": "2013-10-20T19:20:30+01:00",
        "database_software_image_id": "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cdb": true,
        "database_management_config": {
            "management_status": "ENABLING",
            "management_type": "BASIC"
        },
        "sid_prefix": "sid_prefix_example"
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
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import EnableDatabaseManagementDetails
    from oci.database.models import MigrateVaultKeyDetails
    from oci.database.models import ModifyDatabaseManagementDetails
    from oci.database.models import RestoreDatabaseDetails
    from oci.database.models import UpgradeDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        disable_database_management
        enable_database_management
        migrate_vault_key
        modify_database_management
        restore
        rotate_vault_key
        upgrade
    """

    def __init__(self, *args, **kwargs):
        super(DatabaseActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "database_id"

    def get_module_resource_id(self):
        return self.module.params.get("database_id")

    def get_get_fn(self):
        return self.client.get_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database, database_id=self.module.params.get("database_id"),
        )

    def disable_database_management(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_database_management,
            call_fn_args=(),
            call_fn_kwargs=dict(database_id=self.module.params.get("database_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def enable_database_management(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableDatabaseManagementDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_database_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                enable_database_management_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def migrate_vault_key(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, MigrateVaultKeyDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.migrate_vault_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                migrate_vault_key_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def modify_database_management(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ModifyDatabaseManagementDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.modify_database_management,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                modify_database_management_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def restore(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestoreDatabaseDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restore_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                restore_database_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def rotate_vault_key(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.rotate_vault_key,
            call_fn_args=(),
            call_fn_kwargs=dict(database_id=self.module.params.get("database_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def upgrade(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpgradeDatabaseDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.upgrade_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                upgrade_database_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatabaseActionsHelperCustom = get_custom_class("DatabaseActionsHelperCustom")


class ResourceHelper(DatabaseActionsHelperCustom, DatabaseActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            database_id=dict(aliases=["id"], type="str", required=True),
            credential_details=dict(
                type="dict",
                options=dict(
                    user_name=dict(type="str", required=True),
                    password_secret_id=dict(type="str", required=True),
                ),
            ),
            private_end_point_id=dict(type="str"),
            management_type=dict(type="str", choices=["BASIC", "ADVANCED"]),
            service_name=dict(type="str"),
            kms_key_id=dict(type="str"),
            kms_key_version_id=dict(type="str"),
            database_scn=dict(type="str"),
            timestamp=dict(type="str"),
            latest=dict(type="bool"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "disable_database_management",
                    "enable_database_management",
                    "migrate_vault_key",
                    "modify_database_management",
                    "restore",
                    "rotate_vault_key",
                    "precheck",
                    "upgrade",
                    "rollback",
                ],
            ),
            database_upgrade_source_details=dict(
                type="dict",
                options=dict(
                    source=dict(
                        type="str",
                        required=True,
                        choices=["DB_HOME", "DB_SOFTWARE_IMAGE", "DB_VERSION"],
                    ),
                    options=dict(type="str"),
                    db_home_id=dict(type="str"),
                    database_software_image_id=dict(type="str"),
                    db_version=dict(type="str"),
                ),
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
