import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')

url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'

city_names = [col.replace("", " ") for col in pd.read_csv(url, nrows=0).columns if col != 'County']
columnz = st.selectbox("Choose a city", city_names)
columnz = columnz.replace(" ", "")
numby = st.slider('Select a mile radius', 0, 500)

usecols = ['County', columnz]
df_chunk = pd.read_csv(url, usecols=usecols, dtype={'County': str, columnz: np.int32}, chunksize=10**5)
df = pd.concat([chunk.loc[chunk[columnz] <= numby] for chunk in df_chunk], ignore_index=True)
df = df.sort_values(by=[columnz])
df = df.drop_duplicates(subset=['County'], keep='first')
df = df[['County', columnz]]
df
