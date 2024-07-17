import smtplib, ssl


def send_an_email(message):
    # global host, port, username, password, context, message
    host = "smtp.gmail.com"
    port = 465

    username = "airelking@gmail.com"
    password = "gpyr lrrm fkqt cuox"

    receiver = "airelking@gmail.com"  # who we are sending the email to
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as servers:
        servers.login(username, password)
        servers.sendmail(username, receiver, message)