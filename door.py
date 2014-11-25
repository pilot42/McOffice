class Door(Widget):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.layout = FloatLayout()
        self.sprite = Image(
            source="assets/morgan-freeman.jpg",
            texture_size=(300, 600),
            size=(300, 600),
            center_x=Window.width / 2,
            center_y=(Window.height / 2) + 150
        )
        self.layout.add_widget(self.sprite)