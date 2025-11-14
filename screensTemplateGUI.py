import tkinter as tk
from tkinter import ttk
import pyttsx3

engine = pyttsx3.init() 

def read_aloud(text):
    engine.stop()  
    engine.say(text)
    engine.runAndWait()

class Screen(tk.Frame):
    def __init__(self, parent, controller, text, screen_name):
        super().__init__(parent)
        self.controller = controller
        self.text = text
        self.screen_name = screen_name

        label = tk.Label(self, text=text, font=("Arial", 16), wraplength=400)
        label.pack(pady=20)

        read_button = ttk.Button(self, text="Read Aloud", command=lambda: read_aloud(self.text))
        read_button.pack(pady=10)

        nav_frame = tk.Frame(self)
        nav_frame.pack(pady=10)

        if screen_name != "Screen 1":
            back_button = ttk.Button(nav_frame, text="Back", command=lambda: controller.show_screen(f"Screen {int(screen_name.split()[-1]) - 1}"))
            back_button.pack(side="left", padx=5)

        if screen_name != "Screen 3":
            next_button = ttk.Button(nav_frame, text="Next", command=lambda: controller.show_screen(f"Screen {int(screen_name.split()[-1]) + 1}"))
            next_button.pack(side="left", padx=5)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Screen GUI with Voice")
        self.geometry("500x300")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.screens = {}
        self.create_screens()

    def create_screens(self):
        screen_texts = {
            "Screen 1": "Welcome to Screen 1. This is the first screen.",
            "Screen 2": "This is Screen 2. You can navigate back or forward.",
            "Screen 3": "You are now on Screen 3. This is the last screen."
        }

        for screen_name, text in screen_texts.items():
            screen = Screen(self.container, self, text, screen_name)
            self.screens[screen_name] = screen
            screen.grid(row=0, column=0, sticky="nsew")

        self.show_screen("Screen 1")

    def show_screen(self, screen_name):
        screen = self.screens[screen_name]
        screen.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop() #call main loop tkinter