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
module: sub_domains_by_subdomainid
short_description: Handle resource of type sub_domains_by_subdomainid
description: Handle resource of type sub_domains_by_subdomainid
options:
  applicationSlices:
    description:
    - Set of application slices this sub-domain is in
    type: list
  assignable:
    description:
    - Whether the sub-domain can be re-assigned
    type: bool
  decomposable:
    description:
    - Whether the sub-domain can be decomposed
    type: bool
  description:
    description:
    - Description of the sub-domain
    type: str
  domainId:
    description:
    - ID of the domain this sub-domain belongs to
    type: str
  extendedApplicationSlices:
    description:
    - Set of application slices for which this sub-domain acts as an extended sub-domain
    type: list
  id:
    description:
    - Unique ID of the sub-domain
    type: str
  isDefault:
    description:
    - Whether this sub-domain is its domain's default sub-domain
    type: bool
  name:
    description:
    - Name of the sub-domain
    type: str
  ownerTenantId:
    description:
    - The ID of the owner tenant
    type: str
  parentId:
    description:
    - The ID of the container sub-domain, if applicable
    type: str
  scope:
    description:
    - Scope of the sub-domain
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
    - Identifier of the subdomain to update
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
    argument_spec["subDomainId"] = {
        "type": "str",
        "operationIds": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["state"] = {
        "type": "str",
        "choices": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["scope"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["parentId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["ownerTenantId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["name"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["isDefault"] = {"type": "bool", "operationIds": ["patch", "put"]}
    argument_spec["id"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["extendedApplicationSlices"] = {
        "type": "list",
        "operationIds": ["patch", "put"],
    }
    argument_spec["domainId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["decomposable"] = {"type": "bool", "operationIds": ["patch", "put"]}
    argument_spec["assignable"] = {"type": "bool", "operationIds": ["patch", "put"]}
    argument_spec["applicationSlices"] = {
        "type": "list",
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
        app_hostname=module.params["app_hostname"],
        app_username=module.params["app_username"],
        app_password=module.params["app_password"],
    )
    result = await entry_point(module, session)
    module.exit_json(**result)


def url(params):
    return (
        "https://{app_hostname}/bpocore/market/api/v1/sub-domains/{subDomainId}".format(
            **params
        )
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _delete(params, session):
    _url = (
        "https://{app_hostname}/bpocore/market/api/v1/sub-domains/{subDomainId}".format(
            **params
        )
        + gen_args(params, IN_QUERY_PARAMETER)
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
    _url = (
        "https://{app_hostname}/bpocore/market/api/v1/sub-domains/{subDomainId}".format(
            **params
        )
        + gen_args(params, IN_QUERY_PARAMETER)
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
    _url = (
        "https://{app_hostname}/bpocore/market/api/v1/sub-domains/{subDomainId}".format(
            **params
        )
        + gen_args(params, IN_QUERY_PARAMETER)
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
        "applicationSlices",
        "assignable",
        "decomposable",
        "description",
        "domainId",
        "extendedApplicationSlices",
        "id",
        "isDefault",
        "name",
        "ownerTenantId",
        "parentId",
        "scope",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = (
        "https://{app_hostname}/bpocore/market/api/v1/sub-domains/{subDomainId}".format(
            **params
        )
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
        "applicationSlices",
        "assignable",
        "decomposable",
        "description",
        "domainId",
        "extendedApplicationSlices",
        "id",
        "isDefault",
        "name",
        "ownerTenantId",
        "parentId",
        "scope",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i]:
            spec[i] = params[i]
    _url = (
        "https://{app_hostname}/bpocore/market/api/v1/sub-domains/{subDomainId}".format(
            **params
        )
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
