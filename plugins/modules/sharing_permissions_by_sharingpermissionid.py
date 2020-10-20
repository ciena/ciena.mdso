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
module: sharing_permissions_by_sharingpermissionid
short_description: Handle resource of type sharing_permissions_by_sharingpermissionid
description: Handle resource of type sharing_permissions_by_sharingpermissionid
options:
  deletableBySubTenants:
    description:
    - Whether subject is deletable by subtenants if shared
    type: bool
  description:
    description:
    - Description of the permission
    type: str
  id:
    description:
    - Unique id of the permission
    type: str
  isBuiltIn:
    description:
    - Whether this is a built-in permission
    type: bool
  label:
    description:
    - Label of the permission
    type: str
  sharingPermissionId:
    description:
    - Identifier of the sharing permission to update
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
  updatableBySubTenants:
    description:
    - Whether subject is updatable by subtenants if shared
    type: bool
  visibleToSubTenants:
    description:
    - Whether subject is visible to subtenants if shared
    type: bool
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
    argument_spec["visibleToSubTenants"] = {
        "type": "bool",
        "operationIds": ["patch", "put"],
    }
    argument_spec["updatableBySubTenants"] = {
        "type": "bool",
        "operationIds": ["patch", "put"],
    }
    argument_spec["state"] = {
        "type": "str",
        "choices": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["sharingPermissionId"] = {
        "type": "str",
        "operationIds": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["label"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["isBuiltIn"] = {"type": "bool", "operationIds": ["patch", "put"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["deletableBySubTenants"] = {
        "type": "bool",
        "operationIds": ["patch", "put"],
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
        mdso_hostname=module.params["mdso_hostname"],
        mdso_username=module.params["mdso_username"],
        mdso_password=module.params["mdso_password"],
    )
    result = await entry_point(module, session)
    module.exit_json(**result)


def url(params):
    return "https://{mdso_hostname}/bpocore/market/api/v1/sharing-permissions/{sharingPermissionId}".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _delete(params, session):
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/sharing-permissions/{sharingPermissionId}".format(
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
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/sharing-permissions/{sharingPermissionId}".format(
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
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/sharing-permissions/{sharingPermissionId}".format(
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
        "deletableBySubTenants",
        "description",
        "id",
        "isBuiltIn",
        "label",
        "sharingPermissionId",
        "updatableBySubTenants",
        "visibleToSubTenants",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/sharing-permissions/{sharingPermissionId}".format(
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
        "deletableBySubTenants",
        "description",
        "id",
        "isBuiltIn",
        "label",
        "sharingPermissionId",
        "updatableBySubTenants",
        "visibleToSubTenants",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/sharing-permissions/{sharingPermissionId}".format(
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
