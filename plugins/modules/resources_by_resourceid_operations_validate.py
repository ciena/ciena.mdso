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
module: resources_by_resourceid_operations_validate
short_description: Handle resource of type resources_by_resourceid_operations_validate
description: Handle resource of type resources_by_resourceid_operations_validate
options:
  description:
    description:
    - Description of the operation
    - Used by I(state=['post'])
    type: str
  full:
    description:
    - Whether the request body represents a full resource operation
    - Required with I(state=['post'])
    - Used by I(state=['post'])
    type: bool
  inputs:
    description:
    - Inputs of the operation
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['post'])
    type: dict
  interface:
    description:
    - ID of the interface
    - Used by I(state=['post'])
    type: str
  resourceId:
    description:
    - Identifier of the resource for which the operation will be created against
    - Required with I(state=['post'])
    - Used by I(state=['post'])
    type: str
  resourceStateConstraints:
    description:
    - Constraints of the resource state for this operation to execute
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['post'])
    type: dict
  state:
    choices:
    - post
    description: []
    type: str
  title:
    description:
    - Title of the operation
    - Used by I(state=['post'])
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["full"]
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
    argument_spec["title"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["state"] = {"type": "str", "choices": ["post"]}
    argument_spec["resourceStateConstraints"] = {
        "type": "dict",
        "operationIds": ["post"],
    }
    argument_spec["resourceId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["interface"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["inputs"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["full"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["post"]}
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
    return "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}/operations/validate".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _post(params, session):
    accepted_fields = [
        "description",
        "full",
        "inputs",
        "interface",
        "resourceId",
        "resourceStateConstraints",
        "title",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/resources/{resourceId}/operations/validate".format(
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
