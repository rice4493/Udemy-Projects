from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

smtpserver = 'smtp.elasticemail.com'
sender = 'yukta.noela@outlook.com'
username = 'yukta.noela@outlook.com'
password = "4577E6820C95C24600D73DBA039E9D4B8E50"
text_subtype = 'plain'


def send_email(message, receiver):
    msg = MIMEText(message, text_subtype)

    try:
        with SMTP(smtpserver) as conn:
            conn.set_debuglevel(False)
            conn.login(username, password)
            conn.sendmail(sender, [receiver], msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
