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
for chunk in pd.read_csv(url, dtype=col_dtypes, chunksize=100):
    if city_columns is None:
        city_columns = [col for col in chunk.columns if col != 'County']
        city_names = [col.replace("_", " ") for col in city_columns]
        columnz = st.selectbox("Choose a city", city_names)
        columnz = city_columns[city_names.index(columnz)]
        numby = st.slider('Select a mile radius', 0, 500)
    chunk = chunk.loc[chunk[columnz] <= numby]
    chunk = chunk.sort_values(by=[columnz])
    chunk = chunk.drop_duplicates(subset=['County'], keep='first')
    chunk = chunk[['County', columnz]]
    st.write(chunk)
