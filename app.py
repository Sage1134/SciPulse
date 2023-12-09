from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


Window.size = (300, 500)

layout_helper = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Science Wiz'
'''

username_helper = """
MDTextField: 
    hint_text: "Enter Username"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300
"""

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            md_bg_color: 6/225, 204/225, 110/225, 1
            title:'Biology Scanner'

        MDLabel:
            text_size: self.size
            halign: 'left'
            valign: 'top'
            text: f'Welcome {app.username.text}'
            theme_text_color: "Custom"
            text_color: 50/225.0, 104/255.0, 168/255.0, 1
            font_style: 'H6'
"""


class App(MDApp):
    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_palette = "Green"
        button = MDRectangleFlatButton(text='Login', pos_hint={
<<<<<<< Updated upstream
                                       'center_x': 0.5, 'center_y': 0.4}, on_release=self.switch_screen)
        self.username = Builder.load_string(username_helper)
=======
                                       'center_x': 0.5, 'center_y': 0.4}, on_release=self.switchToHome)
        username = Builder.load_string(username_helper)
>>>>>>> Stashed changes
        layout = Builder.load_string(layout_helper)
        self.screen.add_widget(self.username)
        self.screen.add_widget(layout)
        self.screen.add_widget(button)
        return self.screen

<<<<<<< Updated upstream
    def switch_screen(self, obj):
        if self.username.text is "":
            check_string = 'Please enter a username'
            self.dialog = MDDialog(title='Username check',
                       text=check_string,  # Change this line
                       size_hint=(0.8, 1),
                       buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
                       )
            self.dialog.open()
        else:
            self.screen.clear_widgets()
            second_screen = Builder.load_string(screen_helper)
            self.screen.add_widget(second_screen)
=======
    def switchToHome(self, obj):
        # Switch to the second screen
        self.screen.clear_widgets()
        second_screen = Builder.load_string(screen_helper)
        self.screen.add_widget(second_screen)
        button = MDRectangleFlatButton(text='Biology', pos=(
            50, 50), on_release=self.switchToHome)
        self.screen.add_widget(button)
>>>>>>> Stashed changes


    def close_dialog(self, obj):
        self.dialog.dismiss()
    
        

class MyApp(MDApp):
    def build(self):
        return App()


App().run()
