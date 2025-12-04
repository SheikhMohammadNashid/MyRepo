from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "a93F7cP1eD84mQ2sV0rB9xL7tW6yK3Z" #use your api key this key won't work

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None

    if request.method == 'POST':
        city = request.form.get("city")
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}"
            response = requests.get(url)

            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {"error": "City not found!"}

    return render_template('index.html', weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
