import streamlit as st
import requests
from ScriptAPI import QAT_API as api

url = "https://canberra-staging.multileaf.ca/api"
timeout = 5
token = "754303d15f0cd9c49a8606a02a741eac5bf2d1c9"
auth = {"Authorization": "Token %s" % token}


def tryLogin():
    resp = requests.get(url, headers=auth)
    if 200 <= resp.status_code <= 299:
        st.write('Login Success!')
    else:
        st.error('Login failed!')


st.title("QATrack+ Scripts")
st.sidebar.title("Welcome to QAT+ Scripts")
st.sidebar.subheader('------QATrack+ automation------')

site=st.selectbox('Select site',('Clinical','Staging'))

option = st.selectbox(
     'Select user',
    ('','Brendan Wright','Ben Cooper','Helen Gustafsson','Jothy Selvaraj', 'Jon Lee','Kim Legge','kasia Bobrowski', 'Nigel Freeman','Ravi Thura'))

password = st.text_input("Enter your password", type="password")

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)


tryLogin()










