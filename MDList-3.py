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

    ScrollView:
        MDList:
            id: ls
            OneLineListItem:
                text: 'Hello'
                on_press: app.click()
            TwoLineListItem:
                text : 'Item 2'
                secondary_text: ' text2'
                
            ThreeLineListItem:
                text:' item2'
                secondary_text: 'text 2'
                tertiry_text: 'text 3'

<Bye>:
    name: 'bye'
    MDLabel:
        text:'Good Bye'
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
        return screen

    def click(self):
        self.help_str.get_screen('bye').manager.current = 'bye'
DemoApp().run()