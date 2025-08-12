from app import App, WeatherAPI

if __name__ == "__main__":
    api = WeatherAPI(api_key="0c9ddd24c12ae2e9e8a03d419b946243")
    app = App(api)
    app.mainloop()