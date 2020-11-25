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
module: resources_validate
short_description: Handle resource of type resources_validate
description: Handle resource of type resources_validate
options:
  autoClean:
    description:
    - Free up any resources automatically upon any activation failure
    - Used by I(state=['post'])
    type: bool
  custom:
    description:
    - Whether to perform custom validation in addition to built-in schema and accessor
      validations
    - Used by I(state=['post'])
    type: bool
  description:
    description:
    - Detailed description of this resource
    - Used by I(state=['post'])
    type: str
  desiredOrchState:
    description:
    - Desired orchestration state
    - Used by I(state=['post'])
    type: str
  discovered:
    description:
    - Is this resource discovered
    - Used by I(state=['post'])
    type: bool
  full:
    description:
    - Whether the request body represents a full resource
    - Required with I(state=['post'])
    - Used by I(state=['post'])
    type: bool
  label:
    description:
    - Textual label
    - Used by I(state=['post'])
    type: str
  nativeState:
    description:
    - Native (type specific) state
    - Used by I(state=['post'])
    type: str
  orchState:
    description:
    - Current state of the resource in the orchestrator
    - Used by I(state=['post'])
    type: str
  orderId:
    description:
    - If applicable, the order containing this resource
    - Used by I(state=['post'])
    type: str
  productId:
    description:
    - The type of product for this resource
    - Used by I(state=['post'])
    type: str
  properties:
    description:
    - Properties
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['post'])
    type: dict
  providerData:
    description:
    - Provider custom data
    - 'Validate attributes are:'
    - ' - C(obj) (list): '
    - Used by I(state=['post'])
    type: dict
  providerResourceId:
    description:
    - Identifier of the resource in provider's context
    - Used by I(state=['post'])
    type: str
  reason:
    description:
    - Reason for the orchestration state
    - Used by I(state=['post'])
    type: str
  shared:
    description:
    - Is resource shared?
    - Used by I(state=['post'])
    type: bool
  sharingPermissionId:
    description:
    - The sharing permission of the resource
    - Used by I(state=['post'])
    type: str
  state:
    choices:
    - post
    description: []
    type: str
  subDomainId:
    description:
    - Sub-domain ID
    - Used by I(state=['post'])
    type: str
  tags:
    description:
    - Tags
    - Used by I(state=['post'])
    type: dict
author: []
version_added: 1.0.0
requirements:
- python >= 3.6
"""
IN_QUERY_PARAMETER = ["custom", "full"]
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
    argument_spec["tags"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["subDomainId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["state"] = {"type": "str", "choices": ["post"]}
    argument_spec["sharingPermissionId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["shared"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["reason"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["providerResourceId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["providerData"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["properties"] = {"type": "dict", "operationIds": ["post"]}
    argument_spec["productId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["orderId"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["orchState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["nativeState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["label"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["full"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["discovered"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["desiredOrchState"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["description"] = {"type": "str", "operationIds": ["post"]}
    argument_spec["custom"] = {"type": "bool", "operationIds": ["post"]}
    argument_spec["autoClean"] = {"type": "bool", "operationIds": ["post"]}
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
    return "{mdso_hostname}/bpocore/market/api/v1/resources/validate".format(**params)


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _post(params, session):
    accepted_fields = [
        "autoClean",
        "custom",
        "description",
        "desiredOrchState",
        "discovered",
        "full",
        "label",
        "nativeState",
        "orchState",
        "orderId",
        "productId",
        "properties",
        "providerData",
        "providerResourceId",
        "reason",
        "shared",
        "sharingPermissionId",
        "subDomainId",
        "tags",
    ]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "{mdso_hostname}/bpocore/market/api/v1/resources/validate".format(
        **params
    ) + gen_args(params, IN_QUERY_PARAMETER)
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
