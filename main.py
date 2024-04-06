from kivy.app import App
from kivy.uix.label import Label

class map(App):
        def build(self):
                return Label(text = "Hello")

if __name__ == "__main__":
        map().run()
