import pandas
import streamlit as st
# from email import send_email

st.header("Contact Us")

df = pandas.read_csv('topics.csv')

with st.form(key='email'):
    user_email = st.text_input("Your email address")
    for index, row in df.iterrows():
        data = st.selectbox(row['topic'])
    user_select = st.selectbox("What topic do you want to discuss?", data)

    user_message = st.text_area("Your message")
    # message = f"""
    # Subject: New email from {user_email}
    
    # From: {user_email}
    # {user_message}
# """
    button = st.form_submit_button("Submit")

    # if submit:
    # send_email(message)
    # st.info("Your email was sent successfully. \n Thank you for reaching out!")
