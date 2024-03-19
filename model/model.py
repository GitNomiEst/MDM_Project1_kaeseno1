import random
import pandas as pd
import matplotlib.pyplot as plt

from flask import Flask, jsonify, request
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from frontend.api import get_neo_data, save_to_mongodb
from frontend import api


# API Key
api_key = "0m4vbWgrfhHHwXv7FS1U51c3TNxlFqZNcNCUuWs2"
start_date = "2024-03-16"
end_date = "2024-03-19"

print("Start Data load from API...")
neo_data = get_neo_data(api_key, start_date, end_date)
print("Data loaded from API")

save_to_mongodb(neo_data)

# Extract relevant features from the API data
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

# Create a DataFrame from the extracted features and labels
df = pd.DataFrame(features, columns=['absolute_magnitude_h', 'min_diameter_km', 'max_diameter_km', 'miss_distance_km', 'relative_velocity_km_hour'])
df['is_potentially_hazardous'] = labels

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('is_potentially_hazardous', axis=1), df['is_potentially_hazardous'], test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediction on the test set
predictions = model.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Plot feature importance
feature_importances = model.feature_importances_
plt.bar(df.columns[:-1], feature_importances)
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Feature Importance')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('frontend/pic/feature_importance_plot.png')


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Perform the calculation based on the form data
    # For demonstration purposes, let's just return a random prediction
    prediction = "Potentially Hazardous" if random.random() < 0.5 else "Not Hazardous"

    return jsonify({'result': prediction})

if __name__ == '__main__':
    app.run(debug=True)
