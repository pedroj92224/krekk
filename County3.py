import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')

url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'

col_dtypes = {'County': str}
col_dtypes.update({str(col): np.int32 for col in range(1, 5270)})

city_columns = pd.read_csv(url, nrows=0).columns.drop("County")
city_names = [col.replace("_", ", ") for col in city_columns]
selected_city = st.selectbox("Choose a city", city_names)
numby = st.slider('Select a mile radius', 0, 500)

df = pd.read_csv(url, dtype=col_dtypes, usecols=["County", selected_city.replace(", ", "_")], chunksize=1000)
df = pd.concat([chunk.loc[chunk[selected_city.replace(", ", "_")] <= numby] for chunk in df])
df = df.sort_values(by=[selected_city.replace(", ", "_")])
df = df.drop_duplicates(subset=['County'], keep='first')
df = df[['County', selected_city.replace(", ", "_")]]
st.write(df)
