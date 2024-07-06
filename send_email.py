import smtplib
import ssl
import os


def send_email(receive, message_arg):
    email = "jorgeaf303@gmail.com"
    password = os.getenv("PASSWORD")
    print(password)
    host = "smtp.gmail.com"
    port = 465
    receive_me = "jorgeaf303@gmail.com"
    message = f"""\
Subject: New message from: {receive}

From: {receive} 
{message_arg}
"""
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(email, password)
        server.sendmail(email, receive_me, message)

