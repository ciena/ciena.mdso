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
module: relationships_by_relationshipid
short_description: Handle resource of type relationships_by_relationshipid
description: Handle resource of type relationships_by_relationshipid
options:
  relationshipId:
    description:
    - Identifier of the relationship being queried
    type: str
  state:
    choices:
    - delete
    - get
    - head
    description: []
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = []
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
    argument_spec["state"] = {"type": "str", "choices": ["delete", "get", "head"]}
    argument_spec["relationshipId"] = {
        "type": "str",
        "operationIds": ["delete", "get", "head"],
    }
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
    return "https://{app_hostname}/bpocore/market/api/v1/relationships/{relationshipId}".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _delete(params, session):
    _url = "https://{app_hostname}/bpocore/market/api/v1/relationships/{relationshipId}".format(
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
    _url = "https://{app_hostname}/bpocore/market/api/v1/relationships/{relationshipId}".format(
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
    _url = "https://{app_hostname}/bpocore/market/api/v1/relationships/{relationshipId}".format(
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


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
