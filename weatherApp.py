import requests

API_KEY = '7cc8ff3b26de45c9bede1b215fb83539'

def fetch_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}appid={API_KEY}&q={city}&"
    response = requests.get(complete_url)
    return response.json()

def display_data(data):
    if data['cod'] != '404':
        main_data = data['main']
        temperature = main_data['temp']
        humidity = main_data['humidity']
        weather_description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        print(f"Temperature: {temperature:.2f}")
        print(f"Humidity: {humidity}")
        print(f"Weather description: {weather_description.capitalize()}")
        print(f"Wind speed: {wind_speed}")
    else:
        print("City not found. Please try again.")

def main():
    city = input("Enter the name of the city: ")
    weather_data = fetch_data(city)
    display_data(weather_data)

if __name__ == "__main__":
    main()