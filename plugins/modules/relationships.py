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
module: relationships
short_description: Handle resource of type relationships
description: Handle resource of type relationships
options:
  capabilityName:
    description:
    - Capability name in target resource
    type: str
  exactRelationshipTypeId:
    description:
    - Optional query to limit relationships by an exact relationship type
    type: str
  id:
    description:
    - Unique identifier for the relationship (optional/ignored on calls to create)
    type: str
  limit:
    description:
    - The maximum number of elements to return in a single paged request
    type: int
  offset:
    description:
    - Requested offset within the total result set to be the first element in the
      paged response
    type: int
  orchState:
    description:
    - Current state of the resource in the orchestrator
    type: str
  p:
    description:
    - Optional query parameter to define a partial string match filter using property:value
      syntax
    type: str
  pageToken:
    description:
    - String pagination token returned from a previous query that encodes query information
      in order to optimize a
    - subsequent request for a page of results. The token includes the limit and offset
      parameters for the next page, but one or
    - both can be included to override the encoded values
    type: str
  properties:
    description:
    - Relationship properties
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  providerData:
    description:
    - Provider custom data
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  q:
    description:
    - Optional query parameter to define a query filter using property:value syntax
    type: str
  reason:
    description:
    - Reason for the orchestration state
    type: str
  relationshipTypeId:
    description:
    - Optional query to limit relationships by the relationship type (including derived
      types)
    type: str
  requirementName:
    description:
    - Requirement name in source resource
    type: str
  sourceId:
    description:
    - UUID of source resource
    type: str
  state:
    choices:
    - get
    - head
    - post
    description: []
    type: str
  targetId:
    description:
    - UUID of target resource
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = [
    "exactRelationshipTypeId",
    "limit",
    "offset",
    "p",
    "pageToken",
    "q",
]
from ansible.module_utils.basic import env_fallback

try:
    from ansible_module.turbo.module import AnsibleTurboModule as AnsibleModule
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vendor.app.plugins.module_utils.app import (
    gen_args,
    open_session,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "app_hostname": dict(
            type="str", required=False, fallback=(env_fallback, ["APP_HOST"])
        ),
        "app_username": dict(
            type="str", required=False, fallback=(env_fallback, ["APP_USER"])
        ),
        "app_password": dict(
            type="str",
            required=False,
            no_log=True,
            fallback=(env_fallback, ["APP_PASSWORD"]),
        ),
    }
    argument_spec["targetId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["state"] = {"type": "str", "choices": ["get", "head", "post"]}
    argument_spec["sourceId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["requirementName"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["relationshipTypeId"] = {
        "type": "str",
        "operationIds": ["get", "head", "post"],
    }
    argument_spec["reason"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["q"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["providerData"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["properties"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["pageToken"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["p"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["orchState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["offset"] = {"type": "int", "operationIds": ["get", "head"]}
    argument_spec["limit"] = {"type": "int", "operationIds": ["get", "head"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["exactRelationshipTypeId"] = {
        "type": "str",
        "operationIds": ["get", "head"],
    }
    argument_spec["capabilityName"] = {"type": "str", "operationIds": ["post"]}
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
        app_hostname=module.params["app_hostname"],
        app_username=module.params["app_username"],
        app_password=module.params["app_password"],
    )
    result = await entry_point(module, session)
    module.exit_json(**result)


def url(params):
    return "https://{app_hostname}/bpocore/market/api/v1/relationships".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    accepted_fields = ["relationshipTypeId"]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{app_hostname}/bpocore/market/api/v1/relationships".format(**params)
    async with session.get(_url, json=spec) as resp:
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
    accepted_fields = ["relationshipTypeId"]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{app_hostname}/bpocore/market/api/v1/relationships".format(**params)
    async with session.head(_url, json=spec) as resp:
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


async def _post(params, session):
    accepted_fields = [
        "capabilityName",
        "id",
        "orchState",
        "properties",
        "providerData",
        "reason",
        "relationshipTypeId",
        "requirementName",
        "sourceId",
        "targetId",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = "https://{app_hostname}/bpocore/market/api/v1/relationships".format(**params)
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
