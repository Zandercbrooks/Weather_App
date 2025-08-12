import tkinter as tk
import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
    def get_weather(self, city):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}&units=metric")
        return response.json() if response.status_code == 200 else None


class App(tk.Tk):
    def __init__(self, weather_api):
        super().__init__()
        weather_api = weather_api
        
        self.title("Weather App")

        # GUI setup
        
        # Text Entry
        self.textBox = tk.Entry(self,font=("Comic Sans", 20))
        self.textBox.pack(pady=20)
        # Search Button
        self.button = tk.Button(self, text="Search", command=self.setCity)
        self.button.pack(pady=10)
        

    def search_weather(self):
        self.city = self.city_entry.get()
        data = self.weather_api.get_weather(self.city)

        if data:
            temp = data["main"]["temp"]
        else:
            
        

        
if __name__ == "__main__":
    app = App()
    app.mainloop()


