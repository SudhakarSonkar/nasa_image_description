import smtplib, ssl, certifi

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "sudhakarsonkar007@gmail.com"
    password = "ckst-ofze-bcid-giab-giab"

    receiver = "sudhakarsonkar007@gmail.com"
    context = ssl.create_default_context(cafile=certifi.where())

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
