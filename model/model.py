import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from api import get_neo_data, save_to_mongodb

# API-Schlüssel
api_key = "0m4vbWgrfhHHwXv7FS1U51c3TNxlFqZNcNCUuWs2"
start_date = "2024-03-16"
end_date = "2024-03-19"

print("Start Data load from API...")
neo_data = get_neo_data(api_key, start_date, end_date)
print("Data loaded from API")

save_to_mongodb(neo_data)

# Extrahiere relevante Merkmale aus den API-Daten
features = []
labels = []

for data in neo_data:
    near_earth_objects = data.get('near_earth_objects', {})
    for date, asteroids in near_earth_objects.items():
        for asteroid in asteroids:
            features.append([
                asteroid['absolute_magnitude_h'],
                asteroid['estimated_diameter']['kilometers']['estimated_diameter_min'],
                asteroid['estimated_diameter']['kilometers']['estimated_diameter_max'],
                asteroid['close_approach_data'][0]['miss_distance']['kilometers'],
                asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']
            ])
            labels.append(asteroid['is_potentially_hazardous_asteroid'])

# Erstelle einen DataFrame aus den extrahierten Merkmalen und Labels
df = pd.DataFrame(features, columns=['absolute_magnitude_h', 'min_diameter_km', 'max_diameter_km', 'miss_distance_km', 'relative_velocity_km_hour'])
df['is_potentially_hazardous'] = labels

# Aufteilung der Daten in Trainings- und Testsets
X_train, X_test, y_train, y_test = train_test_split(df.drop('is_potentially_hazardous', axis=1), df['is_potentially_hazardous'], test_size=0.2, random_state=42)

# Modelltraining
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Vorhersage auf dem Testset
predictions = model.predict(X_test)

# Evaluierung des Modells
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
