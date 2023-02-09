import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')

url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'

col_dtypes = {'County': str}
col_dtypes.update({str(col): np.int32 for col in range(1, 5270)})

city_columns = None
city_names = None

def load_data(city_name, numby):
    chunk = pd.read_csv(url, dtype=col_dtypes, usecols=['County', city_name])
    df = chunk.loc[chunk[city_name] <= numby]
    df = df.sort_values(by=[city_name])
    df = df.drop_duplicates(subset=['County'], keep='first')
    df = df[['County', city_name]]
    return df

if city_columns is None:
    city_columns = pd.read_csv(url, nrows=0).columns
    city_names = [col.replace("_", " ") for col in city_columns if col != 'County']
    city_name = st.selectbox("Choose a city", city_names)
    numby = st.slider('Select a number', 0, 500, step=1, format='%d')

result = load_data(city_name, numby)
st.write(result)
