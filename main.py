from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from startscreen import StartScreen

class PoodleApp(App):
    def build(self):
        return StartScreen()

PoodleApp().run()
