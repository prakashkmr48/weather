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
# Markdown documentation for the Weather Data API
weather_api_documentation = """
# Weather Data API Documentation

## Introduction

The Weather Data API provides real-time weather information for a given location. It leverages the OpenWeatherMap API to fetch weather data based on the provided city name. This documentation outlines how to use the API, its endpoints, and the expected response.

... (Include the entire documentation here)

## Rate Limiting

- OpenWeatherMap may impose rate limits on API usage for free or trial API keys. Refer to OpenWeatherMap's documentation for rate limit details.

## Conclusion

The Weather Data API allows you to access real-time weather data for a specified city. By following the guidelines provided in this documentation, you can integrate weather information into your applications or services with ease.
"""

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

# Display the documentation when a button is clicked
    if st.button("Show API Documentation"):
        st.markdown(weather_api_documentation)


if __name__ == "__main__":
    main()
