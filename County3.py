import pandas as pd
import streamlit as st

st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')

url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'

col_dtypes = {'County': str}
col_dtypes.update({str(col): 'Int32' for col in range(1, 5270)})

df = pd.read_csv(url, dtype=col_dtypes)
city_columns = [col for col in df.columns if col != 'County']
city_names = [col.replace("_", " ") for col in city_columns]
columnz = st.selectbox("Choose a city", city_names)
numby = st.slider('Select a mile radius', 0, 500)

df2 = df[['County', columnz]]
df3 = df2[df2[columnz] <= numby]
df3 = df3.sort_values(by=[columnz])
df3 = df3.drop_duplicates(subset=['County'], keep='first')
st.write(df3)
