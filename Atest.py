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

app = Signin()
app.run()
