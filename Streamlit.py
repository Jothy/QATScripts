import streamlit as st

st.markdown("<h1 style='text-align: center; color: white;'>QATrack+ Scripts</h1>",unsafe_allow_html=True)
st.sidebar.title("Welcome to QAT+ Scripts")
st.sidebar.subheader('------QATrack+ automation------')

def test():
    st.write('testing...')

option = st.selectbox(
     'Select user',
    ('Brendan Wright','Ben Cooper','Helen Gustafsson','Jothy Selvaraj', 'Jon Lee','Kim Legge','kasia Bobrowski', 'Nigel Freeman','Ravi Thura'))

st.write('You selected:', option)

st.error("Do you really, really, wanna do this?")
if st.button("Yes I'm ready to rumble"):
    test()




