import smtplib
import ssl
from email.message import EmailMessage
from typing import List


def send_email(username: str, password: str, receivers: List[str], text: str, subject: str) -> None:
    port = 465
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(username, password)
        for receiver in receivers:
            msg = EmailMessage()
            msg.set_content(text)
            msg['Subject'] = subject
            msg['From'] = username
            msg['To'] = receiver
            server.send_message(msg)
        server.quit()
