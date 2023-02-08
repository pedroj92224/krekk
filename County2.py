import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')

url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'
col_dtypes = {'County': str}
col_dtypes.update({col: np.int32 for col in range(1, 5270)})

df_chunks = pd.read_csv(url, chunksize=1000, dtype=col_dtypes)
df = pd.concat(df_chunks)


columnz = st.selectbox("Choose a city", df.columns.drop('County'))

numby = st.slider(
    'Select a mile radius',
    0, 500)

df = df.query(f"{columnz} <= {numby}")
df = df.sort_values(by=[columnz])
df = df.drop_duplicates(subset=['County'], keep='first')
df 
