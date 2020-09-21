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
module: products_by_productid_resync
short_description: Handle resource of type products_by_productid_resync
description: Handle resource of type products_by_productid_resync
options:
  full:
    description:
    - Whether the requeset is for a full resync
    type: bool
  productId:
    description:
    - Identifier of the product to be resynced
    type: str
  state:
    choices:
    - post
    description: []
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
    argument_spec["state"] = {"type": "str", "choices": ["post"]}
    argument_spec["productId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["full"] = {"type": "bool", "operationIds": ["post"]}
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
    return "https://{app_hostname}/bpocore/market/api/v1/products/{productId}/resync".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _post(params, session):
    _url = "https://{app_hostname}/bpocore/market/api/v1/products/{productId}/resync".format(
        **params
    ) + gen_args(
        params, IN_QUERY_PARAMETER
    )
    async with session.post(_url) as resp:
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
