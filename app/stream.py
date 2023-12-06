import streamlit as st
import plotly.express as px
from utils import get_data
import requests

st.title("Weather Forecast For Next 5 Days")
place = st.text_input('Place: ')
days = st.slider(
    'Select a range of values',
    1, 5)
option = st.selectbox(
    'Select Data to View',
    ('Temperature', 'Sky'))
st.subheader(f"Temperature for the next {days} days in {place}")

if place:
    try:
        #get the temp/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [dict['main']['temp'] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(
                x=dates,
                y= temperature,
                labels={"x": "Date", "y": "temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {'Rain': 'static\css\images\rain.png', 'Clouds': 'static\css\images\cloud.png', 'Clear': 'static\css\images\clear.png', 'Snow': 'static\css\images\snow.png'}
            sky_condition = [dict['weather'][0]['main'] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_condition]
            st.image(image_path, width=100)
    except KeyError:
        st.write("Please enter correct name of the city")
