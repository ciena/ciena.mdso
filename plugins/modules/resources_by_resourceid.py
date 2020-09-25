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
module: resources_by_resourceid
short_description: Handle resource of type resources_by_resourceid
description: Handle resource of type resources_by_resourceid
options:
  autoClean:
    description:
    - Free up any resources automatically upon any activation failure
    type: bool
  createdAt:
    description:
    - Time of creation
    type: str
  description:
    description:
    - Detailed description of this resource
    type: str
  desiredOrchState:
    description:
    - Desired orchestration state
    type: str
  differences:
    description:
    - Differences represent the difference between desired and observed state
    type: list
  discovered:
    description:
    - Is this resource discovered
    type: bool
  full:
    description:
    - If true, returns volatile status attributes from the provider that are not stored
      in the database
    type: bool
  id:
    description:
    - Unique identifier for the resource (optional/ignored on calls to create)
    type: str
  label:
    description:
    - Textual label
    type: str
  minRevision:
    description:
    - Require the revision of the returned resource to be greater than or equal to
      minRevision. Respond with a 503 if the resource exists, but the revision does
      not meet the minRevision.
    type: int
  nativeState:
    description:
    - Native (type specific) state
    type: str
  obfuscate:
    description:
    - If true, schema obfuscated values will be replaced with a fixed string in the
      response.
    type: bool
  orchState:
    description:
    - Current state of the resource in the orchestrator
    type: str
  orderId:
    description:
    - If applicable, the order containing this resource
    type: str
  productId:
    description:
    - The type of product for this resource
    type: str
  properties:
    description:
    - Properties
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  providerData:
    description:
    - Provider custom data
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  providerResourceId:
    description:
    - Identifier of the resource in provider's context
    type: str
  reason:
    description:
    - Reason for the orchestration state
    type: str
  resourceId:
    description:
    - Identifier of the resource being queried
    type: str
  resourceTypeId:
    description:
    - The type of this resource
    type: str
  revision:
    description:
    - Strictly increasing revision number, incremented every update including observed
      update
    type: int
  shared:
    description:
    - Is resource shared?
    type: bool
  sharingPermissionId:
    description:
    - The sharing permission associated with the resource
    type: str
  state:
    choices:
    - delete
    - get
    - head
    - patch
    - put
    description: []
    type: str
  subDomainId:
    description:
    - Identifier of the resource's sub-domain
    type: str
  tags:
    description:
    - Tags
    type: dict
  tenantId:
    description:
    - Owner tenant of the resource?
    type: str
  updateCount:
    description:
    - Monotonically increasing count of updates applied to this resource
    type: int
  updateReason:
    description:
    - Reason for the update state
    type: str
  updateState:
    description:
    - Current state of updating the resource, or `unset`
    type: str
  updatedAt:
    description:
    - Time of last update
    type: str
  validate:
    description:
    - Whether to perform custom validation in addition to built-in schema and accessor
      validations
    type: bool
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["full", "minRevision", "obfuscate", "validate"]
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
    argument_spec["validate"] = {
        "type": "bool",
        "operationIds": ["delete", "patch", "put"],
    }
    argument_spec["updatedAt"] = {"type": "str", "operationIds": ["patch"]}
    argument_spec["updateState"] = {"type": "str", "operationIds": ["patch"]}
    argument_spec["updateReason"] = {"type": "str", "operationIds": ["patch"]}
    argument_spec["updateCount"] = {"type": "int", "operationIds": ["patch"]}
    argument_spec["tenantId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["tags"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["subDomainId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["sharingPermissionId"] = {
        "type": "str",
        "operationIds": ["patch", "put"],
    }
    argument_spec["shared"] = {"type": "bool", "operationIds": ["patch", "put"]}
    argument_spec["revision"] = {"type": "int", "operationIds": ["patch"]}
    argument_spec["resourceTypeId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["resourceId"] = {
        "type": "str",
        "operationIds": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["reason"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["providerResourceId"] = {
        "type": "str",
        "operationIds": ["patch", "put"],
    }
    argument_spec["providerData"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["properties"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["productId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["orderId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["orchState"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["obfuscate"] = {
        "type": "bool",
        "operationIds": ["get", "head", "patch", "put"],
    }
    argument_spec["nativeState"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["minRevision"] = {"type": "int", "operationIds": ["get", "head"]}
    argument_spec["label"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["full"] = {"type": "bool", "operationIds": ["get", "head"]}
    argument_spec["discovered"] = {"type": "bool", "operationIds": ["patch"]}
    argument_spec["differences"] = {"type": "list", "operationIds": ["patch", "put"]}
    argument_spec["desiredOrchState"] = {
        "type": "str",
        "operationIds": ["patch", "put"],
    }
    argument_spec["description"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["createdAt"] = {"type": "str", "operationIds": ["patch"]}
    argument_spec["autoClean"] = {"type": "bool", "operationIds": ["patch", "put"]}
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
    return "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _delete(params, session):
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}".format(
        **params
    ) + gen_args(
        params, IN_QUERY_PARAMETER
    )
    async with session.delete(_url) as resp:
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
        return await update_changed_flag(_json, resp.status, "delete")


async def _get(params, session):
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}".format(
        **params
    ) + gen_args(
        params, IN_QUERY_PARAMETER
    )
    async with session.get(_url) as resp:
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
        return await update_changed_flag(_json, resp.status, "get")


async def _head(params, session):
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}".format(
        **params
    ) + gen_args(
        params, IN_QUERY_PARAMETER
    )
    async with session.head(_url) as resp:
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
        return await update_changed_flag(_json, resp.status, "head")


async def _patch(params, session):
    accepted_fields = [
        "autoClean",
        "createdAt",
        "description",
        "desiredOrchState",
        "differences",
        "discovered",
        "id",
        "label",
        "nativeState",
        "obfuscate",
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
        "validate",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}".format(
        **params
    )
    async with session.patch(_url, json=spec) as resp:
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
        return await update_changed_flag(_json, resp.status, "patch")


async def _put(params, session):
    accepted_fields = [
        "autoClean",
        "description",
        "desiredOrchState",
        "differences",
        "id",
        "label",
        "nativeState",
        "obfuscate",
        "orchState",
        "orderId",
        "productId",
        "properties",
        "providerData",
        "providerResourceId",
        "reason",
        "resourceId",
        "resourceTypeId",
        "shared",
        "sharingPermissionId",
        "subDomainId",
        "tags",
        "tenantId",
        "validate",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}".format(
        **params
    )
    async with session.put(_url, json=spec) as resp:
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
        return await update_changed_flag(_json, resp.status, "put")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
