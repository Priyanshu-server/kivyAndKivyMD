from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder

#Builder String
helper_string = '''
ScreenManager:
    Hello:
    Bye:

<Hello>:
    name: 'hello'
    MDLabel:
        text: 'Hello world'

<Bye>
    name: 'bye'
    MDLabel: 
        text: 'Good Bye'




'''
class Hello(Screen):
    pass
class Bye(Screen):
    pass

sm = ScreenManager()

sm.add_widget(Hello(name = 'hello'))
sm.add_widget(Bye(name='bye'))

class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        help_str = Builder.load_string(helper_string)

        screen.add_widget(help_str)
        return screen

DemoApp().run()