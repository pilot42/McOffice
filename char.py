from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Rectangle, Ellipse, Line
import time

class Char(Widget):
    def __init__(self):
        super(Char, self).__init__()
        self.layout = FloatLayout()
        self.sprite = Image(
            source="assets/morgan-freeman.jpg",
            texture_size=(30, 50),
            size=(30, 50),
            #center_x=Window.width / 2,
            #center_y=(Window.height / 2) + 150
        )
        #player = ObjectProperty(None)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.layout.add_widget(self.sprite)
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'd':
            self.player.center_x += 10
        elif keycode[1] == 'a':
            self.player.center_x -= 10
        elif keycode[1] == 'w':
            self.player.center_y += 10
            time.sleep(.5)
            self.player.center_y -= 10
        return True