import requests

def get_insight_weather(api_key):
    base_url = "https://api.nasa.gov/insight_weather/"
    params = {
        "api_key": api_key,
        "feedtype": "json",
        "ver": "1.0"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    # API-Schlüssel
    api_key = "0m4vbWgrfhHHwXv7FS1U51c3TNxlFqZNcNCUuWs2"
    weather_data = get_insight_weather(api_key)

    if weather_data:
        print("Weather data:")
        print(weather_data)


def get_insight_weather(api_key):
    base_url = "https://api.nasa.gov/insight_weather/"
    params = {
        "api_key": api_key,
        "feedtype": "json",
        "ver": "1.0"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")
        return None