import requests
from pymongo import MongoClient

def get_neo_data(api_key, start_date, end_date):
    x=0
    print(x)

    all_data = []

    base_url = "https://api.nasa.gov/neo/rest/v1/feed"
    next_url = base_url
    print(next_url)
    while x<=10:
        print("1")
        #response = requests.get(next_url, params={"start_date": start_date, "end_date": end_date, "api_key": api_key})
        response = requests.get(next_url, params={"api_key": api_key})
        x+=1
        print(response.status_code)
        if response.status_code == 200:
            neo_data = response.json()
            all_data.append(neo_data)
            
            # Get the link for the next page, if it exists
            next_url = neo_data.get("links", {}).get("next")
        else:
            print(f"Error: {response.status_code}")
            return None

    print("All NEO data loaded.")
    return all_data

def save_to_mongodb(data):
    client = MongoClient('localhost', 27017)  # Assuming MongoDB is running on localhost
    db = client['nasa']
    collection = db['nasa']
    collection.insert_many(data)
    print("Data saved to MongoDB.")

if __name__ == "__main__":
    # API Key
    api_key = "0m4vbWgrfhHHwXv7FS1U51c3TNxlFqZNcNCUuWs2"
    start_date = "2024-03-16"  # Example start date
    end_date = "2024-03-23"  # Example end date
    neo_data = get_neo_data(api_key, start_date, end_date)
    
    if neo_data:
        save_to_mongodb(neo_data)
