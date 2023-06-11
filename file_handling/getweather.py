import json, requests

APPID = 'aee6f1c6f5e9b13363bc89f767b5469c'

# Compute location from input.
location = input('Enter city name: ')

# Fetch geocode.
geocode_url = f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={APPID}'
geocode_response = requests.get(geocode_url)
geocode_response.raise_for_status()
geocode_data = geocode_response.json()

if geocode_data:
    lat, lon = geocode_data[0]['lat'], geocode_data[0]['lon']

    # Fetch weather data.
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APPID}'
    weather_response = requests.get(weather_url)
    weather_response.raise_for_status()
    weather_data = weather_response.json()

    main = weather_data.get('main', {})
    weather = weather_data.get('weather', [{}])[0]

    # Output weather data.
    print(f"Temperature: {main.get('temp', 'N/A')}")
    print(f"Pressure: {main.get('pressure', 'N/A')}")
    print(f"Humidity: {main.get('humidity', 'N/A')}")
    print(f"Description: {weather.get('description', 'N/A')}")

else:
    print("City not found")
