from flask import Flask, render_template
from frontend.api import get_neo_data, save_to_mongodb
from model.model import load_neo_data, preprocess_data, train_model, evaluate_model, save_feature_importance_plot

# Execute code from model.py
print("Start Data load from API...")

api_key = "0m4vbWgrfhHHwXv7FS1U51c3TNxlFqZNcNCUuWs2"
neo_data = get_neo_data(api_key)
print("Data loaded from API")

save_to_mongodb(neo_data)

# Execute code from model.py
print("Start Data load from API...")

api_key = "0m4vbWgrfhHHwXv7FS1U51c3TNxlFqZNcNCUuWs2"
neo_data = load_neo_data(api_key)
print("Data loaded from API")

save_to_mongodb(neo_data)

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


if __name__ == "__main__":
    app.run(debug=True)
