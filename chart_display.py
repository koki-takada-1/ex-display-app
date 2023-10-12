import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('usd.csv')
fig = px.line(df,x='date',y=['tts','ttb'],title="USD 4-Moth Chart")
st.plotly_chart(fig, use_container_width=True)