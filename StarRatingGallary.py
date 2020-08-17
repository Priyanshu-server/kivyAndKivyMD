from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder


#Builder String
helper_string = '''
ScreenManager:
    Hello:
<MyTile@SmartTileWithStar>
    size_hint_y : None
    height : '240dp'
<Hello>:
    name: 'hello'
    ScrollView:
        MDGridLayout:
            cols:3
            padding: dp(4),dp(4)
            spacing : dp(8)

            MyTile:
                source: 'doremon.jpg'
                text : '[size=26]Doraemon[/size]'
                # stars: 5
            MyTile:
                source: 'cat.jpg'
                text : '[size=26][color=#00FFFF]CAT[/color][/size]'
                # stars: 2
            MyTile:
                source : 'google.png'
                text: '[size=26][color=#FF0000]GOOGLE[/size][/color]'
                # stars: 5
    
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