import asyncio
import logging
import time

import aiohttp

from app.headers import base_headers
from app.models_pdc import Task, Answer


async def request_dispatcher(tasks: list[Task]) -> list[Answer]:
    async with aiohttp.ClientSession(headers=base_headers) as session:
        pack = [asyncio.ensure_future(get_request(session, task)) for task in tasks]
        # TODO: make request from each proxy
        for task in tasks:
            pack.append(asyncio.ensure_future(my_request(session, task)))
        answers = await asyncio.gather(*pack)
        return answers


async def my_request(session, task: Task):
    start_time = time.time()
    status = -1
    try:
        if task.request_type == "GET":
            status = await get_request(session, task)
    except Exception as e:
        logging.error(e)

    end_time = time.time()
    if status == task.expectation:
        if end_time - start_time > 0.5:
            return Answer(uuid=task.uuid, status="partial")
        return Answer(uuid=task.uuid, status="ok")
    return Answer(uuid=task.uuid, status="critical")


async def get_request(session, task: Task) -> Answer:
    async with session.get(task.url) as resp:
        return resp.status
