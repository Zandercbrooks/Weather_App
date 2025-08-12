import tkinter as tk
import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
    def get_weather(self, city):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=imperial")
        return response.json() if response.status_code == 200 else None


class App(tk.Tk):
    def __init__(self, weather_api: WeatherAPI):
        super().__init__()
        self.weather_api = weather_api
        
        self.title("Weather App")

        # GUI setup
        
        # Search Bar
        self.searchBar = tk.Entry(self,font=("Comic Sans", 20))
        self.searchBar.pack(pady=20)
        # Search Button
        self.searchButton = tk.Button(self, text="Search", command=self.search_weather)
        self.searchButton.pack(pady=10)
        # Result text
        self.weather_label = tk.Label(self, text="")
        self.weather_label.pack()
        

    def search_weather(self):
        city = self.searchBar.get()
        data = self.weather_api.get_weather(city)

        if data:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"].title()
            self.weather_label.config(text=f"{temp}°F\n{condition}")
        else:
            self.weather_label.config(text="City not found")
            
        

        
if __name__ == "__main__":
    app = App()
    app.mainloop()


