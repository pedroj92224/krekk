import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')

url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'

# get the column names
with open(url) as f:
    first_line = f.readline()
column_names = first_line.strip().split(',')

columnz = st.selectbox("Choose a city", column_names[1:])
numby = st.slider('Select a mile radius', 0, 500)

# set usecols based on user input
usecols = ['County', columnz]

# read the csv in chunks
df_chunks = pd.read_csv(url, usecols=usecols, chunksize=100000, dtype={'County': str, columnz: np.int32})
df = pd.concat([chunk for chunk in df_chunks])

df = df.loc[df[columnz] <= numby]
df = df.sort_values(by=[columnz])
df = df.drop_duplicates(subset=['County'], keep='first')
df = df[['County', columnz]]
df
