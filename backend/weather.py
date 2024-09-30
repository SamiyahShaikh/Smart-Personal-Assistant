import requests

def get_weather():
    api_key = 'YOUR_OPENWEATHER_API_KEY'
    city = 'San Francisco'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
    weather_data = response.json()
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
    return f'The weather in {city} is {description} with a temperature of {temperature:.1f}°C.'
