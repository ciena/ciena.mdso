#!/usr/bin/env python
# Info module template

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by
#   https://github.com/jgroom33/vmware_rest_code_generator
#
# Do not edit this file manually.
#
# Changes should be made in the swagger used to
#   generate this file or in the generator
#
#############################################

from __future__ import absolute_import, division, print_function

__metaclass__ = type
import socket
import json

DOCUMENTATION = """
module: resources_by_resourceid_validate
short_description: Handle resource of type resources_by_resourceid_validate
description: Handle resource of type resources_by_resourceid_validate
options:
  autoClean:
    description:
    - Free up any resources automatically upon any activation failure
    - Used by I(state=['post'])
    type: bool
  createdAt:
    description:
    - Time of creation
    - Used by I(state=['post'])
    type: str
  custom:
    description:
    - Whether to perform custom validation in addition to built-in schema and accessor
      validations
    - Used by I(state=['post'])
    type: bool
  description:
    description:
    - Detailed description of this resource
    - Used by I(state=['post'])
    type: str
  desiredOrchState:
    description:
    - Desired orchestration state
    - Used by I(state=['post'])
    type: str
  differences:
    description:
    - Differences represent the difference between desired and observed state
    - Used by I(state=['post'])
    type: list
  discovered:
    description:
    - Is this resource discovered
    - Used by I(state=['post'])
    type: bool
  id:
    description:
    - Unique identifier for the resource (optional/ignored on calls to create)
    - Used by I(state=['post'])
    type: str
  label:
    description:
    - Textual label
    - Used by I(state=['post'])
    type: str
  method:
    choices:
    - DELETE
    - PATCH
    - PUT
    description:
    - The HTTP method for the resource to be validated against
    - Required with I(state=['post'])
    - Used by I(state=['post'])
    type: str
  nativeState:
    description:
    - Native (type specific) state
    - Used by I(state=['post'])
    type: str
  orchState:
    description:
    - Current state of the resource in the orchestrator
    - Used by I(state=['post'])
    type: str
  orderId:
    description:
    - If applicable, the order containing this resource
    - Used by I(state=['post'])
    type: str
  productId:
    description:
    - The type of product for this resource
    - Used by I(state=['post'])
    type: str
  properties:
    description:
    - Properties
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['post'])
    type: dict
  providerData:
    description:
    - Provider custom data
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['post'])
    type: dict
  providerResourceId:
    description:
    - Identifier of the resource in provider's context
    - Used by I(state=['post'])
    type: str
  reason:
    description:
    - Reason for the orchestration state
    - Used by I(state=['post'])
    type: str
  resourceId:
    description:
    - Identifier of the resource being validated against
    - Required with I(state=['post'])
    - Used by I(state=['post'])
    type: str
  resourceTypeId:
    description:
    - The type of this resource
    - Used by I(state=['post'])
    type: str
  revision:
    description:
    - Strictly increasing revision number, incremented every update including observed
      update
    - Used by I(state=['post'])
    type: int
  shared:
    description:
    - Is resource shared?
    - Used by I(state=['post'])
    type: bool
  sharingPermissionId:
    description:
    - The sharing permission associated with the resource
    - Used by I(state=['post'])
    type: str
  state:
    choices:
    - post
    description: []
    type: str
  subDomainId:
    description:
    - Identifier of the resource's sub-domain
    - Used by I(state=['post'])
    type: str
  tags:
    description:
    - Tags
    - Used by I(state=['post'])
    type: dict
  tenantId:
    description:
    - Owner tenant of the resource?
    - Used by I(state=['post'])
    type: str
  updateCount:
    description:
    - Monotonically increasing count of updates applied to this resource
    - Used by I(state=['post'])
    type: int
  updateReason:
    description:
    - Reason for the update state
    - Used by I(state=['post'])
    type: str
  updateState:
    description:
    - Current state of updating the resource, or `unset`
    - Used by I(state=['post'])
    type: str
  updatedAt:
    description:
    - Time of last update
    - Used by I(state=['post'])
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["custom", "method"]
from ansible.module_utils.basic import env_fallback

try:
    from ansible_module.turbo.module import AnsibleTurboModule as AnsibleModule
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ciena.mdso.plugins.module_utils.mdso import (
    gen_args,
    open_session,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "mdso_hostname": dict(
            type="str", required=False, fallback=(env_fallback, ["MDSO_HOST"])
        ),
        "mdso_username": dict(
            type="str", required=False, fallback=(env_fallback, ["MDSO_USER"])
        ),
        "mdso_password": dict(
            type="str",
            required=False,
            no_log=True,
            fallback=(env_fallback, ["MDSO_PASSWORD"]),
        ),
    }
    argument_spec["updatedAt"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["updateState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["updateReason"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["updateCount"] = {"type": "int", "operationIds": ["post"]}
    argument_spec["tenantId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["tags"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["subDomainId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["state"] = {"type": "str", "choices": ["post"]}
    argument_spec["sharingPermissionId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["shared"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["revision"] = {"type": "int", "operationIds": ["post"]}
    argument_spec["resourceTypeId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["resourceId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["reason"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["providerResourceId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["providerData"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["properties"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["productId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["orderId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["orchState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["nativeState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["method"] = {
        "type": "str",
        "choices": ["DELETE", "PATCH", "PUT"],
        "operationIds": ["post"],
    }
    argument_spec["label"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["discovered"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["differences"] = {"type": "list", "operationIds": ["post"]}
    argument_spec["desiredOrchState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["custom"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["createdAt"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["autoClean"] = {"type": "bool", "operationIds": ["post"]}
    return argument_spec


async def get_device_info(params, session, _url, _key):
    async with session.get(((_url + "/") + _key)) as resp:
        _json = await resp.json()
        entry = _json["value"]
        entry["_key"] = _key
        return entry


async def list_devices(params, session):
    existing_entries = []
    _url = url(params)
    async with session.get(_url) as resp:
        _json = await resp.json()
        devices = _json["value"]
    for device in devices:
        _id = list(device.values())[0]
        existing_entries.append((await get_device_info(params, session, _url, _id)))
    return existing_entries


async def main():
    module_args = prepare_argument_spec()
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    session = await open_session(
        mdso_hostname=module.params["mdso_hostname"],
        mdso_username=module.params["mdso_username"],
        mdso_password=module.params["mdso_password"],
    )
    result = await entry_point(module, session)
    module.exit_json(**result)


def url(params):
    return "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}/validate".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _post(params, session):
    accepted_fields = [
        "autoClean",
        "createdAt",
        "custom",
        "description",
        "desiredOrchState",
        "differences",
        "discovered",
        "id",
        "label",
        "method",
        "nativeState",
        "orchState",
        "orderId",
        "productId",
        "properties",
        "providerData",
        "providerResourceId",
        "reason",
        "resourceId",
        "resourceTypeId",
        "revision",
        "shared",
        "sharingPermissionId",
        "subDomainId",
        "tags",
        "tenantId",
        "updateCount",
        "updateReason",
        "updateState",
        "updatedAt",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}/validate".format(
        **params
    )
    async with session.post(_url, json=spec) as resp:
        content_types = [
            "application/json-patch+json",
            "application/vnd.api+json",
            "application/json",
        ]
        try:
            if resp.headers["Content-Type"] in content_types:
                _json = await resp.json()
            else:
                print("response Content-Type not supported")
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "post")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
