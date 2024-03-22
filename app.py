from flask import Flask, jsonify, render_template, request
from model.model import load_neo_data, preprocess_data, train_model, evaluate_model, save_feature_importance_plot, predict_danger, model

# Execute code from model.py
neo_data = load_neo_data()
df = preprocess_data(neo_data)
model, X_test, y_test = train_model(df)
accuracy = evaluate_model(model, X_test, y_test)
print("Accuracy:", accuracy)
save_feature_importance_plot(model, df, 'frontend/static/feature_importance_plot.png')

# Initialize Flask app
app = Flask(__name__, static_url_path='/', static_folder='frontend', template_folder='frontend/build')

@app.route('/')
@app.route('/index.html')
def main_page():
    return render_template('index.html')

@app.route('/model.html')
def model_page():
    return render_template('model.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Get form data
    absolute_magnitude = float(data['absolute-magnitude'])
    min_diameter = float(data['min-diameter'])
    max_diameter = float(data['max-diameter'])
    miss_distance = float(data['miss-distance'])
    relative_velocity = float(data['relative-velocity'])

    # Predict danger level
    danger_level = predict_danger(model, absolute_magnitude, min_diameter, max_diameter, miss_distance, relative_velocity)

    danger_level_str = str(danger_level)

    # Return prediction result
    if danger_level:
        prediction_message = "Your asteroid is dangerous!"
    else:
        prediction_message = "Planet Earth is safe."

    return jsonify({'result': prediction_message})


if __name__ == "__main__":
    app.run(debug=True)
