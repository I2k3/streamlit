import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(100000000, 2) / [50, 50] + [ 18.836, -97.1397],
    columns=['lat', 'lon'])

st.map(map_data)