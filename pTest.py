from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.core.window import Window

Window.size = (300, 500)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            md_bg_color: 6/225, 204/225, 110/225, 1
            title:'Biology Scanner'

        MDLabel:
            id: diagnostic
            text_size: self.size
            halign: 'left'
            valign: 'top'
            text: 'Welcome (user)'
            theme_text_color: "Custom"
            text_color: 50/225.0, 104/255.0, 168/255.0, 1
            font_style: 'H6'
"""


class MyApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


MyApp().run()
