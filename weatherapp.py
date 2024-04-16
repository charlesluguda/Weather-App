from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import requests

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

def get_current_weather(city):
    """
    Retrieves current weather conditions for a specified city using OpenWeatherMap API.
    """
    api_key = os.getenv("API_KEY")
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=imperial'

    try:
        # Make HTTP GET request to OpenWeatherMap API with timeout (e.g., 10 seconds)
        response = requests.get(request_url, timeout=10)

        # Check if request was successful
        if response.status_code == 200:
            weather_data = response.json()
            return {
                "city": weather_data['name'],
                "temperature": weather_data['main']['temp'],
                "description": weather_data['weather'][0]['description']
            }
        else:
            return None
    except requests.exceptions.Timeout:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    weather_data = get_current_weather(city)
    if weather_data:
        return render_template('weather.html', weather_data=weather_data)
    else:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True)
