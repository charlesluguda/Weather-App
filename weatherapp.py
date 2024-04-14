import os
from dotenv import load_dotenv
import requests

def get_current_weather():
    """
    Retrieves current weather conditions for a specified city using OpenWeatherMap API.
    """
    print("\n*** Get Current Weather Conditions ***\n")

    # Load environment variables from .env file
    load_dotenv()

    # Prompt user to enter city name
    city = input("\nEnter city name: ")

    # Retrieve API key from environment variables
    api_key = os.getenv("API_KEY")

    # Construct API request URL
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=imperial'

    # Print the API request URL (for testing purposes)
    print(f"Request URL: {request_url}")

    try:
        # Make HTTP GET request to OpenWeatherMap API with timeout (e.g., 10 seconds)
        response = requests.get(request_url, timeout=10)

        # Check if request was successful
        if response.status_code == 200:
            weather_data = response.json()
            print("\nCurrent Weather Conditions:")
            print(f"City: {weather_data['name']}")
            print(f"Temperature: {weather_data['main']['temp']} °F")
            print(f"Weather Description: {weather_data['weather'][0]['description']}")
        else:
            print(f"\nFailed to retrieve weather data. Status Code: {response.status_code}")
    except requests.exceptions.Timeout:
        print("\nRequest timed out. Please try again later.")

if __name__ == "__main__":
    # Call the function to get current weather conditions
    get_current_weather()
