import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')

url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'

city_columns = []
city_names = []
for chunk in pd.read_csv(url, chunksize=100):
    city_columns = [col for col in chunk.columns if col != 'County']
    city_names = [col.replace("_", " ") for col in city_columns]
    break

columnz = st.selectbox("Choose a city", city_names)
columnz_index = city_columns.index(columnz.replace(" ", "_"))
numby = st.slider('Select a mile radius', 0, 500)

df_result = pd.DataFrame(columns=['County', columnz])
for chunk in pd.read_csv(url, usecols=['County', city_columns[columnz_index]], chunksize=100):
    df = chunk.loc[chunk[city_columns[columnz_index]] <= numby]
    df = df.sort_values(by=[city_columns[columnz_index]])
    df = df.drop_duplicates(subset=['County'], keep='first')
    df = df[['County', city_columns[columnz_index]]]
    df_result = pd.concat([df_result, df], ignore_index=True)

df_result
