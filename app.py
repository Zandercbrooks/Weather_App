import tkinter as tk

class App(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        # GUI setup
        canvas = tk.Canvas(self, bg="white", width=500,height=600)
        canvas.pack()
        # Text Entry
        textBox = tk.Entry(self,font=("Comic Sans", 20))
        textBox.pack(pady=20)


root = tk.Tk()
root.title("Weather App")
app = App(root)
app.mainloop()