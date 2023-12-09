import kivy
from kivy.app import App
from kivy.uix.label import MDLabel

kivy.require('1.9.0')


class MyApp(App):
    def build(self):
        label = MDLabel(text="hello world", halign='center',
                        theme_Text_Color='custom', text_color=(0, 0, 1, 1))
        return label


app = MyApp()
app.run()
