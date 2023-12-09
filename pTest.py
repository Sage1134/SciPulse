from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.core.window import Window

Window.size = (300, 500)

screen_helper = """
Screen:
    FloatLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title:'Biology Scanner'
            pos_hint: {'top': 1}
        MDLabel:
            text: 'Welcome (user)'
            pos: (25, 325)
            theme_text_color: "Custom"
            text_color: 50/225.0, 104/255.0, 168/255.0, 1
            font_style: 'Subtitle1'
"""


class MyApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


MyApp().run()
