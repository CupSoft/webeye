import asyncio
import logging
import time

from aiohttp import ClientSession

from app.models_pdc import Task, Answer


async def request_dispatcher(session: ClientSession, tasks: list[Task]) -> list[Answer]:
    pack = [asyncio.ensure_future(get_request(session, task)) for task in tasks]
    # TODO: make request from each proxy
    for task in tasks:
        if task.method == "get":
            pack.append(asyncio.ensure_future(my_request(session, task)))

    answers = await asyncio.gather(*pack)
    return answers


async def my_request(session, task: Task):
    start_time = time.time()
    status = -1
    try:
        if task.method == "get":
            status = await get_request(session, task)
    except Exception as e:
        logging.error(e)

    end_time = time.time()
    if status == task.expectation_code:
        if end_time - start_time > 0.5:
            return Answer(db_id=task.db_id, status="partial")
        return Answer(db_id=task.db_id, status="ok")
    return Answer(db_id=task.db_id, status="critical")


async def get_request(session, task: Task) -> Answer:
    async with session.get(task.url) as resp:
        return resp.status
