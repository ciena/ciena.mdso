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
module: jobs_by_jobid_progress
short_description: Handle resource of type jobs_by_jobid_progress
description: Handle resource of type jobs_by_jobid_progress
options:
  jobId:
    description:
    - Identifier of the job whose execution is in progress
    - Required with I(state=['put'])
    - Used by I(state=['put'])
    type: str
  progress:
    description:
    - Value describing the execution progress
    - Used by I(state=['put'])
    type: dict
  state:
    choices:
    - put
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
    argument_spec["state"] = {"type": "str", "choices": ["put"]}
    argument_spec["progress"] = {"type": "dict", "operationIds": ["put"]}
    argument_spec["jobId"] = {"type": "str", "operationIds": ["put"]}
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
    return "{mdso_hostname}/bpocore/market/api/v1/jobs/{jobId}/progress".format(
        **params
    )


async def entry_point(module, session):
    func = globals()[("_" + module.params["state"])]
    return await func(module.params, session)


async def _put(params, session):
    accepted_fields = ["jobId", "progress"]
    spec = {}
    for i in accepted_fields:
        if params[i] is not None:
            spec[i] = params[i]
    _url = "{mdso_hostname}/bpocore/market/api/v1/jobs/{jobId}/progress".format(
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
