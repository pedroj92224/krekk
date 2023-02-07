import pandas as pd
import streamlit as st


st.set_page_config(page_title='Distance Tool')
st.header('Counties Within Mile Radius')
st.subheader('Choose a city:')
url = 'https://media.githubusercontent.com/media/pedroj92224/krekk/master/Distances_Offline.csv'
df = pd.read_csv(url, on_bad_lines='skip')
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
