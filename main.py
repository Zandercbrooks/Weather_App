import requests

cityName = ""
apiKey = ""
url = ""
weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}&units=metric")