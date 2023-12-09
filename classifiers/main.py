import shutil
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from physicsBot import getResponse



Window.size = (300, 500)

user = ''


layout_helper = '''
Screen:
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: 'Science Wiz'

        BoxLayout:
            orientation: 'vertical'
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

        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'biochemphy.png'  
                size_hint_y: None
                height: 300  


        MDLabel:
            id: welcome_label
            text_size: self.size
            halign: 'left'
            valign: 'top'
            theme_text_color: "Custom"
            text_color: 50/225.0, 104/255.0, 168/255.0, 1
            font_style: 'H6'
"""

biologypage = '''
BoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: 'Biology Scanner'

    BoxLayout:
        orientation: 'vertical'
'''

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
    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_palette = "Green"
        self.dialog = None  # Define
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
            self.changeToHome(obj)

    def changeToHome(self, obj):
        self.screen.clear_widgets()
        home_screen = Builder.load_string(homepage)
        self.screen.add_widget(home_screen)
        biology_button = MDRectangleFlatButton(text='Bio Scanner', pos=(
            50, 50), on_release=self.changeToBio)
        self.screen.add_widget(biology_button)
        wiz_button = MDRectangleFlatButton(text='Science Wizard', pos=(
            300, 50), on_release=self.changeToWizard)
        self.screen.add_widget(wiz_button)

    def changeToBio(self, obj):
        self.screen.clear_widgets()
        bio_screen = Builder.load_string(biologypage)
        self.screen.add_widget(bio_screen)
        home_button = MDRectangleFlatButton(text='Home', pos=(
            50, 50), on_release=self.loginCheck)
        self.screen.add_widget(home_button)
        wiz_button = MDRectangleFlatButton(text='Science Wizard', pos=(
            300, 50), on_release=self.changeToWizard)
        self.screen.add_widget(wiz_button)

    def changeToWizard(self, obj):
        self.screen.clear_widgets()
        wizard_screen = Builder.load_string(wizardPage)
        self.screen.add_widget(wizard_screen)

        # Store the reference to the MDTextField in a variable
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

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def wizard(self, obj):
        response = getResponse("self.text_input_field.text")
        print(response)


class MyApp(MDApp):
    def build(self):
        return App()


if __name__ == "__main__":
    App().run()
