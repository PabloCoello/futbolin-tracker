import streamlit as st
import pandas as pd
import numpy as np

st.title('Futbolin tracker')

page_names = ['Log in', 'Create new account']
page = st.radio('', page_names)

if page == 'Create new account':
    team = st.text_input('Name of your new team')
    password = st.text_input('Set Password')
else:
    team = st.text_input('Log in with the name of your team')
    password = st.text_input('Password')
