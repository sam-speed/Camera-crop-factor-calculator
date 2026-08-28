from conversions import apply_crop, apply_adapter, classify_focal_length, aperture_ranking
from data import crop_factor, crop_adapters, greetings, focal_length_available, focal_aperture_available
from usage_data import save_usage_data, mark_new_job_clicked
import streamlit as st
import random

def greet(greetings_list):
    greeting_selected = random.choice(greetings_list)
    return (greeting_selected)

def convertions(sensor_name, adapter_name, focal_length_input, focal_aperture_input):
    focal_length_result = apply_adapter(adapter_name, apply_crop(sensor_name, focal_length_input))
    aperture_real = apply_adapter(adapter_name, focal_aperture_input)
    aperture_equivalent = apply_adapter(adapter_name, apply_crop(sensor_name, focal_aperture_input))
    return (focal_length_result, aperture_real, aperture_equivalent)

def run():
    st.image("banner.png", use_container_width=True)
    if "show_results" not in st.session_state:
        st.session_state.show_results = False
    if "data_saving_state" not in st.session_state:
            st.session_state.data_saving_state = False
    if st.session_state.show_results == False:
        if "greeting" not in st.session_state:
                st.session_state.greeting=greet(greetings)
        st.markdown(f"## {st.session_state.greeting}")
        col1, col2, col3, col4=st.columns(4)
        col1.markdown("### Sensor:")
        st.session_state.sensor_name=col1.selectbox(
            label="",
            options = list(crop_factor.keys()),
            format_func = lambda tipo: f"{tipo}-{crop_factor[tipo]}x"
        )

        col2.markdown("### Adapter:")
        st.session_state.adapter_name=col2.selectbox(
            label="",
            options = tuple(crop_adapters.keys()),
            format_func = lambda tipo: f"{tipo}-{crop_adapters[tipo][0]}"
        )

        col3.markdown("### Length:")
        st.session_state.focal_length_input = col3.select_slider(
             label="",
             options = focal_length_available,
             value=35
        )
        
        col4.markdown("### Aperture:")
        st.session_state.focal_aperture_input = col4.select_slider(
             label = "",
             options = focal_aperture_available,
             value=4.0
        )

        if st.button("Run"):
            results = convertions(st.session_state.sensor_name, st.session_state.adapter_name, st.session_state.focal_length_input, st.session_state.focal_aperture_input)
            st.session_state.length_result = results[0]
            st.session_state.aperture_result = results[1]
            st.session_state.aperture_equivalent = results[2]
            st.session_state.show_results = True
            st.rerun() 
    else:
        st.toast("Your data will be saved anonymously in the app's 'Usage Data' section.")
        st.markdown("## Results:")
        st.markdown(f"### Your lens: {st.session_state.length_result}mm, f{st.session_state.aperture_result} (f{st.session_state.aperture_equivalent} full frame equivalent)")
        length_classification=classify_focal_length(st.session_state.length_result)
        st.markdown(f"### Your lens is a {length_classification} lens\n")
        ranking = aperture_ranking(st.session_state.aperture_equivalent)
        st.markdown(f"### Your Low Light Ranking is {ranking}/5")
        if st.session_state.data_saving_state == False:
            st.session_state.request_timestamp = save_usage_data(st.session_state.sensor_name, st.session_state.adapter_name, st.session_state.focal_length_input, st.session_state.focal_aperture_input, st.session_state.length_result, st.session_state.aperture_result, st.session_state.aperture_equivalent, length_classification, ranking)
            st.session_state.data_saving_state = True
        if st.button("New job"):
            mark_new_job_clicked(st.session_state.request_timestamp)
            st.session_state.show_results=False
            st.session_state.data_saving_state = False
            st.rerun()
