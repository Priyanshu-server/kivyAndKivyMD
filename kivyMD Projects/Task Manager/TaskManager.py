from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import OneLineListItem

Buil_strng ='''
ScreenManager:
    First:
    Second:

<First>:
    name:'first'
    MDLabel:
        text:'Task'
        halign: 'center'
        font_style: 'H2'
        pos_hint:{'center_y':0.8}
    MDTextField:
        id : task_text
        size_hint:(0.7,0.1)
        pos_hint:{'center_x':0.5,'center_y':0.55}
        hint_text:'Enter your task '

    
    MDRaisedButton:
        text:'Add task'
        pos_hint: {'center_x':0.5,'center_y':0.35}
        on_press:
            app.addTask()
<Second>:
    name: 'second'
    ScrollView:
        MDList:
            id:task_items

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x':0.3,'center_y':0.2}
        on_press:
            root.manager.current = 'first'

'''
class First(Screen):
    pass
class Second(Screen):
    pass


sm = ScreenManager()
sm.add_widget(First(name = 'first'))
sm.add_widget(Second(name = 'second'))


class NewApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(Buil_strng)
        return self.strng

    def addTask(self):
        self.task_text = self.strng.get_screen('first').ids.task_text.text
        if self.task_text.split() != []:
            self.strng.get_screen('second').manager.current = 'second'
            self.strng.get_screen('second').ids.task_items.add_widget(
                OneLineListItem(text = self.task_text)
            )
        else:
            Snackbar(text = 'Task is Empty').show()
    


NewApp().run()