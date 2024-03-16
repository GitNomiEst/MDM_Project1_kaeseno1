import requests

def get_neo_data(api_key, start_date, end_date):
    base_url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        neo_data = response.json()
        print("NEO data:")
        print(neo_data)
        return neo_data
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    # API-Schlüssel
    api_key = "0m4vbWgrfhHHwXv7FS1U51c3TNxlFqZNcNCUuWs2"
    start_date = "2024-03-16"  # Beispielstartdatum
    end_date = "2024-03-23"  # Beispielenddatum
    neo_data = get_neo_data(api_key, start_date, end_date)
