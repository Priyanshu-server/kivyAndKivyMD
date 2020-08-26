from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

#Builder String
helper_string = '''

ScreenManager:
    Hello:
<Hello>:
    name: 'hello'
    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            title: 'xDoramming'

        MDTabs:
            id:tabs
            on_tab_switch: app.on_tab_switch(*args)
            
        




<Tab>:
    MDLabel:
        id:label
        text:"xDoramming" #hello
        halign:"center"

'''
class Hello(Screen):
    pass
class Tab(FloatLayout, MDTabsBase):
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
        self.help_str.get_screen("hello").ids.tabs.add_widget(Tab(text = "Cameras"))
        self.help_str.get_screen("hello").ids.tabs.add_widget(Tab(text = "meassages"))
        self.help_str.get_screen("hello").ids.tabs.add_widget(Tab(text = "Story"))

    def on_tab_switch(self,instance_tabs,instance_tab,instance_tab_label,tab_text):
        instance_tab.ids.label.text = 'hello'

DemoApp().run()