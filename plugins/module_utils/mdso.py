import aiohttp

import functools
import json
from async_lru import alru_cache


@alru_cache()
async def open_session(
    mdso_hostname=None, mdso_username=None, mdso_password=None, validate_certs=False
):
    connector = aiohttp.TCPConnector(limit=20, verify_ssl=validate_certs)
    async with aiohttp.ClientSession(
        connector=connector,
        connector_owner=False,
        headers={"content-type": "application/json"},
    ) as session:
        if not mdso_hostname.startswith("http"):
            async with session.post(
                "{hostname}/tron/api/v1/tokens".format(hostname=mdso_hostname),
                json={"username": mdso_username, "password": mdso_password},
            ) as resp:
                if resp.status != 201:
                    try:
                        from ansible_module.turbo.exceptions import (
                            EmbeddedModuleFailure,
                        )

                        raise EmbeddedModuleFailure(
                            "Authentication failure. code: {}, json: {}".format(
                                resp.status, await resp.text()
                            )
                        )
                    except ImportError:
                        pass
                response = await resp.json()
                token = response["token"]
                headers = {
                    "Authorization": "Bearer %s" % token,
                    "content-type": "application/json",
                }
        else:
            headers = {"content-type": "application/json"}

        session = aiohttp.ClientSession(
            connector=connector, headers=headers, connector_owner=False
        )
        return session


def gen_args(params, in_query_parameter):
    args = ""
    for i in in_query_parameter:
        v = params.get(i)
        if not v:
            continue
        if not args:
            args = "?"
        else:
            args += "&"
        if isinstance(v, list):
            for j in v:
                args += (i + "=") + j
        elif isinstance(v, bool) and v:
            args += i + "=true"
        else:
            args += (i + "=") + v
    return args


async def update_changed_flag(data, status, operation):
    success_operations = [200, 201, 204]
    if operation == "create" and status in success_operations:
        data["failed"] = False
        data["changed"] = True
    elif operation == "delete" and status in success_operations:
        data["failed"] = False
        data["changed"] = True
    elif operation == "delete" and status in success_operations:
        data["failed"] = False
        data["changed"] = True

    data["_debug_info"] = {"status": status, "operation": operation}
    return data
