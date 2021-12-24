import streamlit as st
import requests
import configparser
from ScriptAPI import QAT_API as api

config = configparser.ConfigParser()
config.read('Settings.properties')

st.set_page_config(page_title='QATScripts', page_icon = 'Images\\QATScriptIcon.png', layout = 'centered', initial_sidebar_state = 'auto')

siteNames=[]
siteURLs=[]
sites=dict(config.items('Sites'))
for key in sites:
    siteNames.append(key)
    siteURLs.append(sites[key])

users=config.get("General",'users')
users=users.split(',')

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

sites=config.items('Sites')


with st.form("my_form"):
    site=st.selectbox('Select site',siteNames)
    user = st.selectbox(
        'Select user',users)
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











