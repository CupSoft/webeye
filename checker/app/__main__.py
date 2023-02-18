import asyncio
import logging
import platform
from asyncio import sleep

import aiohttp
import coloredlogs
from aiohttp import ClientSession

from app.URLS import URL_TASKS
from app.models_pdc import Task
from app.request_shecker import request_dispatcher

base_headers = {"X-Requested-With": "XMLHttpRequest", "Content-Type": "application/json"}


async def get_root_jwt():
    async with aiohttp.ClientSession() as session:
        url = ''
        async with session.get(url) as resp:
            data = await resp.json()
            logging.info("Root jwt successfully received")
            return data["jwt"]


async def get_tasks(session: ClientSession) -> list[Task]:
    tasks = []
    t = ["https://www.twilio.com/", "https://dovuz.sfu-kras.ru/", "https://aiosmtplib.readthedocs.io/"]
    for i in range(3):
        tasks.append(Task(db_id=i, method="get", url=t[i], expectation_code=200))
    return tasks

    async with session.get(URL_TASKS) as resp:
        data = await resp.json()


async def watcher():
    while True:
        logging.info("Watcher iteration")
        async with aiohttp.ClientSession(headers=base_headers) as session:
            # TODO: Разобраться с сессиями (токены)
            tasks = await get_tasks(session)
            answers = await request_dispatcher(session, tasks)
            print(answers)
        await sleep(3 * 60)


async def main():
    global base_headers
    coloredlogs.install(level=logging.INFO)
    logging.info("Startup")
    # root_jwt = get_root_jwt()
    # base_headers["root_jwt"] = root_jwt
    await watcher()


if __name__ == "__main__":
    try:
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Checker stopped!")

