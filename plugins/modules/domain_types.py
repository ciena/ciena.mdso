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
module: domain_types
short_description: Handle resource of type domain_types
description: Handle resource of type domain_types
options:
  limit:
    description:
    - The maximum number of elements to return in a single paged request
    - Used by I(state=['get', 'head'])
    type: int
  offset:
    description:
    - Requested offset within the total result set to be the first element in the
      paged response
    - Used by I(state=['get', 'head'])
    type: int
  pageToken:
    description:
    - String pagination token returned from a previous query that encodes query information
      in order to optimize a
    - subsequent request for a page of results. The token includes the limit and offset
      parameters for the next page, but one or
    - both can be included to override the encoded values
    - Used by I(state=['get', 'head'])
    type: str
  q:
    description:
    - Optional query parameter to define a query filter using property:value syntax
    - Used by I(state=['get', 'head'])
    type: str
  state:
    choices:
    - get
    - head
    description: []
    type: str
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["limit", "offset", "pageToken", "q"]
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
    argument_spec["state"] = {"type": "str", "choices": ["get", "head"]}
    argument_spec["q"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["pageToken"] = {"type": "str", "operationIds": ["get", "head"]}
    argument_spec["offset"] = {"type": "int", "operationIds": ["get", "head"]}
    argument_spec["limit"] = {"type": "int", "operationIds": ["get", "head"]}
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
    return "{mdso_hostname}/bpocore/market/api/v1/domain-types".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _get(params, session):
    _url = "{mdso_hostname}/bpocore/market/api/v1/domain-types".format(
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
    _url = "{mdso_hostname}/bpocore/market/api/v1/domain-types".format(
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


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
