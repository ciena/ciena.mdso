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
module: products_by_productid
short_description: Handle resource of type products_by_productid
description: Handle resource of type products_by_productid
options:
  active:
    description:
    - State of the product (active or inactive)
    type: bool
  constraints:
    description:
    - Additional constraints for the product
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  description:
    description:
    - Detailed description of the product
    type: str
  domainId:
    description:
    - Identifier of the domain that advertises the product
    type: str
  id:
    description:
    - Unique identifier of the product (ignored during create request)
    type: str
  productId:
    description:
    - Identifier of the product being queried
    type: str
  providerData:
    description:
    - Provider custom data
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    type: dict
  providerProductId:
    description:
    - Identifier within the provider's context or scope for the product
    type: str
  resourceTypeId:
    description:
    - The type of resource provided by the product
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
  title:
    description:
    - Name or title describing the product
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
    argument_spec["state"] = {
        "type": "str",
        "choices": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["resourceTypeId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["providerProductId"] = {
        "type": "str",
        "operationIds": ["patch", "put"],
    }
    argument_spec["providerData"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["productId"] = {
        "type": "str",
        "operationIds": ["delete", "get", "head", "patch", "put"],
    }
    argument_spec["id"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["domainId"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["patch", "put"]}
    argument_spec["constraints"] = {"type": "dict", "operationIds": ["patch", "put"]}
    argument_spec["active"] = {"type": "bool", "operationIds": ["patch", "put"]}
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
    return "https://{mdso_hostname}/bpocore/market/api/v1/products/{productId}".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _delete(params, session):
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/products/{productId}".format(
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
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/products/{productId}".format(
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
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/products/{productId}".format(
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
        "active",
        "constraints",
        "description",
        "domainId",
        "id",
        "productId",
        "providerData",
        "providerProductId",
        "resourceTypeId",
        "title",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/products/{productId}".format(
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
        "active",
        "constraints",
        "description",
        "domainId",
        "id",
        "productId",
        "providerData",
        "providerProductId",
        "resourceTypeId",
        "title",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "https://{mdso_hostname}/bpocore/market/api/v1/products/{productId}".format(
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
