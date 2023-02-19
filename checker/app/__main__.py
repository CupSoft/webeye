import asyncio
import logging
import platform
from asyncio import sleep

import aiohttp
import coloredlogs

from app.URLS import URL_TASKS
from app.headers import base_headers
from app.models_pdc import Task
from app.request_shecker import request_dispatcher



async def get_root_jwt():
    async with aiohttp.ClientSession() as session:
        url = ''
        async with session.get(url) as resp:
            data = await resp.json()
            logging.info("Root jwt successfully received")
            return data["jwt"]


async def get_tasks() -> list[Task]:
    tasks = []
    async with aiohttp.ClientSession(headers=base_headers) as session:
        async with session.get(URL_TASKS) as resp:
            data = await resp.json()
            for task in data:
                tasks.append(Task(**task))
    return tasks


async def watcher():
    while True:
        logging.info("Watcher iteration")
        tasks = await get_tasks()
        answers = await request_dispatcher(tasks)
        print(answers)
        await sleep(3 * 60)


async def main():
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
