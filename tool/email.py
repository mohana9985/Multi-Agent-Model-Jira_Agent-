import os
import asyncio
from email.mime.text import MIMEText
from aiosmtplib import SMTP
from langchain_core.tools import tool
from dotenv import load_dotenv

@tool("individual_email_tool", return_direct=True)
def individual_email_tool(to_email: list, subject: str, message: str) -> str:
    """Sends individual email to the list of email address

    Args:
        to_email (str): list of email address
        subject (str): subject
        message (str): message of the email
    """
    for to in to_email:
       load_dotenv()
       smtp_host = os.getenv('SMTP_HOST')
       smtp_port = int(os.getenv('SMTP_PORT'))
       smtp_username = os.getenv('SMTP_USERNAME01')
       smtp_password = os.getenv('SMTP_PASSWORD01')
       email_message = MIMEText(message)
       email_message["From"] = os.getenv('FROM_EMAIL')
       email_message["To"] = to
       email_message["Subject"] = subject
       with SMTP(hostname=smtp_host, port=smtp_port) as smtp:
        smtp.login(smtp_username, smtp_password)
        smtp.send_message(email_message)


