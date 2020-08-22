from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.bottomsheet import MDListBottomSheet,MDGridBottomSheet
from kivymd.toast import toast
Window.size = (400,600)

#Builder String
helper_string = '''
ScreenManager:
    Hello:

<Hello>:
    name: 'hello'
    MDFloatingActionButton:
        icon: 'android'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        user_font_size: '100sp'
        on_press: app.bottom_layer()
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
    def callback_(self,*args):
        toast(args[0])

    def bottom_layer(self):
        data = {
            "Facebook":"facebook-box",
            "YouTube":"youtube",
            "Twitter":"twitter-box",
            "Camera":"camera"
        }
        bottom_sheet = MDGridBottomSheet()
        for item in data.items():
            bottom_sheet.add_item(
                item[0],
                lambda x,y=item[0]:self.callback_(y),
                icon_src=item[1]
            )
        bottom_sheet.open()
DemoApp().run()