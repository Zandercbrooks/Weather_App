import requests
from app import App

# run app
app = App()
app.mainloop()

cityName = "Los Angeles"
apiKey = "0c9ddd24c12ae2e9e8a03d419b946243"
weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}&units=metric")
#def getWeather():
#if weatherData.status_code == 200:
   # data = weatherData.json()
    # Pulling data from weatherData
    #temp = data["main"]["temp"]


