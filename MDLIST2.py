from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.list import MDList,OneLineListItem,TwoLineListItem,ThreeLineListItem,OneLineIconListItem,IconLeftWidget

#Builder String
helper_string = '''
ScreenManager:
    Hello:

<Hello>:
    name: 'hello'

    ScrollView:
        MDList:
            id: ls
            # OneLineIconListItem:
            #     text: 'item 1'
            #     IconLeftWidget:
            #         icon : 'android'
            # OneLineAvatarListItem:
            #     text: 'item2'
            #     ImageLeftWidget:
            #         source : 'fb.png'


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

    def on_start(self):
        for i in range(20):
            
            item = OneLineIconListItem(text=f'item {i} ')
            icon = IconLeftWidget(icon= 'android')
            item.add_widget(icon)
            self.help_str.get_screen('hello').ids.ls.add_widget(item)
            self.help_str.get_screen('hello').ids.ls.add_widget(
                 TwoLineListItem(text = f'item for twoline {i}',secondary_text= f'text {i}'))
            
               
DemoApp().run()