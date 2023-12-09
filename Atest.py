from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window

Window.size = (300, 500)

username_helper = """
MDTextField: 
    hint_text: "Enter Username"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300
"""

layout_helper = '''
Screen: 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Science Wiz'
'''

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

class Signin(MDApp):
    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_palette = "Green"
        button = MDRectangleFlatButton(text='Login', pos_hint={'center_x': 0.5, 'center_y': 0.4}, on_release=self.switch_screen) 
        username = Builder.load_string(username_helper)
        layout = Builder.load_string(layout_helper)
        self.screen.add_widget(username)
        self.screen.add_widget(layout)
        self.screen.add_widget(button)
        return self.screen
    
    def switch_screen(self, obj):
        # Switch to the second screen
        self.screen.clear_widgets()
        second_screen = Builder.load_string(screen_helper)
        self.screen.add_widget(second_screen)

class MyApp(MDApp):
    def build(self):
        return Signin()

Signin().run()
