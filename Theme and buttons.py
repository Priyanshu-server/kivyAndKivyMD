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
        text: 'Hello!! world'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color : 148/255,0,211/255,1
        font_style : 'H1'
    
    MDRectangleFlatIconButton:
        icon: 'android'
        text: 'Hello'
        user_font_size: '100sp'
        pos_hint: {'center_x':0.5,'center_y':0.4}


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
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = 'A700'
        screen = Screen()

        help_str = Builder.load_string(helper_string)

        screen.add_widget(help_str)
        return screen

DemoApp().run()