import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")

        # GUI setup
        self.canvas = tk.Canvas(self, bg="white", width=500,height=600)
        self.canvas.pack()
        # Text Entry
        self.textBox = tk.Entry(self,font=("Comic Sans", 20))
        self.textBox.pack(pady=20)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()


