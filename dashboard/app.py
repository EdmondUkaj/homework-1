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

c = alt.Chart(df).mark_point().encode(
    x='tv_audience_share:Q',
    y='gdp_weighted_share:Q',
    size=alt.Size('population_share',
                title='Population'),
    tooltip=['tv_audience_share', 'gdp_weighted_share']
).properties(
    title='World Cup 2010 – Shares',
).interactive()

st.altair_chart(c, use_container_width=True)

st.write("fourth chart")

c = alt.Chart(df).mark_point().encode(
    x='tv_audience_share:Q',
    y='gdp_weighted_share:Q',
    tooltip=['tv_audience_share', 'gdp_weighted_share']
).properties(
    title='World Cup 2010 – Shares',
).interactive()

st.altair_chart(c, use_container_width=True)

st.write("fifth chart")


source = pd.DataFrame(df.confederation.value_counts())
source = source.reset_index()
source.rename(columns={"index": "category", "confederation": "value"}, inplace=True)
source

c = alt.Chart(source).mark_arc.encode(
    theta=alt.Theta("value:Q", stack=True), 
    color=alt.Color("category:N", legend=None)
).properties(
    title='FIFA Confederations',
)

pie = c.mark_arc(outerRadius=100)
text = c.mark_text(radius=130, size=12).encode(text="category:N")

pie + text

st.altair_chart(c, use_container_width=True)


