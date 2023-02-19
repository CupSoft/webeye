import logging
from email.message import EmailMessage
from config import settings as s
import aiosmtplib

from schemas import EmailNotification


async def sender(email: EmailNotification):
    message = EmailMessage()
    message["From"] = s.SMTP_USERNAME
    message["To"] = email.recipient
    message["Subject"] = email.subject
    message.set_content(email.body)
    try:
        await aiosmtplib.send(
            message,
            hostname=s.SMTP_HOST,
            port=s.SMTP_PORT,
            username=s.SMTP_USERNAME,
            password=s.SMTP_PASSWORD,
            use_tls=True,
        )
        logging.info(f"The email was successfully sent to {email.recipient}")

    except Exception as e:
        logging.error(e)
