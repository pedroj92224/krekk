import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')

url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'

columnz = st.selectbox("Choose a city", range(1, 5270))
numby = st.slider('Select a mile radius', 0, 500)

usecols = ['County', str(columnz + 1)]
df = pd.read_csv(url, usecols=usecols, dtype={'County': str, str(columnz + 1): np.int32})
df = df.loc[df[str(columnz + 1)] <= numby]
df = df.sort_values(by=[str(columnz + 1)])
df = df.drop_duplicates(subset=['County'], keep='first')
df = df[['County', str(columnz + 1)]]
df