from flask import Flask, render_template
from api import get_neo_data

app = Flask(__name__, static_url_path='/', static_folder='web', template_folder='web')

@app.route("/")
def indexPage():
    # API-Schlüssel
    api_key = "0m4vbWgrfhHHwXv7FS1U51c3TNxlFqZNcNCUuWs2"
    start_date = "2024-03-16"  # Beispielstartdatum
    end_date = "2024-03-23"  # Beispielenddatum
    neo_data = get_neo_data(api_key, start_date, end_date)

    # Wetterdaten an HTML-Seite übergeben
    return render_template("index.html", neo_data=neo_data)

if __name__ == "__main__":
    app.run(debug=True)