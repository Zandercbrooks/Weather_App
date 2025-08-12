import requests

cityName = "Los Angeles"
apiKey = "0c9ddd24c12ae2e9e8a03d419b946243"
weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}&units=metric")

if weatherData.status_code == 200:
    print(weatherData.json())
    temp = weatherData["main"]["temp"]
    