import tkinter as tk
class App(tk.Tk):
    def __init__(self, on_enter=None):
        super().__init__()
        self.city = None
        self.on_enter = on_enter
        self.title("Weather App")

        # GUI setup
        self.canvas = tk.Canvas(self, bg="white", width=500,height=600)
        self.canvas.pack()
        # Text Entry
        self.textBox = tk.Entry(self,font=("Comic Sans", 20))
        self.textBox.pack(pady=20)
        self.textBox.bind("<Return>",self.setCity)

    def setCity(self,event):
        self.city = self.textBox.get()
        if self.on_enter:
            self.on_enter()

    def getCity(self):
        return self.city

        
if __name__ == "__main__":
    app = App()
    app.mainloop()


