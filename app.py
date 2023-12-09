from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window

Window.size = (300, 500)

user = ''

layout_helper = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Science Wiz'
'''

username_helper = """
MDTextField: 
    id: username_field
    hint_text: "Enter Username"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300
"""

homepage = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            md_bg_color: 6/225, 204/225, 110/225, 1
            title:'Homepage'

        MDLabel:
            id: welcome_label
            text_size: self.size
            halign: 'left'
            valign: 'top'
            theme_text_color: "Custom"
            text_color: 50/225.0, 104/255.0, 168/255.0, 1
            font_style: 'H6'
"""


class App(MDApp):
    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_palette = "Green"
        self.dialog = None  # Define the dialog attribute
        button = MDRectangleFlatButton(text='Login', pos_hint={
                                       'center_x': 0.5, 'center_y': 0.4}, on_release=self.loginCheck)
        self.username = Builder.load_string(username_helper)
        layout = Builder.load_string(layout_helper)
        self.screen.add_widget(self.username)
        self.screen.add_widget(layout)
        self.screen.add_widget(button)
        return self.screen

    def loginCheck(self, obj):
        if self.username.text == "":
            check_string = 'Please enter a username'
            self.dialog = MDDialog(title='Username check',
                                   text=check_string,
                                   size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(
                                       text='Close', on_release=self.close_dialog)]
                                   )
            self.dialog.open()
        else:
            self.screen.clear_widgets()
            second_screen = Builder.load_string(homepage)
            self.screen.add_widget(second_screen)
            biology_button = MDRectangleFlatButton(text='Biology', pos=(
                50, 50))
            self.screen.add_widget(biology_button)

    def close_dialog(self, obj):
        self.dialog.dismiss()


class MyApp(MDApp):
    def build(self):
        return App()


App().run()
