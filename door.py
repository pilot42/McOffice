from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Rectangle, Ellipse, Line
class Door (Widget):
	def __init__(self):
		super(Door, self).__init__()
		self.layout = FloatLayout()
		self.add_widget(self.layout)
            source="assets/morgan-freeman.jpg",
            texture_size=(300, 600),
            size=(300, 600),
            center_x=Window.width / 2,
            center_y=(Window.height / 2) + 150
        )
		self.y = 0
		self.layout.add_widget(self.sprite)
