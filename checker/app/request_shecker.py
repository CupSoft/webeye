import asyncio
import logging
import sys
import time
from datetime import datetime

import aiohttp

from app.URLS import URL_SEND_ANSWER
from app.headers import base_headers, api_headers
from app.models_pdc import Task, Answer, Status


async def request_dispatcher(tasks: list[Task]) -> list[Answer]:
    async with aiohttp.ClientSession(headers=base_headers) as session:
        pack = []
        # TODO: make request from each proxy
        for task in tasks:
            pack.append(asyncio.ensure_future(my_request(session, task)))
        answers = await asyncio.gather(*pack)
        return answers


async def send_answers(answers: list[Answer]):
    async with aiohttp.ClientSession(headers=api_headers) as session:
        pack = [asyncio.ensure_future(send_answer(session, ans)) for ans in answers]
        answers = await asyncio.gather(*pack)


async def send_answer(session, answer: Answer):
    json = answer.json()
    logging.info(f"Send. Check_uuid: {answer.check_uuid}")
    async with session.post(URL_SEND_ANSWER, data=json, headers=api_headers) as resp:
        if resp.status != 201:
            print(f"Error status: {resp.status}")
            logging.error("API is not responding")


async def my_request(session, task: Task):
    start_time = time.time()
    resp_code = 500
    try:
        if task.request_type == "GET":
            resp_code = await get_request(session, task)
    except Exception as e:
        logging.error(e)

    end_time = time.time()
    if resp_code == task.expectation:
        status = Status.ok
        if end_time - start_time > 1:
            status = Status.partial
        return Answer(response=str(resp_code), location="RUSSIA", datetime=datetime.now(), status=status,
                      check_uuid=task.uuid)
    return Answer(response=str(resp_code), location="RUSSIA", datetime=datetime.now(), status=Status.critical,
                  check_uuid=task.uuid)


async def get_request(session, task: Task) -> Answer:
    async with session.get(task.url, allow_redirects=True, timeout=15, verify_ssl=False) as resp:
        if resp.status != 200:
            logging.warning(f"Problem with {task.url} \nStatus: {resp.status} \nText: {await resp.text()}")
        return resp.status
