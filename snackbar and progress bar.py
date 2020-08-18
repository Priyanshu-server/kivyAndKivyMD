from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
#Builder String
helper_string = '''
ScreenManager:
    Hello:

<Hello>:
    name: 'hello'
    #:import Snackbar kivymd.uix.snackbar.Snackbar
    MDIconButton:
        icon: 'android'
        pos_hint: {'center_x':0.5,'center_y':0.5} 
        on_press: Snackbar(text='Hi! i am a button').show()
    MDProgressBar:
        value:40
        pos_hint: {'center_y':0.02}


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
               
DemoApp().run()