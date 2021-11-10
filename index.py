import streamlit as st
import pandas as pd
import datetime as dt
import numpy as np
from dateutil.relativedelta import relativedelta
import re

st.title("TARA en Chile / Sampling")
def dms2dd(s):
    # example: s = """0°51'56.29"S"""
    degrees, minutes = re.split('[°]', s)
    dd = float(degrees) + float(minutes)/60;
    return -dd


st.subheader("Type of Sampling")

df = pd.read_csv("data/data_tara_orden.csv", index_col=0, sep="\t")

#Seleccionar rango
#datefilter = st.slider('Days', , 23, 17)



