from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager

Builder_strng = '''
ScreenManager:
    Main:
<Main>:
    name: 'main'
    ScrollView:
        MDGridLayout:
            cols:3
            adaptive_height:True
            padding: dp(4),dp(10)
            spacing: dp(4)

            MDLabel:
                text:'Hello worl loremasdsaddddddddddddassssssssssssssssssssssssssssssd'
            MDLabel:
                text:'Hello world'
            MDLabel:
                text:'Hello xDoramming viewers'
'''

class Main(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name = 'main'))

class NewApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(Builder_strng)
        return self.strng

NewApp().run()