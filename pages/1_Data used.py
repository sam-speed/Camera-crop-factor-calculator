import pandas as pd
import streamlit as st
from data import crop_factor, crop_adapters, length_classification

st.markdown("# Data used:")
st.markdown("*Crop factor used for the convertions*")
st.markdown("## Sensor crop:")
st.dataframe(crop_factor, use_container_width=True)
st.markdown("## Adapters crop:")
st.dataframe(crop_adapters, use_container_width=True)