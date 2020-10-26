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
module: resources_by_resourceid_operations_by_operationid
short_description: Handle resource of type resources_by_resourceid_operations_by_operationid
description: Handle resource of type resources_by_resourceid_operations_by_operationid
options:
  createdAt:
    description:
    - When the operation was created
    - Used by I(state=['patch', 'put'])
    type: str
  description:
    description:
    - Description of the operation
    - Used by I(state=['patch', 'put'])
    type: str
  executionGroup:
    description:
    - Execution group of the operation
    - Used by I(state=['patch', 'put'])
    type: str
  id:
    description:
    - Unique identifier for the operation
    - Used by I(state=['patch', 'put'])
    type: str
  inputs:
    description:
    - Inputs of the operation
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['patch', 'put'])
    type: dict
  interface:
    description:
    - ID of the interface
    - Used by I(state=['patch', 'put'])
    type: str
  minRevision:
    description:
    - Require the revision of the returned resource to be greater than or equal to
      minRevision. Respond with a 503 if the resource exists, but the revision does
      not meet the minRevision
    - Used by I(state=['get', 'head'])
    type: int
  operationId:
    description:
    - Identifier of the operation to be queried
    - Required with I(state=['delete', 'get', 'head', 'patch', 'put'])
    - Used by I(state=['delete', 'get', 'head', 'patch', 'put'])
    type: str
  outputs:
    description:
    - Outputs of the operation
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['patch', 'put'])
    type: dict
  progress:
    description:
    - Describes any progress towards completion that the operation has made
    - 'Validate attributes are:'
    - ' - C(arr) (list): '
    - Used by I(state=['patch', 'put'])
    type: dict
  providerData:
    description:
    - Provider custom data
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['patch', 'put'])
    type: dict
  reason:
    description:
    - Reason for the operation state
    - Used by I(state=['patch', 'put'])
    type: str
  resourceId:
    description:
    - Identifier of the resource whose operations will be queried
    - Required with I(state=['delete', 'get', 'head', 'patch', 'put'])
    - Used by I(state=['delete', 'get', 'head', 'patch', 'put'])
    type: str
  resourceStateConstraints:
    description:
    - Constraints of the resource state for this operation to execute
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['patch', 'put'])
    type: dict
  revision:
    description:
    - Strictly increasing revision number, incremented every update
    - Used by I(state=['patch', 'put'])
    type: int
  state:
    choices:
    - delete
    - get
    - head
    - patch
    - put
    description: []
    type: str
  title:
    description:
    - Title of the operation
    - Used by I(state=['patch', 'put'])
    type: str
  updatedAt:
    description:
    - When the operation was last updated
    - Used by I(state=['patch', 'put'])
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["minRevision"]
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
    argument_spec["updatedAt"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["title"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["revision"] = {"type": "int", "operationIds": ["patch", "put"]}
    argument_spec["resourceStateConstraints"] = {
        "type": "dict",
        "operationIds": ["patch", "put"],
    }
    argument_spec["resourceId"] = {
        "type": "str",
        "operationIds": ["delete", "get", "head", "patch", "patch", "put", "put"],
    }
    argument_spec["reason"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["providerData"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["progress"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["outputs"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["operationId"] = {
        "type": "str",
        "operationIds": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["minRevision"] = {"type": "int", "operationIds": ["get", "head"]}
    argument_spec["interface"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["inputs"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["executionGroup"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["createdAt"] = {"type": "str", "operationIds": ["patch", "put"]}
    return argument_spec


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
    return "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}/operations/{operationId}".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _delete(params, session):
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}/operations/{operationId}".format(
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
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}/operations/{operationId}".format(
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
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}/operations/{operationId}".format(
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
        "createdAt",
        "description",
        "executionGroup",
        "id",
        "inputs",
        "interface",
        "operationId",
        "outputs",
        "progress",
        "providerData",
        "reason",
        "resourceId",
        "resourceStateConstraints",
        "revision",
        "title",
        "updatedAt",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}/operations/{operationId}".format(
        **params
    ) + gen_args(
        params, IN_QUERY_PARAMETER
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
        "createdAt",
        "description",
        "executionGroup",
        "id",
        "inputs",
        "interface",
        "operationId",
        "outputs",
        "progress",
        "providerData",
        "reason",
        "resourceId",
        "resourceStateConstraints",
        "revision",
        "title",
        "updatedAt",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}/operations/{operationId}".format(
        **params
    ) + gen_args(
        params, IN_QUERY_PARAMETER
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
