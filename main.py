import requests
import xml.etree.ElementTree as ET


# API class
class WeatherApiClient:
    # constructor
    def __init__(self, api_key):
        self.api_key = api_key

    # request data from api
    def getWeather(self, city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric'
        res = requests.get(url)
        return res.json()

    # Show output
    def showData(self, data):
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        zone = data['timezone'] / 3600

        print(f"\nTemperature: {temp} degree Celsius")
        print(f"Description: {description}")
        print(f"Zone: GMT {zone}")


if __name__ == '__main__':

    # Menu
    print("\t\tWeather Forecast API\n")
    print("1) Enter API Key")
    print("2) Use Default API Key")
    choice = input("Choice: ")

    # get api key
    api_key = ''
    if choice == '1':
        api_key = input("Enter API Key: ")
    elif choice == '2':
        api_key = 'ac7c75b9937a495021393024d0a90c44'

    # Create object
    weather_api = WeatherApiClient(api_key)

    # Use functions
    data = weather_api.getWeather(input("Enter City: "))
    weather_api.showData(data)
