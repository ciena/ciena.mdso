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
module: domains_by_domainid
short_description: Handle resource of type domains_by_domainid
description: Handle resource of type domains_by_domainid
options:
  accessUrl:
    description:
    - Access URL to the domain
    - Used by I(state=['patch', 'put'])
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
    - Used by I(state=['patch', 'put'])
    type: dict
  connectionStatus:
    description:
    - Connection status of the domain
    - Used by I(state=['patch', 'put'])
    type: dict
  description:
    description:
    - Detailed description
    - Used by I(state=['patch', 'put'])
    type: str
  domainId:
    description:
    - Identifier of the domain being queried
    - Required with I(state=['delete', 'get', 'head', 'patch', 'put'])
    - Used by I(state=['delete', 'get', 'head', 'patch', 'put'])
    type: str
  domainType:
    description:
    - Type of the domain
    - Used by I(state=['patch', 'put'])
    type: str
  id:
    description:
    - Unique id of the domain
    - Used by I(state=['patch', 'put'])
    type: str
  initialDiscoveryStatus:
    description:
    - Initial Discovery status of the domain
    - Used by I(state=['patch', 'put'])
    type: dict
  lastConnected:
    description:
    - Last time domain was connected to southbound
    - Used by I(state=['patch', 'put'])
    type: str
  obfuscate:
    description:
    - If true, schema obfuscated values will be replaced with a fixed string in the
      response.
    - Used by I(state=['get', 'head', 'patch', 'put'])
    type: bool
  onlyEnableTypes:
    description:
    - When non-empty, only enable these resource types in the domain
    - Used by I(state=['patch', 'put'])
    type: list
  operationMode:
    description:
    - Operation mode of this domain
    - Used by I(state=['patch', 'put'])
    type: str
  properties:
    description:
    - Properties the domain
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['patch', 'put'])
    type: dict
  reason:
    description:
    - Reason message for connection failure
    - Used by I(state=['patch', 'put'])
    type: str
  rpId:
    description:
    - Resource provider that creates this domain
    - Used by I(state=['patch', 'put'])
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
  tenantId:
    description:
    - Orchestrator tenant
    - Used by I(state=['patch', 'put'])
    type: str
  title:
    description:
    - Descriptive name/title of domain
    - Used by I(state=['patch', 'put'])
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["obfuscate"]
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
    argument_spec["title"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["tenantId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["rpId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["reason"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["properties"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["operationMode"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["onlyEnableTypes"] = {
        "type": "list",
        "operationIds": ["patch", "put"],
    }
    argument_spec["obfuscate"] = {
        "type": "bool",
        "operationIds": ["get", "head", "patch", "put"],
    }
    argument_spec["lastConnected"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["initialDiscoveryStatus"] = {
        "type": "dict",
        "operationIds": ["patch", "put"],
    }
    argument_spec["id"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["domainType"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["domainId"] = {
        "type": "str",
        "operationIds": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["description"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["connectionStatus"] = {
        "type": "dict",
        "operationIds": ["patch", "put"],
    }
    argument_spec["address"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["accessUrl"] = {"type": "str", "operationIds": ["patch", "put"]}
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
    return "{mdso_hostname}/bpocore/market/api/v1/domains/{domainId}".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _delete(params, session):
    _url = "{mdso_hostname}/bpocore/market/api/v1/domains/{domainId}".format(
        **params
    ) + gen_args(params, IN_QUERY_PARAMETER)
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
    _url = "{mdso_hostname}/bpocore/market/api/v1/domains/{domainId}".format(
        **params
    ) + gen_args(params, IN_QUERY_PARAMETER)
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
    _url = "{mdso_hostname}/bpocore/market/api/v1/domains/{domainId}".format(
        **params
    ) + gen_args(params, IN_QUERY_PARAMETER)
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
        "accessUrl",
        "address",
        "connectionStatus",
        "description",
        "domainId",
        "domainType",
        "id",
        "initialDiscoveryStatus",
        "lastConnected",
        "obfuscate",
        "onlyEnableTypes",
        "operationMode",
        "properties",
        "reason",
        "rpId",
        "tenantId",
        "title",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "{mdso_hostname}/bpocore/market/api/v1/domains/{domainId}".format(
        **params
    ) + gen_args(params, IN_QUERY_PARAMETER)
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
        "accessUrl",
        "address",
        "connectionStatus",
        "description",
        "domainId",
        "domainType",
        "id",
        "initialDiscoveryStatus",
        "lastConnected",
        "obfuscate",
        "onlyEnableTypes",
        "operationMode",
        "properties",
        "reason",
        "rpId",
        "tenantId",
        "title",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "{mdso_hostname}/bpocore/market/api/v1/domains/{domainId}".format(
        **params
    ) + gen_args(params, IN_QUERY_PARAMETER)
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
