import streamlit as st
import requests
from ScriptAPI import QAT_API as api

url = "https://canberra-staging.multileaf.ca/api"
timeout = 5
token = "00754303d15f0cd9c49a8606a02a741eac5bf2d1c9"
auth = {"Authorization": "Token %s" % token}


def tryLogin():
    request = requests.get(url, headers=auth)
    if(request.json()['detail']!='invalid token'):
        st.success('Connected to '+url)
    else:
        st.error("Login failed")

st.markdown("<h1 style='text-align: center; color: white;'>QATrack+ Scripts</h1>",unsafe_allow_html=True)
st.sidebar.title("Welcome to QAT+ Scripts")
st.sidebar.subheader('------QATrack+ automation------')

def test():
    st.write('testing...')

option = st.selectbox(
     'Select user',
    ('','Brendan Wright','Ben Cooper','Helen Gustafsson','Jothy Selvaraj', 'Jon Lee','Kim Legge','kasia Bobrowski', 'Nigel Freeman','Ravi Thura'))

password = st.text_input("Enter your password", type="password")

tryLogin()










