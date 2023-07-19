import pandas
import streamlit as st
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

smtpserver = 'smtp.elasticemail.com'
sender = 'yukta.noela@outlook.com'
username = 'yukta.noela@outlook.com'
password = "4577E6820C95C24600D73DBA039E9D4B8E50"
# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'

st.header("Contact Me")


def disable():
    st.session_state.disabled = True


if "disabled" not in st.session_state:
    st.session_state.disabled = False

with st.form(key='email'):
    user_email = st.text_input("Your email address")
    destination = [user_email]

    user_name = st.text_input("Your name")

    user_message = st.text_area("Your message")

    button = st.form_submit_button("Submit", on_click=disable,
                                   disabled=st.session_state.disabled)
    if button:
        try:
            message = f"""From: {user_name}\n\n{user_message}"""
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
