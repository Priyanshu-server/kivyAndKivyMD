from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
#Builder String
helper_string = '''
ScreenManager:
    Hello:
    Bye:

<Hello>:
    name: 'hello'
    
    MDLabel:
        id: text_change
        text: 'Hello!! world'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color : 148/255,0,211/255,1
        font_style : 'H1'
    
    MDRectangleFlatIconButton:
        icon: 'android'
        text: 'Hello'
        user_font_size: '100sp'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_release:
            root.manager.current = 'bye'
            root.manager.transition.direction = 'left'

    MDRectangleFlatButton:
        text: 'theme changer'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_release: app.theme_changer()

    MDRectangleFlatButton:
        text: 'Property changer'
        pos_hint: {'center_x':0.8,'center_y':0.7}
        on_release: app.property_changer()




<Bye>
    name: 'bye'
    MDLabel: 
        text: 'Good Bye'
    MDIconButton:
        icon:'android'
        on_release: app.username_checker()

    MDTextField:
        id: username_text
        hint_text: "Enter Username"
        color_mode: 'custom'
        line_color_normal: app.theme_cls.primary_color
        line_color_focus: 0,0.5,0,1
        helper_text: "Required"
        helper_text_mode: "on_error"
        # mode: "rectangle"
        icon_right: 'account'
        icon_right_color: 0,0.5,0,0.9
        pos_hint: {'center_x':0.5,'center_y':0.7}
        required: True
        size_hint: (0.8,0.1)



'''
class Hello(Screen):
    pass
class Bye(Screen):
    pass

sm = ScreenManager()

sm.add_widget(Hello(name = 'hello'))
sm.add_widget(Bye(name='bye'))

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        # self.theme_cls.primary_hue = 500
        screen = Screen()

        self.help_str = Builder.load_string(helper_string)

        screen.add_widget(self.help_str)
        return screen

    def theme_changer(self):
        if self.theme_cls.theme_style=='Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'
    def property_changer(self):
        self.help_str.get_screen('hello').ids.text_change.text = 'Bye!! World'
    
    def username_checker(self):
            username_check_false = True
            username_text_data = self.help_str.get_screen('bye').ids.username_text.text
            # print(username_text_data)
            try:
                int(username_text_data)
            except:
                username_check_false = False
            if username_check_false or username_text_data.split()==[]:
                cancel_btn = MDFlatButton(text='Retry',on_release=self.close_dialog)
                self.username_dialog = MDDialog(title = 'Invalid Username',text = 'Please eneter a valid username',size_hint = (0.5,0.2), buttons = [cancel_btn] )
                self.username_dialog.open()
    def close_dialog(self,obj):
        self.username_dialog.dismiss()
DemoApp().run()