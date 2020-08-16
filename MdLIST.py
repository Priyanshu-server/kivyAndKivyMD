from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.list import MDList,OneLineListItem,TwoLineListItem,ThreeLineListItem

#Builder String
helper_string = '''
ScreenManager:
    Hello:

<Hello>:
    name: 'hello'

    ScrollView:
        MDList:
            id: ls
            OneLineListItem:
                text: 'Hello'
            TwoLineListItem:
                text : 'Item 2'
                secondary_text: ' text2'
                
            ThreeLineListItem:
                text:' item2'
                secondary_text: 'text 2'
                tertiry_text: 'text 3'


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

    # def on_start(self):
    #     for i in range(20):
    #         self.help_str.get_screen('hello').ids.ls.add_widget(
    #             OneLineListItem(text=f'item {i} ')
    #         )
    #         self.help_str.get_screen('hello').ids.ls.add_widget(
    #              TwoLineListItem(text = f'item for twoline {i}',secondary_text= f'text {i}'))
            
               
DemoApp().run()