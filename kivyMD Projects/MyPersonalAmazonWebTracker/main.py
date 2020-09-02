from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.button import MDFlatButton,MDIconButton,MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from helper import code_helper
from kivymd.uix.snackbar import Snackbar

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.taptargetview import MDTapTargetView

Window.size = (400,600)


class WelcomeScreen(Screen):
    pass


class AndroidInfo(Screen):
    pass


class UsernameScreen(Screen):
    pass

class UsernameHelper(Screen):
    pass


class dobscreen(Screen):
    pass

class DobHelper(Screen):
    pass

class AssistantWelcome(Screen):
    pass

class FinalWelcome(Screen):
    pass

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'firstwelcome'))
sm.add_widget(AndroidInfo(name = 'androidinfo'))
sm.add_widget(AssistantWelcome(name = 'assistantwelcome'))
sm.add_widget(UsernameScreen(name = 'usernamescreen'))
sm.add_widget(UsernameHelper(name = 'usernamehelper'))
sm.add_widget(dobscreen(name = 'dobentered'))
sm.add_widget(DobHelper(name = 'dobhelper'))
sm.add_widget(FinalWelcome(name = 'finalwelcome'))

class AmazonApp(MDApp):
    
    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Light"
        self.helper_string = Builder.load_string(code_helper)
        screen.add_widget(self.helper_string)
        self.skip_target_view = MDTapTargetView(
                                                widget=self.helper_string.get_screen('firstwelcome').ids.welcome_skip,
                                                title_text="Next",widget_position="left_bottom",title_text_size="20sp",
                                                description_text="GO next",outer_radius='80dp',description_text_color=[1, 0, 0, 0]
                                                ,outer_circle_alpha = 0.40,target_radius='40dp')
        self.android_target_view = MDTapTargetView(
                                                widget=self.helper_string.get_screen('androidinfo').ids.android_info,
                                                title_text="Hey!!",widget_position="center",title_text_size="20sp",title_position="right_top",
                                                description_text="I am your assistant\nClick on me",outer_radius='180dp',description_text_color=[0,0,0,1]
                                                ,outer_circle_alpha = 0.5,target_radius='50dp')
        self.skip_target_view.start()
        self.android_target_view.start()

        #self.dob initialize
        self.dob_entered= True
        return screen
    
    
    def theme_switcher(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"
    
    
    
    def tap_target_stop(self):
        self.skip_target_view.stop()


    def android_info_targerview_stop(self):
        self.android_target_view.stop()

    

    def help_chip(self, instance, value):
        help_cancel_btn_first = MDIconButton(icon = 'checkbox-marked-circle-outline',on_release = self.help_close_dialog_btn)
        self.help_dialog = MDDialog(title = 'Help',
                               text = 'Little android is your assistant\nClick the android for more Info',
                               size_hint = (0.7,0.1),buttons = [help_cancel_btn_first])
        self.help_dialog.open()

    def help_close_dialog_btn(self,obj):
        self.help_dialog.dismiss()


    def username_checker(self):
        username_check_false = True
        username_text_data = self.helper_string.get_screen('usernamescreen').ids.username_text.text
        # print(username_text_data)
        try:
            int(username_text_data)
        except:
            username_check_false = False
        if username_check_false or username_text_data.split()==[]:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.username_dialoge = MDDialog(title = 'Invalid Username',text = 'Please Enter a valid Username',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.username_dialoge.open()
        else:
            screen_usernamescreen = self.helper_string.get_screen('usernamescreen')
            screen_usernamescreen.ids.username_enter.disabled = False
            screen_usernamescreen.ids.username_check_extra_button.icon = 'account-check-outline'
            screen_usernamescreen.ids.username_check_btn.text_color = [1,1,1,0]
            screen_usernamescreen.ids.username_check_btn.md_bg_color =[1,1,1,0]
            screen_usernamescreen.ids.username_check_extra_button.text_color = self.theme_cls.primary_color
            screen_usernamescreen.ids.username_check_extra_button.pos_hint = {'center_x':0.5,'center_y':0.62}
            screen_usernamescreen.ids.username_check_extra_button.user_font_size = '60sp'



    def close_username_dialog(self,obj):
        self.username_dialoge.dismiss()


    
# DOB Picker
#self.dob for Date of birth



    def show_date_picker(self):
        date_dialog = MDDatePicker(
            callback=self.get_date,
            year=1999,
            month=1,
            day=1,
        )
        date_dialog.open()

    def get_date(self, date):
        self.dob = date
        dob_input_screen_selector = self.helper_string.get_screen('dobinput')
        #here i put the next button disbaled as False so user can enter in that window
        dob_input_screen_selector.ids.dob_enter.disabled = False
        dob_input_screen_selector.ids.account_shield.icon = 'shield-account'
        dob_input_screen_selector.ids.dob.text = str(self.dob)
        dob_input_screen_selector.ids.secure.text_color = [0,1,0,0.7]
AmazonApp().run()