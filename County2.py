import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')

url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'
col_dtypes = {'County': str}
col_dtypes.update({col: np.int32 for col in range(1, 5270)})

df_chunks = pd.read_csv(url, chunksize=100, dtype=col_dtypes)
df = pd.concat(df_chunks)


columnz = st.selectbox("Choose a city", df.columns.drop('County'))

numby = st.slider(
    'Select a mile radius',
    0, 500)

df2 = pd.DataFrame(df, columns = ['County', columnz])
if df2.get(columnz) is not None:
    df3 = df2.loc[df2[columnz] <= numby]
    df4 = df3.sort_values(by=[columnz])
    df5 = df4.drop_duplicates(subset=['County'], keep='first')
    df6 = pd.DataFrame(df5, columns = ['County', columnz])
    df6
else:
    st.error('The selected city does not exist in the DataFrame')
