from kivymd.app import MDApp
from kivy.lang import Builder

# from kivymd.uix.label import MDLabel
# from kivymd.uix.screen import Screen
from kivy.core.window import Window

Window.size = (300, 500)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title:'demo app'
        MDLabel:
            text: 'hello world'
            halign: 'center'
"""


class MyApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        # label = MDLabel(text="Biology Scanner", pos_hint={'center_x': 0.5, 'y': 0.4}, theme_text_color='Custom', text_color=(
        #   50/225.0, 104/255.0, 168/255.0, 1), font_style='H3')
        return screen


MyApp().run()
