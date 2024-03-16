import requests

class NEOData:
    def __init__(self):
        self.data = []

    def load_data(self, api_key, start_date, end_date):
        base_url = "https://api.nasa.gov/neo/rest/v1/feed"
        next_url = base_url

        while next_url:
            response = requests.get(next_url, params={"start_date": start_date, "end_date": end_date, "api_key": api_key})
            
            if response.status_code == 200:
                neo_data = response.json()
                self.data.append(neo_data)
                
                # Get the link for the next page, if it exists
                next_url = neo_data.get("links", {}).get("next")
            else:
                print(f"Error: {response.status_code}")
                return None

        print("All NEO data loaded.")

if __name__ == "__main__":
    # API-Schlüssel
    api_key = "0m4vbWgrfhHHwXv7FS1U51c3TNxlFqZNcNCUuWs2"
    start_date = "2024-03-16"  # Beispielstartdatum
    end_date = "2024-03-23"  # Beispielenddatum

    neo_data_object = NEOData()
    neo_data_object.load_data(api_key, start_date, end_date)

    # Zugriff auf die geladenen Daten
    print(neo_data_object.data)
