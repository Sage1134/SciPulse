import shutil
import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.theming import ThemeManager
from physicsBot import getResponse
import requests


import bioClassifier
import chemClassifier

# window size
Window.size = (300, 500)

# First Page
layout_helper = '''
Screen:
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: 'Science Pulse'

        BoxLayout:
            orientation: 'vertical'
'''
# username page
username_helper = """
MDTextField: 
    id: username_field
    hint_text: "Enter Username"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300
"""
# homepage
homepage = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            md_bg_color: 6/225, 204/225, 110/225, 1
            title:'Homepage'

        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'biochemphy.png'  
                size_hint_y: None
                height: 300 


        MDLabel:
            id: welcome_label
            text: "Welcome"
            text_size: self.size
            halign: 'center'
            valign: 'top'
            theme_text_color: "Custom"
            text_color: 50/225.0, 104/255.0, 168/255.0, 1
            font_style: 'H6'
"""
# bio page
biologypage = '''
BoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: 'Biology Scanner'

    FloatLayout:
        orientation: 'vertical'
        MDRectangleFlatButton:
            text: 'Select File'
            pos: (400, 775)
            on_release: app.select_file()
        
    MDLabel:
        text: "Please Select a File to Classify"
        text_size: self.size
        halign: 'center'
        valign: 'top'
        theme_text_color: "Custom"
        text_color: 50/225.0, 104/255.0, 168/255.0, 1
        font_style: 'H6'
'''
# chem page
chemistryPage = '''
BoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: 'Titration Scanner'

    FloatLayout:
        orientation: 'vertical'
        MDRectangleFlatButton:
            text: 'Select File'
            pos: (400, 775)
            on_release: app.select_file()
        
    MDLabel:
        text: "Please Select a File to Classify"
        text_size: self.size
        halign: 'center'
        valign: 'top'
        theme_text_color: "Custom"
        text_color: 50/225.0, 104/255.0, 168/255.0, 1
        font_style: 'H6'
'''

# wizard page
wizardPage = '''
Screen:
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: 'Science Wizard'

        BoxLayout:
            orientation: 'vertical'

    MDTextField: 
        id: textinput_field
        hint_text: "Enter Your Question"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
'''


class App(MDApp):
    # builds the basic front-page
    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Dark"  # Use "Light" for a light theme
        self.screen = Screen()
        self.dialog = None  # Define
        button = MDRectangleFlatButton(text='Login', pos_hint={
                                       'center_x': 0.5, 'center_y': 0.4}, on_release=self.loginCheck)
        self.username = Builder.load_string(username_helper)
        layout = Builder.load_string(layout_helper)
        self.screen.add_widget(self.username)
        self.screen.add_widget(layout)
        self.screen.add_widget(button)
        self.file_manager = None  # initialize the file manager
        return self.screen

    # checks if use put a username in login, if not they will be prompted to do so
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
            self.changeToHome(obj)

    # changes the page to the homepage
    def changeToHome(self, obj):
        self.current_page = "Home"
        self.screen.clear_widgets()
        home_screen = Builder.load_string(homepage)
        self.screen.add_widget(home_screen)
        biology_button = MDRectangleFlatButton(text='Bio Scanner', pos=(
            50, 50), on_release=self.changeToBio)
        self.screen.add_widget(biology_button)
        wiz_button = MDRectangleFlatButton(text='Science Wizard', pos=(
            300, 50), on_release=self.changeToWizard)
        self.screen.add_widget(wiz_button)
        chem_button = MDRectangleFlatButton(text='Chem Scanner', pos=(
            300, 150), on_release=self.changeToChem)
        self.screen.add_widget(chem_button)

    # changes the page to the biology page
    def changeToBio(self, obj):
        self.current_page = "Biology"
        self.screen.clear_widgets()
        bio_screen = Builder.load_string(biologypage)
        self.screen.add_widget(bio_screen)
        home_button = MDRectangleFlatButton(text='Home', pos=(
            50, 50), on_release=self.loginCheck)
        self.screen.add_widget(home_button)
        wiz_button = MDRectangleFlatButton(text='Science Wizard', pos=(
            300, 50), on_release=self.changeToWizard)
        self.screen.add_widget(wiz_button)
        chem_button = MDRectangleFlatButton(text='Chem Scanner', pos=(
            300, 150), on_release=self.changeToChem)
        self.screen.add_widget(chem_button)

    # changes the page to the chemistry page
    def changeToChem(self, obj):
        self.current_page = "Chemistry"
        self.screen.clear_widgets()
        chem_screen = Builder.load_string(chemistryPage)
        self.screen.add_widget(chem_screen)
        home_button = MDRectangleFlatButton(text='Home', pos=(
            50, 50), on_release=self.loginCheck)
        self.screen.add_widget(home_button)
        wiz_button = MDRectangleFlatButton(text='Science Wizard', pos=(
            300, 50), on_release=self.changeToWizard)
        self.screen.add_widget(wiz_button)
        biology_button = MDRectangleFlatButton(text='Bio Scanner', pos=(
            300, 150), on_release=self.changeToBio)
        self.screen.add_widget(biology_button)

    # allows you to select file
    def select_file(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager, select_path=self.selected_file
        )
        self.file_manager.show('/')  # You can specify the starting directory

    # exits the file manager
    def exit_file_manager(self, *args):
        self.file_manager.close()

    # selects the file
    def selected_file(self, path):
        print(f'Selected file: {path}')
        fileToCopy = path
        destination = './tempAssets'
        shutil.copy(fileToCopy, destination)

        # file name
        file_name = os.path.basename(path)

        # checks the page. If bio, use bio classifier or if chem, use chem classifier
        if self.current_page == "Biology":
            output = bioClassifier.predict(file_name)
        elif self.current_page == "Chemistry":
            output = chemClassifier.predict(file_name)
        else:
            output = "Invalid screen"

        print(output)

        # shows response on a dialog
        self.dialog = MDDialog(title='Information',
                               text=output,
                               size_hint=(0.8, 1),
                               buttons=[MDFlatButton(
                                   text='Close', on_release=self.close_dialog)]
                               )
        self.dialog.open()

        self.exit_file_manager()

    # Changes to wizard page
    def changeToWizard(self, obj):
        self.screen.clear_widgets()
        wizard_screen = Builder.load_string(wizardPage)
        self.screen.add_widget(wizard_screen)

        self.text_input_field = wizard_screen.ids.textinput_field

        answerButton = MDRectangleFlatButton(
            text='Enter', pos_hint={'center_x': 0.5, 'center_y': 0.4}, on_release=self.wizard
        )
        self.screen.add_widget(answerButton)
        home_button = MDRectangleFlatButton(
            text='Home', pos=(50, 50), on_release=self.loginCheck)
        self.screen.add_widget(home_button)
        biology_button = MDRectangleFlatButton(
            text='Bio Scanner', pos=(300, 50), on_release=self.changeToBio)
        self.screen.add_widget(biology_button)
        chem_button = MDRectangleFlatButton(text='Chem Scanner', pos=(
            300, 150), on_release=self.changeToChem)
        self.screen.add_widget(chem_button)

    # closes dialog page

    def close_dialog(self, obj):
        self.dialog.dismiss()

    # uses the openAI api to get a response
    def wizard(self, obj):
        response = getResponse(self.text_input_field.text)
        self.dialog = MDDialog(title='Science Wizard',
                               text=response,
                               size_hint=(0.8, 1),
                               buttons=[MDFlatButton(
                                   text='Close', on_release=self.close_dialog)]
                               )
        self.dialog.open()

# builds app


class MyApp(MDApp):
    def build(self):
        return App()


# runs app
if __name__ == "__main__":
    App().run()
