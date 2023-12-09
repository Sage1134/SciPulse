import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder 

    
username_helper = """
MDTextField: 
    hint_text: "Enter Username"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""
class Signin(MDApp):
     def build(self):
         screen = Screen()
         username = Builder.load_string(username_helper)
         screen.add_widget(username)
         return screen

<<<<<<< Updated upstream
app = Signin()
=======
class MyApp(MDApp):
    def build(self):
        screen = Screen()
        label = MDLabel(text="hello world", halign='center',
                        theme_text_color='Custom', text_color=(50/225.0, 104/255.0, 168/255.0, 1), font_style='H1')
        return label
    
username_helper = """
MDTextField: 
    hint_text: "Enter Username"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""
class SignIn(MDApp):
     def build(self):
         screen = Screen()
         username = Builder.load_string(username_helper)
         screen.add_widget(username)
         return screen

app = SignIn()
>>>>>>> Stashed changes
app.run()
