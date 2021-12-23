import streamlit as st
import requests

url = "https://canberra-staging.multileaf.ca/api"
timeout = 5
token = "00754303d15f0cd9c49a8606a02a741eac5bf2d1c9"
auth = {"Authorization": "Token %s" % token}

request = requests.get(url,headers=auth)
print(request)

try:
	request = requests.get(url, timeout=timeout,headers=auth)
	st.success('Connected to '+url)
except (requests.ConnectionError, requests.Timeout) as exception:
	st.error("Could not connect to ",url)


st.markdown("<h1 style='text-align: center; color: white;'>QATrack+ Scripts</h1>",unsafe_allow_html=True)
st.sidebar.title("Welcome to QAT+ Scripts")
st.sidebar.subheader('------QATrack+ automation------')

def test():
    st.write('testing...')

option = st.selectbox(
     'Select user',
    ('','Brendan Wright','Ben Cooper','Helen Gustafsson','Jothy Selvaraj', 'Jon Lee','Kim Legge','kasia Bobrowski', 'Nigel Freeman','Ravi Thura'))

password = st.text_input("Enter your password", type="password")

if st.button("Login"):
    st.write(password)






