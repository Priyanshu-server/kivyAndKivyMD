from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.taptargetview import MDTapTargetView
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

    MDIconButton:
        icon: 'android'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_release: root.manager.current = 'bye' 
        on_press : app.open_tapview()
        user_font_size: '200sp'           
<Bye>:
    name: 'bye'
    MDFloatingActionButton:
        id: textview
        icon: 'plus'
        pos_hint: {'center_x':0.1,'center_y':0.1}
        on_release: root.manager.current = 'bye' 
        on_press : app.close_tapview()
        user_font_size: '45sp'
    
    MDFloatingActionButton:
        id: next
        icon: 'arrow-right'
        pos_hint: {'center_x':0.9,'center_y':0.1}
        disabled: True 
        user_font_size: '45sp'
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
        self.taptarget = MDTapTargetView(widget = self.help_str.get_screen('bye').ids.textview,title_text = 'text',widget_position = 'left_bottom', title_text_size ='20sp'
        ,description_text="GO next",outer_radius='80dp',description_text_color=[1, 0, 0, 0]
                                                ,outer_circle_alpha = 0.40,target_radius='40dp' )
        return screen

    def open_tapview(self):
        self.taptarget.start()
    def close_tapview(self):
        self.taptarget.stop()
        self.help_str.get_screen('bye').ids.next.disabled = False
               
DemoApp().run()