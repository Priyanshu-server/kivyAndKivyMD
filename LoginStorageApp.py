from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.picker import MDDatePicker

helpstr = '''
ScreenManager:
    WelcomeScreen:
    UsernameScreen:
    DOB:
    MainScreen:


<WelcomeScreen>:
    name : 'welcomescreen'
    MDLabel:
        text:'Welcome Screen'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_y':0.65}
    MDFloatingActionButton:
        icon:'android'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '60sp'
        pos_hint: {'center_x':0.5,'center_y':0.32}
        on_press:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'

    MDProgressBar:
        value:30
        pos_hint:{'center_y' : 0.02}
<UsernameScreen>
    name:'usernamescreen'
    MDFloatingActionButton:
        icon: 'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'welcomescreen'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        id:disabled_button
        disabled: True
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'dob'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value:60
        pos_hint: {'center_y':0.02}

    MDLabel:
        text:'Username'
        font_style: 'H2'
        halign: 'center'
        pos_hint : {'center_y':0.85}

    MDTextField:
        id:username_text_fied
        pos_hint: {'center_x':0.5,'center_y':0.6}
        size_hint: (0.7,0.1)
        hint_text : 'username'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required : True

    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.35}
        user_font_size: '50sp'
        on_press: app.check_username()

<DOB>:
    name:'dob'
    MDLabel:
        text:'Date of Birth'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_y':0.75} 

    MDRaisedButton:
        id:date_picker
        text:'Date Picker'
        user_font_size : '70sp'
        pos_hint : {'center_x':0.5,'center_y':0.6}
        on_press:
            app.show_date_picker()

    MDFloatingActionButton:
        icon:'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size: '45sp'
        on_press: root.manager.current = 'usernamescreen'
    MDFloatingActionButton:
        id: second_disabled
        disabled: True
        icon:'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size: '45sp'
        on_press: root.manager.current = 'mainscreen'
    
<MainScreen>:
    name : 'mainscreen'
    MDLabel:
        id:profile_name
        text:'main screen'
        font_style : 'H2'
        halign : 'center'
        pos_hint : {'center_y':0.7}
    

'''
class WelcomeScreen(Screen):
    pass
class UsernameScreen(Screen):
    pass
class DOB(Screen):
    pass
class MainScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(UsernameScreen(name = 'usernamescreen'))
sm.add_widget(DOB(name = 'dob'))
sm.add_widget(MainScreen(name = 'main_screen'))
class NewApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(helpstr)
        return self.strng

    def check_username(self):
        self.username_text = self.strng.get_screen('usernamescreen').ids.username_text_fied.text
        username_check_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.username_text.split() == []:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Invalid Username',text = "Please input a valid username",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()

        else:
            self.strng.get_screen('usernamescreen').ids.disabled_button.disabled = False

    def close_username_dialogue(self,obj):
        self.dialog.dismiss()

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback = self.get_date,year = 1999,month = 1,day =1,)
        date_dialog.open()
    def get_date(self,date):
        self.dob = date
        self.strng.get_screen('dob').ids.date_picker.text = str(self.dob)
        self.strng.get_screen('dob').ids.second_disabled.disabled = False

        #Storing of DATA
        self.store.put('UserInfo',name = self.username_text,dob = str(self.dob))
        self.username_changer()

    def username_changer(self):
        self.strng.get_screen('mainscreen').ids.profile_name.text = f"Welcome {self.store.get('UserInfo')['name']}"

    def on_start(self):
        self.store = JsonStore("userProfile.json")
        try:
            if self.store.get('UserInfo')['name'] != "":
                self.username_changer()
                self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
                
        except KeyError:
            self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'


NewApp().run()