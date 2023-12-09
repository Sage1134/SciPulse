import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder
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
