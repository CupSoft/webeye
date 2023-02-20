import asyncio
import logging
import platform
import sys
from asyncio import sleep

import aiohttp
import coloredlogs

from app.URLS import URL_TASKS, URL_GET_JWT
from app.headers import base_headers, api_headers
from app.models_pdc import Task
from app.request_shecker import request_dispatcher, send_answers
from app.settings import settings


async def get_root_jwt():
    async with aiohttp.ClientSession() as session:
        json = {
            "username": settings().API_LOGIN,
            "password": settings().API_PASSWORD,
        }
        async with session.post(URL_GET_JWT, data=json) as resp:
            if resp.status != 200:
                logging.info("JWT token not received!!!")
                sys.exit(-1)
            data = await resp.json()
            logging.info("Root jwt successfully received")
            return f"Bearer {data['access_token']}"


async def get_tasks() -> list[Task]:
    tasks = []
    async with aiohttp.ClientSession(headers=api_headers) as session:
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
        logging.info("Responses received, sending... ")
        await send_answers(answers)
        logging.info("Sending completed")
        await sleep(3 * 60)


async def main():
    coloredlogs.install(level=logging.INFO)
    logging.info("Startup")
    root_jwt = await get_root_jwt()
    api_headers["Authorization"] = root_jwt
    await watcher()


if __name__ == "__main__":
    try:
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Checker stopped!")
