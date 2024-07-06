import streamlit as st
import send_email as se

st.header("Contact Me")


with st.form(key="input_email"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        se.send_email(user_email, message)
        st.info("Your message was sending successfully")



