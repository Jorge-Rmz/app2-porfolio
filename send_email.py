import smtplib
import ssl

email = "jorgeaf303@gmail.com"
password = "uryq hmxn fjtk tbyi"
host = "smtp.gmail.com"
port = 465
receive = "jorgeaf303@gmail.com"


my_context = ssl.create_default_context()

message = """\
Subject: Hi, 
How are you? 
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(email, password)
    server.sendmail(email, receive, message)

