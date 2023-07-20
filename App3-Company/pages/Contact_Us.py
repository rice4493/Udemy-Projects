import pandas
import streamlit as st
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
import re

smtpserver = 'smtp.elasticemail.com'
sender = 'yukta.noela@outlook.com'
username = 'yukta.noela@outlook.com'
password = "4577E6820C95C24600D73DBA039E9D4B8E50"
# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'

st.header("Contact Me")


def is_valid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]'
                       r'+(\.[A-Z|a-z]{2,})+')
    return re.fullmatch(regex, email)


def disable():
    st.session_state.disabled = True


if "disabled" not in st.session_state:
    st.session_state.disabled = False

user_email = st.text_input("Your email address")
if user_email and not is_valid(user_email):
    st.warning("Invalid email. Try again.")

with st.form(key='email'):
    destination = [user_email]

    user_name = st.text_input("Your name")

    df = pandas.read_csv('topics.csv')
    choice = st.selectbox(label="What topic do you want to discuss?",
                                options=df['topic'])

    user_message = st.text_area("Your message")

    button = st.form_submit_button("Submit", on_click=disable,
                                   disabled=st.session_state.disabled)
    if button:
        try:
            message = f"""From: {user_name}\nTopic: {choice}
            \n\n{user_message}\n"""
            msg = MIMEText(message, text_subtype)
            msg['Subject'] = f"New email from {user_email}"
            msg['From'] = sender

            # some SMTP servers will do this automatically, not all
            with SMTP(smtpserver) as conn:
                conn.set_debuglevel(False)
                conn.login(username, password)
                try:
                    conn.sendmail(sender, destination, msg.as_string())
                finally:
                    conn.quit()

            st.info("Your email was sent successfully. \n"
                    "Thank you for reaching out!")

        except Exception as e:
            st.error(f"An error occurred while sending the email: {e}")
            # give an error message
