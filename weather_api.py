import requests

# pip install requests para fazer o request para a pagina do API.
# we are using the requests module to get the data from the weather API server

API_KEY = ##############################
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['list'][0]['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")
