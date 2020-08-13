from kivymd.app import MDApp
from kivymd.uix.screen import Screen

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        return screen

DemoApp().run()