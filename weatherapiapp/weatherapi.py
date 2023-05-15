import requests

API_KEY = "7cc9e768177548ddb2191214231505"
BASE_URL = "https://api.weatherapi.com/v1/current.json"

city = input("enter the city name:")
request_url = f"{BASE_URL}?key={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['current']['condition']['text']
    temperature = data['current']['temp_c']
    print(f"weather in {city}:{weather}")
    print(f"temperature in {city}:{temperature}")

    
else:
    print("An error occurred.")