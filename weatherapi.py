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
  
# Weather Data API Documentation

## Introduction
The Weather Data API provides real-time weather information for a given location. It leverages the OpenWeatherMap API to fetch weather data based on the provided city name. This documentation outlines how to use the API, its endpoints, and the expected response.

## Getting Started

### Base URL

The base URL for accessing the Weather Data API is:
```
https://api.openweathermap.org/data/2.5/weather
```

### API Key

To use this API, you need an API key from OpenWeatherMap. Replace `"YOUR_API_KEY"` in the requests with your actual API key. You can obtain a free API key by signing up at [OpenWeatherMap](https://openweathermap.org/).

## Endpoints

### Get Weather Data

#### Endpoint: `/api/get-weather`

- **HTTP Method:** GET
- **Description:** Retrieve weather data for a specific city.
- **Parameters:**
  - `q` (string, required): The name of the city for which you want to retrieve weather data.
  - `appid` (string, required): Your OpenWeatherMap API key.
  - `units` (string, optional): Unit system for temperature. Use `"metric"` for Celsius or `"imperial"` for Fahrenheit (default: `"metric"`).

#### Example Request:
```http
GET /api/get-weather?q=London&appid=YOUR_API_KEY
```

#### Response:

- **Status Code:** 200 (OK) if successful, other status codes if there is an error.
- **Response Format:** JSON

##### Successful Response (Status Code: 200):
```json
{
  "coord": {
    "lon": -0.1257,
    "lat": 51.5085
  },
  "weather": [
    {
      "id": 801,
      "main": "Clouds",
      "description": "few clouds",
      "icon": "02d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 21.76,
    "feels_like": 21.32,
    "temp_min": 21.19,
    "temp_max": 22.36,
    "pressure": 1015,
    "humidity": 45
  },
  "visibility": 10000,
  "wind": {
    "speed": 2.91,
    "deg": 41,
    "gust": 2.64
  },
  "clouds": {
    "all": 22
  },
  "dt": 1632178609,
  "sys": {
    "type": 2,
    "id": 2031932,
    "country": "GB",
    "sunrise": 1632139032,
    "sunset": 1632182282
  },
  "timezone": 3600,
  "id": 2643743,
  "name": "London",
  "cod": 200
}
```

##### Error Response:
- If the city name is not found or other errors occur, you will receive a JSON response with an appropriate error message and status code.

## Usage Example

### Python Example Code:

```python
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
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city_name = input("Enter the name of the city: ")

    weather_data = get_weather(api_key, city_name)

    if weather_data:
        print(f"Weather in {city_name}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Unable to fetch weather data.")

if __name__ == "__main__":
    main()
```

## Error Handling

- In case of errors, the API will return appropriate HTTP status codes along with error messages in the JSON response.

## Rate Limiting

- OpenWeatherMap may impose rate limits on API usage for free or trial API keys. Refer to OpenWeatherMap's documentation for rate limit details.

## Conclusion

The Weather Data API allows you to access real-time weather data for a specified city. By following the guidelines provided in this documentation, you can integrate weather information into your applications or services with ease.
