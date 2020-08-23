from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory

#Builder String
helper_string = '''

<CustomSheet@BoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height: "400dp"

    MDToolbar:
        title: 'Custom bottom sheet:'

    ScrollView:
        OneLineIconListItem:
            text: "Preview"
            IconLeftWidget:
                icon: "page-previous"

                    



ScreenManager:
    Hello:

<Hello>:
    name: 'hello'
    MDFloatingActionButton:
        icon: 'android'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        user_font_size: '100sp'
        on_press: on_release: app.show_example_custom_bottom_sheet()
'''
class Hello(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Hello(name = 'hello'))



class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        self.help_str = Builder.load_string(helper_string)

        screen.add_widget(self.help_str)
        return screen

    def show_example_custom_bottom_sheet(self):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.CustomSheet())
        self.custom_sheet.open()

DemoApp().run()