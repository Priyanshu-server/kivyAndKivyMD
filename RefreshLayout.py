from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.utils import asynckivy

Builder_string = '''
ScreenManager:
    Main:

<Main>:
    name:'main'
    MDLabel:
        id:heading
        text:'hello world'
        font_style:'H2'
        pos_hint: {'center_y':0.5}
        halign:'center'

'''
class Main(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name = 'main'))

class NewApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(Builder_string)
        self.set_heading()
        return self.strng

    def set_heading(self):
        async def set_heading():
            for i in range(5):
                await asynckivy.sleep(1)
                text_heading = self.strng.get_screen('main').ids.heading
                text_heading.text = str(i)
            text_heading.text = "Happy Birthday !!"

        asynckivy.start(set_heading())

NewApp().run()