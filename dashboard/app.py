import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

home_path = str(Path.home())

df = pd.read_csv('/Users/edmondukaj/big_data/homework-1/data/external/fifa_countries_audience.csv')

st.title("Stramlit")
st.image("hdm-logo.jpg")
st.header("Group K's Dashboard")

st.sidebar.header("Congrats, you've opened the sidebar!")
satisfation = st.sidebar.slider("How satisfied are you with this dashboard",0 , 10, 1)
st.sidebar.write("I rate this dashboard", satisfation, "/10")

st.dataframe(df)
