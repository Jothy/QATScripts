import streamlit as st

st.title('QAT+ Scripts')
st.sidebar.title("Welcome to QAT+ Scripts")
st.sidebar.subheader('')

option = st.selectbox(
     'Select user',
    ('Jothy Selvaraj', 'Jon Lee', 'Ravi Thura','Helen Gustafsson','Kim Legge','kasia Bobrowski','Brendan Wright','Nigel Freeman','Ben Cooper'))

st.write('You selected:', option)