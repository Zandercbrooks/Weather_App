import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO


class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
    def get_weather(self, city):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=imperial")
        return response.json() if response.status_code == 200 else None
    def fetchIcon(icon_code):
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        request = requests.get(icon_url, timeout=10)
        # request.raise_for_status()
        img = Image.open(BytesIO(request.content))
        return ImageTk.PhotoImage(img)
    


class App(tk.Tk):
    def __init__(self, weather_api: WeatherAPI):
        super().__init__()
        self.config(bg="lightblue") # sets app background to blue
        self.icon_image = None
        self.weather_api = weather_api
        self.title("Weather App")

        # GUI setup
        
        # Icon for weather symbol
        self.icon = tk.Label(self,bg=self["bg"])
        self.icon.pack(pady=20, padx=10)
        
        # Search Bar
        self.searchBar = tk.Entry(self,font=("Comic Sans", 20), justify="center")
        self.searchBar.pack(pady=20, padx=10)
        # Search Button
        searchButton = tk.Button(self, text="Search", command=self.search_weather)
        searchButton.pack(pady=10, padx=10)
        # Result text
        self.weather_label = tk.Label(self, text="",bg=self["bg"])
        self.weather_label.pack()
        
        

    def search_weather(self):
        city = self.searchBar.get()
        data = self.weather_api.get_weather(city)
        

        if data:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"].title()
            self.weather_label.config(text=f"{temp}°F\n{condition}")
            self.icon_image = WeatherAPI.fetchIcon(data["weather"][0]["icon"])
            self.icon.config(image=self.icon_image)
            
        else:
            self.weather_label.config(text="City not found")
            
        

        
if __name__ == "__main__":
    app = App()
    app.mainloop()


