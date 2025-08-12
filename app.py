import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.temp = None
        self.title("Weather App")

        # GUI setup
        self.canvas = tk.Canvas(self, bg="white", width=500,height=600)
        self.canvas.pack()
        # Text Entry
        self.textBox = tk.Entry(self,font=("Comic Sans", 20))
        self.textBox.pack(pady=20)
        self.textBox.bind("<Return>",self.setTemp)

    def setTemp(self,event):
        self.temp = self.textBox.get()
    def getTemp(self):
        return self.temp

        
if __name__ == "__main__":
    app = App()
    app.mainloop()


