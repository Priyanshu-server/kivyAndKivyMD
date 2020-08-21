from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.toast import toast

#Builder String
helper_string = '''
ScreenManager:
    Hello:

<Hello>:
    name: 'hello'
    MDRaisedButton:
        text: 'TOAST UP'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        user_font_size: '80sp'
        on_press: app.toast_up()

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

    def toast_up(self):
        toast("Hi!! Toast")
DemoApp().run()