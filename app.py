import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen


class MyApp(MDApp):
    def build(self):
        screen = Screen()
        label = MDLabel(text="hello world", halign='center',
                        theme_text_color='Custom', text_color=(50/225.0, 104/255.0, 168/255.0, 1), font_style='H1')
        return label


app = MyApp()
app.run()
