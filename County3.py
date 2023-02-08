import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')

url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'

col_dtypes = {'County': str}
col_dtypes.update({str(col): np.int32 for col in range(1, 5270)})

df = pd.read_csv(url, usecols=['County'] + city_columns, dtype=col_dtypes)
city_columns = [col for col in df.columns if col != 'County']
city_names = [col.replace("_", " ") for col in city_columns]
columnz = st.selectbox("Choose a city", city_names)
column_index = city_columns.index(columnz.replace(" ", "_"))
numby = st.slider('Select a mile radius', 0, 500)

df = df.loc[df[city_columns[column_index]] <= numby]
df = df.sort_values(by=[city_columns[column_index]])
df = df.drop_duplicates(subset=['County'], keep='first')
df = df[['County', city_columns[column_index]]]
st.dataframe(df)
