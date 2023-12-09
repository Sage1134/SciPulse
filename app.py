import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.9.0')


class MyApp(App):
    def build(self):
        label = Label(text="hello world", font_size='20sp')
        return label


app = MyApp()
app.run()
