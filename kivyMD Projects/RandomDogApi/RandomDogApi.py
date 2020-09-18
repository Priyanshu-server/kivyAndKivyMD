from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.app import MDApp
import requests
import json
from kivy.core.window import Window
Window.size = {400,600}



Builder_strng = '''
<MyTile@SmartTileWithStar>
    size_hint_y: None
    height: "240dp"
ScreenManager:
    Main:

<Main>:
    name:'main'


    MDRaisedButton:
        text:'Load'
        pos_hint:{'center_x':0.5,'center_y':0.1}
        on_press: app.dog_image()
    MDLabel:
        text:'Random Dog API'
        font_style: 'H2'
        halign : 'center'
        pos_hint: {'center_y':0.8}

    MDGridLayout:
        cols: 1
        adaptive_height: True
        padding: dp(20), dp(120)
        spacing: dp(4)

        MyTile:
            id:img
            source: ""


'''
class Main(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name = 'main'))

class MainApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(Builder_strng)
        return self.strng

    def dog_image(self):
        self.url =  json.loads(requests.get("https://dog.ceo/api/breeds/image/random").content)['message']
        self.strng.get_screen('main').ids.img.source = self.url


MainApp().run()