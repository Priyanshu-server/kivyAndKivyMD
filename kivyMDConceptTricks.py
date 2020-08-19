from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
#Builder String
helper_string = '''
ScreenManager:
    Hello:
    Bye:

<Hello>:
    name: 'hello'

    MDFloatingActionButton:
        id : leftButton
        icon: 'arrow-left'
        md_bg_color: 1,0,0,1
        pos_hint: {'center_x':0.3,'center_y':0.5}
        user_font_size: '70sp'
        on_release: app.screen_swipe()
    
    MDFloatingActionButton:
        icon: 'arrow-right'
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.6,'center_y':0.5}
        user_font_size: '70sp'
        on_press : app.color_changer()
<Bye>:
    name: 'bye'
    MDLabel:
        text : 'text'

'''
class Hello(Screen):
    pass
class Bye(Screen):
    pass
sm = ScreenManager()
sm.add_widget(Hello(name = 'hello'))
sm.add_widget(Bye(name = 'bye'))



class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        self.help_str = Builder.load_string(helper_string)
        screen.add_widget(self.help_str)
        button = MDIconButton(icon = 'android',pos_hint = {'center_x':0.5,'center_y':0.3},user_font_size = '60sp')
        self.help_str.get_screen('bye').add_widget(button)
        return screen


    def color_changer(self):
        self.help_str.get_screen('hello').ids.leftButton.md_bg_color = self.theme_cls.primary_color
    
    def screen_swipe(self):
        self.help_str.get_screen('bye').manager.current  = 'bye'
DemoApp().run()