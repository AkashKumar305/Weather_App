import requests

def get_weather_data(url, querystring, headers):
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  
        weather_data = response.json()
    except requests.exceptions.RequestException as e:
        print("Error: Failed to retrieve weather data -", e)
        return

    current_weather = weather_data.get('current', {})
    location_info = weather_data.get('location', {})

    if not current_weather or not location_info:
        print("Error: Incomplete weather data received.")
        return

    display_weather_data(current_weather, location_info)

def display_weather_data(current_weather, location_info):
    cloud_cover = current_weather.get('cloud', '-')
    condition_text = current_weather.get('condition', {}).get('text', '-')
    temperature_celsius = current_weather.get('temp_c', '-')
    temperature_fahrenheit = current_weather.get('temp_f', '-')
    humidity = current_weather.get('humidity', '-')
    wind_speed_kph = current_weather.get('wind_kph', '-')
    wind_speed_mph = current_weather.get('wind_mph', '-')
    wind_direction = current_weather.get('wind_dir', '-')
    pressure_mb = current_weather.get('pressure_mb', '-')
    visibility_km = current_weather.get('vis_km', '-')
    visibility_miles = current_weather.get('vis_miles', '-')
    
    country = location_info.get('country', '-')
    city = location_info.get('name', '-')
    region = location_info.get('region', '-')
    local_time = location_info.get('localtime', '-')

    print("Weather in {}, {} - {}".format(city, region, country))
    print("Local Time: {}".format(local_time))
    print("Condition: {}".format(condition_text))
    print("Temperature: {:.1f}°C ({:.1f}°F)".format(temperature_celsius, temperature_fahrenheit))
    print("Cloud Cover: {}%".format(cloud_cover))
    print("Humidity: {}%".format(humidity))
    print("Wind Speed: {:.1f} kph ({:.1f} mph), Direction: {}".format(wind_speed_kph, wind_speed_mph, wind_direction))
    print("Pressure: {} mb".format(pressure_mb))
    print("Visibility: {:.1f} km ({:.1f} miles)".format(visibility_km, visibility_miles))

def main():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    city = input('Enter a City name: ')
    querystring = {'q': city}
    headers = {
        "X-RapidAPI-Key": "778a2e7123msh5e3a530d8bfbf9cp188e4bjsnfc9bd024b4e0",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    get_weather_data(url, querystring, headers)

if __name__ == '__main__':
    main()
