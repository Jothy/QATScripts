import streamlit as st
import requests
from ScriptAPI import QAT_API as api

st.set_page_config(page_title='QATScripts', page_icon = 'Images\\QATScriptIcon.png', layout = 'centered', initial_sidebar_state = 'auto')


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
st.sidebar.button('Somatom_1_QA')



with st.form("my_form"):
    site=st.selectbox('Select site',('Clinical','Staging'))
    user = st.selectbox(
        'Select user',
        ('','Brendan Wright','Ben Cooper','Helen Gustafsson','Jothy Selvaraj', 'Jon Lee','Kim Legge','kasia Bobrowski', 'Nigel Freeman','Ravi Thura'))
    password = st.text_input("Enter your password", type="password")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("User:",user)


tryLogin()
if site=='Staging':
    st.write("Please review submitted results on  "+"https://canberra-staging.multileaf.ca")
else:
    st.write("Please review submitted results on  "+"https://canberra.multileaf.ca")











