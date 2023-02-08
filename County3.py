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

# Read only the header row of the CSV file
df = pd.read_csv(url, dtype=col_dtypes, nrows=0)
if city_columns is None:
    city_columns = [col for col in df.columns if col != 'County']
    city_names = [col.replace("_", " ") for col in city_columns]

columnz = st.selectbox("Choose a city", city_names)
numby = st.slider('Select a mile radius', 0, 500)

# Filter only the necessary rows from the CSV file
df = pd.read_csv(url, usecols=['County', columnz], dtype=col_dtypes, engine='c')

df = df.loc[df[columnz] <= numby]
df = df.sort_values(by=[columnz])
df = df.drop_duplicates(subset=['County'], keep='first')
df = df[['County', columnz]]
st.write(df)
