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

df_list = []
for chunk in pd.read_csv(url, dtype=col_dtypes, chunksize=1000):
    if city_columns is None:
        city_columns = [col for col in chunk.columns if col != 'County']
        city_names = [col.replace("_", " ") for col in city_columns]
        columnz = st.selectbox("Choose a city", city_names)
        number = st.number_input('Insert a number')
        

    df = chunk.loc[chunk[columnz] <= number]
    df = df.sort_values(by=[columnz])
    df = df.drop_duplicates(subset=['County'], keep='first')
    df = df[['County', columnz]]
    df_list.append(df)

result = pd.concat(df_list)
st.write(result)
