from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
#Builder String


helper_string = '''
ScreenManager:
    Hello:

<Hello>:
    name: 'hello'
    MDChooseChip:
        
        pos_hint: {'center_x':0.55,'center_y':0.5}
        MDChip:
            label:'Google'
            icon: 'android'
            selected_chip_color: 0,0,1,1

        MDChip:
            label:'Facebook'
            icon:'arrow-right'
            selected_chip_color: 0,0,1,1
            
        


'''
class Hello(Screen):
    pass

sm = ScreenManager()

sm.add_widget(Hello(name = 'hello'))

class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        help_str = Builder.load_string(helper_string)

        screen.add_widget(help_str)
        return screen

    def call(self,instance,value):
        print(instance,value,sep='\n')
DemoApp().run()