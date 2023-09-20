import streamlit as st
import requests


def get_weather(api_key, city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",  # Change to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def main():
    st.title("Weather App")

    api_key = "eddfcb2e5368ad6034a63479dd015c5b"  # Replace with your OpenWeatherMap API key
    city_name = st.text_input("Enter the name of the city:")

    if st.button("Get Weather"):
        weather_data = get_weather(api_key, city_name)

        if weather_data:
            st.write(f"Weather in {city_name}:")
            st.write(f"Temperature: {weather_data['main']['temp']}°C")
            st.write(f"Description: {weather_data['weather'][0]['description']}")
            st.write(f"Humidity: {weather_data['main']['humidity']}%")
            st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        else:
            st.write("Unable to fetch weather data.")


if __name__ == "__main__":
    main()
  
api_documentation = """
# Weather Data API Documentation

## Introduction

The Weather Data API provides real-time weather information for a given location. It leverages the OpenWeatherMap API to fetch weather data based on the provided city name. This documentation outlines how to use the API, its endpoints, and the expected response.

## Getting Started

### Base URL

The base URL for accessing the Weather Data API is:
