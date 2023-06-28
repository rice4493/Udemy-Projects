import smtplib, ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 535

    username = '20p0839.mcc@gmail.com'
    password = 'hyNgiz-rakda8-xawgez'

    context = ssl.create_default_context()

    receiver = '20p0839.mcc@gmail.com'
    message = """
    Hi! 
    How are you?
    Bye.
    """

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
