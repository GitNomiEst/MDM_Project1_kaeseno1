from flask import Flask, render_template

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
