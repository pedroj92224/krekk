import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')

url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'

city_columns = None
city_names = None

# Read only the first chunk of the CSV file to get the city columns
for chunk in pd.read_csv(url, chunksize=1000):
    if city_columns is None:
        city_columns = [col for col in chunk.columns if col != 'County']
        city_names = [col.replace("_", " ") for col in city_columns]
        break

columnz = st.selectbox("Choose a city", city_names)
numby = st.slider('Select a mile radius', 0, 500)

# Read only the selected city column and the County column, with the dtype of the city column set to int32
df = pd.read_csv(url, usecols=['County', columnz], dtype={columnz: np.int32})

# Filter the rows where the value of the selected city column is less than or equal to the selected radius
df = df.loc[df[columnz] <= numby]
df = df.sort_values(by=[columnz])
df = df.drop_duplicates(subset=['County'], keep='first')
df = df[['County', columnz]]

st.write(df)
