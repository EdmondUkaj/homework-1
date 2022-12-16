import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

home_path = str(Path.home())

df = pd.read_csv('/Users/edmondukaj/big_data/homework-1/data/external/fifa_countries_audience.csv')

st.title("Streamlit")
st.image("hdm-logo.jpg")
st.header("Group K's Dashboard")

st.sidebar.header("Congrats, you've opened the sidebar!")
satisfation = st.sidebar.slider("How satisfied are you with this dashboard",0 , 10, 1)
st.sidebar.write("I rate this dashboard", satisfation, "/10")

st.dataframe(df)

st.write("First chart")

c = alt.Chart(df).mark_bar().encode(
        x=('confederation'),
        y=alt.Y('count(confederation)')
)
st.altair_chart(c, use_container_width=True)

st.write("Second Chart")

c = alt.Chart(df).mark_bar().encode(
    x=alt.X('confederation',
            sort='-y',
            axis=alt.Axis(title="Confederations", 
                          titleAnchor="start", 
                          labelAngle=0)),
    y=alt.Y('count(confederation)', 
            axis=alt.Axis(title = "Count", 
                          titleAnchor="end")),
    color= alt.Color('count(confederation)', 
                     legend=alt.Legend(title="Count"))
).properties(
    title='FIFA Confederations',
    width=350,
    height=150
)
st.altair_chart(c, use_container_width=True)

st.write("third chart")



st.write("fourth chart")

