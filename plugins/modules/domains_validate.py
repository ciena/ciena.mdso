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
module: domains_validate
short_description: Handle resource of type domains_validate
description: Handle resource of type domains_validate
options:
  accessUrl:
    description:
    - Access URL to the domain
    - Used by I(state=['post'])
    type: str
  address:
    description:
    - Address of the domain
    - 'Validate attributes are:'
    - ' - C(city) (str): City'
    - ' - C(country) (str): Country'
    - ' - C(latitude) (number): Latitude'
    - ' - C(longitude) (number): Longitude'
    - ' - C(state) (str): State/province'
    - ' - C(street) (str): Street'
    - ' - C(zip) (str): Postal/zip code'
    - Used by I(state=['post'])
    type: dict
  description:
    description:
    - Detailed description
    - Used by I(state=['post'])
    type: str
  full:
    description:
    - Whether to perform a full validation request
    - Required with I(state=['post'])
    - Used by I(state=['post'])
    type: bool
  onlyEnableTypes:
    description:
    - When non-empty, only enable these resource types in the domain
    - Used by I(state=['post'])
    type: list
  operationMode:
    description:
    - Operation mode of this domain
    - Used by I(state=['post'])
    type: str
  properties:
    description:
    - Properties the domain
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['post'])
    type: dict
  rpId:
    description:
    - Resource provider managing this domain
    - Used by I(state=['post'])
    type: str
  state:
    choices:
    - post
    description: []
    type: str
  tenantId:
    description:
    - Orchestrator tenant ID for the domain owner (if unspecified defaults to requester)
    - Used by I(state=['post'])
    type: str
  title:
    description:
    - Descriptive name/title of domain
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
    argument_spec["tenantId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["state"] = {"type": "str", "choices": ["post"]}
    argument_spec["rpId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["properties"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["operationMode"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["onlyEnableTypes"] = {"type": "list", "operationIds": ["post"]}
    argument_spec["full"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["address"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["accessUrl"] = {"type": "str", "operationIds": ["post"]}
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
    return "https://{mdso_hostname}/bpocore/market/api/v1/domains/validate".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _post(params, session):
    accepted_fields = [
        "accessUrl",
        "address",
        "description",
        "full",
        "onlyEnableTypes",
        "operationMode",
        "properties",
        "rpId",
        "tenantId",
        "title",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/domains/validate".format(
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
