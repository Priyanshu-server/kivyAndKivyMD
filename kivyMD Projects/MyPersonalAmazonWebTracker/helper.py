code_helper = """
ScreenManager:
    WelcomeScreen:
    AndroidInfo:
    AssistantWelcome:
    UsernameScreen:
    UsernameHelper:
    dobscreen:
    DobHelper:
    FinalWelcome:
    


<WelcomeScreen>:
    name: 'firstwelcome'
    MDLabel:
        text: 'Welcome'
        pos_hint: {'center_y':0.8}
        halign: 'center'
        font_style: 'H2'
    MDLabel:
        text: 'to'
        pos_hint: {'center_y':0.65}
        halign: 'center'
        font_style: 'H3'
    MDLabel:
        text: 'Amazon Price Tracker'
        pos_hint: {'center_y':0.5}
        halign: 'center'
        font_style: 'H4'
    MDProgressBar:
        value: 20
        id: progress
        pos_hint: {'center_y':0.02}
        type: "indeterminate"
    MDFloatingActionButton:
        id : welcome_skip
        icon: "arrow-down"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.25}
        on_press: app.tap_target_stop()
        user_font_size: "50sp"
        on_release :
            root.manager.current = 'androidinfo'
            root.manager.transition.direction = 'up'

<AndroidInfo>:
    name: 'androidinfo'
    
    MDIconButton:
        id : android_info
        icon: "android"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: app.android_info_targerview_stop()
        user_font_size: "80sp"
        on_release :
            root.manager.current = 'assistantwelcome'
            root.manager.transition.direction = 'up'
    MDFloatingActionButton:
        id : welcome_back
        icon: "arrow-up"
        pos_hint: {'center_x':0.15,'center_y':0.11}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "38sp"
        on_release :
            root.manager.current = 'firstwelcome'
            root.manager.transition.direction = 'down'
    MDFloatingActionButton:
        id : username_enter 
        icon: "arrow-right"
        pos_hint: {'center_x':0.83,'center_y':0.11}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "43sp"
        on_release:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value: 40
        pos_hint: {'center_y':0.02}


<AssistantWelcome>:
    name: 'assistantwelcome'
    #:import Snackbar kivymd.uix.snackbar.Snackbar
    MDBackdrop:
        header: ''
        radius: 21
        id: backdrop
        title:'Hello!! I am your assistant'
        left_action_items: [['menu-open',lambda x: self.open()]]
        right_action_items: [['android',lambda x: self.open()]]
        # background_color: [0,1,0,0.7]
        specific_text_color: app.theme_cls.primary_color

        MDBackdropBackLayer:
            
            FloatLayout:
                orientation: 'vertical'
                MDLabel:
                    text:'android'
                    halign:'center'
                    font_style: 'H2'
                MDIconButton:
                    icon: 'android'
                    pos_hint: {'center_x':0.5,'center_y':0.65}
                    user_font_size: "120sp"

        MDBackdropFrontLayer:
            
            
            BoxLayout:
                orientation:'vertical'
                FloatLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: 'close'
                        pos_hint: {'center_x':0.94,'center_y':0.15}
                        user_font_size: "47sp"
                        on_release:
                            root.manager.current = 'usernamescreen'
                            root.manager.transition.direction = 'down'
            FloatLayout:
                orientation:'vertical'
                MDCard:
                    orientation: "vertical"
                    padding: "8dp"
                    size_hint: None, None
                    size: "253dp", "180dp"
                    pos_hint: {"center_x": .01, "center_y": .6}

                    MDLabel:
                        text: "Info"
                        theme_text_color: "Primary"
                        size_hint_y: None
                        font_style: 'H5'
                        height: self.texture_size[1]

                    MDSeparator:
                        height: "1dp"

                    MDLabel:
                        text: "I am your assistant you can use me anytime by clicking on me, if you want to see me then click on the left-top menu bar"
                    MDSeparator:
                        height: "1dp"

                    MDRectangleFlatButton:
                        pos_hint:{'center_x':0.45}
                        text:'more'
                        on_release : Snackbar(text="Hi!! How are you doing??").show()
<UsernameScreen>:
    name: 'usernamescreen'
    MDLabel:
        text: 'User Info'
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H3'
    MDFloatingActionButton:
        id : welcome_back
        icon: "arrow-up"
        pos_hint: {'center_x':0.15,'center_y':0.1}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "35sp"
        on_release :
            root.manager.current = 'firstwelcome'
            root.manager.transition.direction = 'down'
            

            

    MDIconButton:
        id : username_enter
        icon: "android"
        pos_hint: {'center_x':0.48,'center_y':0.069}
        # md_bg_color: app.theme_cls.primary_color
        user_font_size: "115sp"
        on_release :
            root.manager.current = 'usernamehelper'
            root.manager.transition.direction = 'up'
    
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


    MDChip:
        label: 'Help'
        color: 0,0.5,0,0.7
        icon: 'help'
        pos_hint: {'center_x':0.14,'center_y':0.35}
        callback: app.help_chip

    
    MDRoundFlatIconButton:
        text: 'Theme'
        icon: 'theme-light-dark'
        pos_hint: {'center_x':0.213,'center_y':0.42}
        font_size: '18sp'
        on_release: app.theme_switcher()

    MDFloatingActionButton:
        id : username_enter 
        disabled: True
        icon: "arrow-right"
        pos_hint: {'center_x':0.83,'center_y':0.11}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "43sp"
        on_release:
            root.manager.current = 'dobinput'
            root.manager.transition.direction = 'left'
    MDIconButton:
        id : username_check_extra_button
        icon: "reload"
        pos_hint: {'center_x':0.69,'center_y':0.62}
        theme_text_color: "Custom"
        text_color: [0,0,0,0]
        user_font_size: "40sp"
            
    MDRoundFlatButton:
        id: username_check_btn
        text: 'Check'

        pos_hint: {'center_x':0.5,'center_y':0.62}
        font_size: '23sp'
        on_release: app.username_checker()
    
    MDProgressBar:
        value: 60
        pos_hint: {'center_y':0.02}



<UsernameHelper>:
    name: 'usernamehelper'
    #:import Snackbar kivymd.uix.snackbar.Snackbar
    MDBackdrop:
        header: ''
        radius: 21
        id: backdrop
        title:'Hello!! I am your assistant'
        left_action_items: [['menu-open',lambda x: self.open()]]
        right_action_items: [['android',lambda x: self.open()]]
        # background_color: [0,1,0,0.7]
        specific_text_color: app.theme_cls.primary_color

        MDBackdropBackLayer:
            FloatLayout:
                orientation: 'vertical'
                MDLabel:
                    text:'android'
                    halign:'center'
                    font_style: 'H2'
                MDIconButton:
                    icon: 'android'
                    pos_hint: {'center_x':0.5,'center_y':0.65}
                    user_font_size: "120sp"

        MDBackdropFrontLayer:
            BoxLayout:
                orientation:'vertical'
                FloatLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: 'close'
                        pos_hint: {'center_x':0.94,'center_y':0.15}
                        user_font_size: "47sp"
                        on_release :
                            root.manager.current = 'usernamescreen'
                            root.manager.transition.direction = 'down'
                        
            FloatLayout:
                orientation:'vertical'
                MDCard:
                    orientation: "vertical"
                    padding: "8dp"
                    size_hint: None, None
                    size: "253dp", "150dp"
                    pos_hint: {"center_x": .05, "center_y": .6}

                    MDLabel:
                        text: "Username"
                        theme_text_color: "Primary"
                        size_hint_y: None
                        font_style: 'H5'
                        height: self.texture_size[1]

                    MDSeparator:
                        height: "1dp"

                    MDLabel:
                        text: "Username is must so we can intract with you"
                    MDSeparator:
                        height: "1dp"

                    MDRectangleFlatButton:
                        pos_hint:{'center_x':0.45}
                        text:'more'
                        on_release : Snackbar(text="You can change your username later").show()


<dobscreen>:
    name:'dobinput'
    #:import Snackbar kivymd.uix.snackbar.Snackbar
    MDLabel:
        text: 'Date Of Birth'
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H3'
    MDRoundFlatButton:
        id : dob
        text: 'Select'   
        pos_hint: {'center_x':0.5,'center_y':0.5}
        font_size: '30sp'
        on_release : app.show_date_picker()
    
    MDIconButton:
        id : username_enter
        icon: "android"
        pos_hint: {'center_x':0.48,'center_y':0.069}
        # md_bg_color: app.theme_cls.primary_color
        user_font_size: "115sp"
        on_release :
            root.manager.current = 'dobhelper'
            root.manager.transition.direction = 'up'
    
    MDFloatingActionButton:
        icon: "arrow-left"
        pos_hint: {'center_x':0.15,'center_y':0.1}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "35sp"
        on_release :
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'right'

    MDFloatingActionButton:
        icon: "arrow-right"
        disabled: True
        id : dob_enter 
        pos_hint: {'center_x':0.83,'center_y':0.11}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "43sp"
        on_release:
            root.manager.current = 'finalwelcome'
            root.manager.transition.direction = 'left'

    MDIconButton:
        id: secure
        icon : 'pirate'
        pos_hint: {'center_x':0.5,'center_y':0.35}
        user_font_size: "50sp"
        theme_text_color: "Custom"
        text_color: [1,0,0,1]
    MDIconButton:
        id: account_shield
        icon: 'account-circle'
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.7}
        user_font_size: "110sp"



    MDProgressBar:
        value: 80
        pos_hint: {'center_y':0.02}




<DobHelper>:
    name: 'dobhelper'
    #:import Snackbar kivymd.uix.snackbar.Snackbar
    MDBackdrop:
        header: ''
        radius: 21
        id: backdrop
        title:'Hello!! I am your assistant'
        left_action_items: [['menu-open',lambda x: self.open()]]
        right_action_items: [['android',lambda x: self.open()]]
        # background_color: [0,1,0,0.7]
        specific_text_color: app.theme_cls.primary_color

        MDBackdropBackLayer:
            FloatLayout:
                orientation: 'vertical'
                MDLabel:
                    text:'android'
                    halign:'center'
                    font_style: 'H2'
                MDIconButton:
                    icon: 'android'
                    pos_hint: {'center_x':0.5,'center_y':0.65}
                    user_font_size: "120sp"

        MDBackdropFrontLayer:
            BoxLayout:
                orientation:'vertical'
                FloatLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: 'close'
                        pos_hint: {'center_x':0.94,'center_y':0.15}
                        user_font_size: "47sp"
                        on_release :
                            root.manager.current = 'dobinput'
                            root.manager.transition.direction = 'down'
                        
            FloatLayout:
                orientation:'vertical'
                MDCard:
                    orientation: "vertical"
                    padding: "8dp"
                    size_hint: None, None
                    size: "253", "150dp"
                    pos_hint: {"center_x": .05, "center_y": .6}

                    MDLabel:
                        text: "Date Of Birth"
                        theme_text_color: "Primary"
                        size_hint_y: None
                        font_style: 'H5'
                        height: self.texture_size[1]

                    MDSeparator:
                        height: "1dp"

                    MDLabel:
                        text: "DOB is must so we can suggest you accordingly"
                    MDSeparator:
                        height: "1dp"

                    MDRectangleFlatButton:
                        pos_hint:{'center_x':0.45}
                        text:'more'
                        on_release : Snackbar(text="You can't change your DOB later").show()




<FinalWelcome>:
    name: 'finalwelcome'
    MDLabel:
        text: 'Account Setup Complete'
        halign: 'center'
        font_style: 'H3'

    MDFloatingActionButton:
        icon: 'account-check'
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.78}
        user_font_size : '145sp'

    MDIconButton:
        icon: "location-enter"
        pos_hint: {'center_x':0.5,'center_y':0.25}
        user_font_size : '140sp'
        # md_bg_color: app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        
    # MDRectangleFlatButton:
    #     text: "Let's Go"
    #     pos_hint: {'center_x':0.5,'center_y':0.085}
    #     user_font_size : '70sp'


"""