
import requests

API_KEY = ""
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():
    
    location = input("Enter a city name or ZIP code: ").strip()

    
    if not location:
        print("Error: City name or ZIP code cannot be empty.")
        return

    
    if location.isdigit():
        
        params = {
            "zip": f"{location},ZA",
            "appid": API_KEY,
            "units": "metric"
        }
    else:
        
        params = {
            "q": location,
            "appid": API_KEY,
            "units": "metric"
        }

    try:
        
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        
        if response.status_code == 404:
            print("Error: City or ZIP code not found.")
            return

        if response.status_code == 401:
            print("Error: Invalid API key. Check your API key.")
            return

        response.raise_for_status()

        
        data = response.json()

        
        city = data["name"]
        temperature_c = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        
        temperature_f = (temperature_c * 9 / 5) + 32

        
        print("\n--- Current Weather ---")
        print(f"Location: {city}")
        print(f"Temperature: {temperature_c:.1f} °C")
        print(f"Temperature: {temperature_f:.1f} °F")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.title()}")
        print(f"Wind speed: {wind_speed} m/s")

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Network connection failed. Check your internet.")

    except requests.exceptions.RequestException as error:
        print(f"Error: Unable to retrieve weather data. {error}")

    except (KeyError, IndexError, ValueError):
        print("Error: Unexpected response received from the weather API.")



get_weather()

