import smtplib, ssl


host = "smtp.gmail.com"
port = 465


username = "airelking@gmail.com"
password = "gpyr lrrm fkqt cuox"
receiver = "airelking@gmail.com"    # who we are sending the email to

context = ssl.create_default_context()

message = """\
Subject: You did it!
How does it feel to be a genius?
"""

with smtplib.SMTP_SSL(host, port, context = context) as servers:
    servers.login(username, password)
    servers.sendmail(username, receiver, message)

