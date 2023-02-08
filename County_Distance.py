import pandas as pd
import streamlit as st
from collections import defaultdict

st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')
url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'
col_dtypes = {col: str for col in range(0, 1)}
col_dtypes.update({col: int for col in range(1, 5270)})
df = pd.read_csv(url, dtype=col_dtypes)
column_names = df.columns
for i in range(1, len(column_names)):
    dtypes[i] = int
df = pd.read_csv(url, dtype=dict((column_names[i], dtypes[i]) for i in range(len(column_names))))
dfa = df.loc[ :, df.columns != 'County']

columnz = st.selectbox("Choose a city", dfa.columns)

numby = st.slider(
    'Select a mile radius',
    0, 500)


df2 = pd.DataFrame(df, columns = ['County', columnz])
df3 = df2.loc[df2[columnz] <= numby]
df4 = df3.sort_values(by=[columnz])
df5 = df4.drop_duplicates(subset=['County'], keep='first')
df6 = pd.DataFrame(df5, columns = ['County', columnz])
df6
