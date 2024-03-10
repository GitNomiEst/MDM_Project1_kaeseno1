from flask import Flask, render_template
from flask.helpers import send_file
from api import get_insight_weather

app = Flask(__name__, static_url_path='/', static_folder='web', template_folder='web')

@app.route("/")
def indexPage():
    # API-Schlüssel
    api_key = "0m4vbWgrfhHHwXv7FS1U51c3TNxlFqZNcNCUuWs2"
    weather_data = get_insight_weather(api_key)

    # Wetterdaten an HTML-Seite übergeben
    return render_template("index.html", weather_data=weather_data)