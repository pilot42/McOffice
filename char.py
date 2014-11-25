import time

class Char(Widget):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.layout = FloatLayout()
        self.sprite = Image(
            source="assets/morgan-freeman.jpg",
            texture_size=(30, 50),
            size=(30, 50),
            #center_x=Window.width / 2,
            #center_y=(Window.height / 2) + 150

        player = ObjectProperty(None)

        def __init__(self, **kwargs):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

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
        )
        self.layout.add_widget(self.sprite)