from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder

#Builder String
helper_string = '''
ScreenManager:
    Hello:
<Hello>:
    name: 'hello'
    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            title: 'Bottom navigation'
            md_bg_color: .2, .2, .2, 1
            specific_text_color: 1, 1, 1, 1

        MDBottomNavigation:
            panel_color: 1,1,1,1

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Python'
                icon: 'language-python'

                MDLabel:
                    text: 'Python'
                    halign: 'center'

            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'C++'
                icon: 'language-cpp'

                MDLabel:
                    text: 'I programming of C++'
                    halign: 'center'

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'JS'
                icon: 'language-javascript'

                MDLabel:
                    text: 'JS'
                    halign: 'center'



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