import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

home_path = str(Path.home())

df = pd.read_csv('fifa_countries_audience.csv')

