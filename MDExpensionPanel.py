from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine

#Builder String
helper_string = '''
<Content>:
    adaptive_height: True


    TwoLineIconListItem:
        text : 'Hello'
        secondary_text : 'Sec Text'

        IconLeftWidget:
            icon: 'phone'

ScreenManager:
    Hello:
<Hello>:
    name: 'hello'

    ScrollView:
        MDGridLayout:
            id: box
            cols:1
            adaptive_height : True

'''
class Hello(Screen):
    pass
class Content(MDBoxLayout):
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
        for i in range(10):
            self.help_str.get_screen('hello').ids.box.add_widget(
                MDExpansionPanel(
                    icon = 'google.png',
                    content = Content(),
                    panel_cls= MDExpansionPanelThreeLine(
                        text = 'Text 1',
                        secondary_text= 'sec text',
                        tertiary_text = 'ter text'
                    ) )

            )
DemoApp().run()