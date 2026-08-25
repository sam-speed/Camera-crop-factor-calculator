import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("usage_data.csv")

st.markdown("# Analytics")
st.markdown("*Usage statistics*")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_conversions = len(df)
    st.metric("Total conversions", total_conversions)

with col2:
    top_sensor = df["sensor_name"].mode()[0].replace("_", " ").title()
    st.metric("Most used sensor", top_sensor)

with col3:
    bokeh_ranking = round(df["bouque_ranking"].mean(), 1)
    st.metric("Average bokeh score", f"{bokeh_ranking} / 5")

with col4:
    conversions = int(df["new_job_clicked"].sum())
    st.metric("Multiple conversions:", f"{conversions}/{total_conversions}")

st.divider()

pie_settings = px.pie(
        df,
        names="sensor_name",
        hole=0.5
    )
col1, col2 = st.columns(2)

with col1:
    st.subheader("Lens type:")
    st.plotly_chart(pie_settings, use_container_width=True)

with col2:
    st.markdown("## Sensor type:")
    st.plotly_chart(pie_settings, use_container_width=False)
