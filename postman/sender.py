import logging
from asyncio import sleep
from email.message import EmailMessage
from os import getenv

import aiosmtplib


async def sender(to, event, details):
    logging.info(f"Sending an email to {to}")
    message = EmailMessage()
    message["From"] = getenv("SMTP_USERNAME")
    message["To"] = to
    message["Subject"] = event
    message.set_content(details)
    try:
        await aiosmtplib.send(message,
                              hostname=getenv("SMTP_HOST"),
                              port=getenv("SMTP_PORT"),
                              username=getenv("SMTP_USERNAME"),
                              password=getenv("SMTP_PASSWORD"),
                              use_tls=True)
        logging.info(f"The email was successfully sent to {to}")
    except Exception as e:
        logging.error(e)
