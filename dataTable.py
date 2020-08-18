from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
#Builder String
helper_string = '''
ScreenManager:
    Hello:
    Bye:

<Hello>:
    name: 'hello'

<Bye>:
    name: 'bye'
    MDLabel:
        id : tex
        text: "Username"


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



        table = MDDataTable(pos_hint = {'center_x':0.5,'center_y':0.5},size_hint = (0.9,0.6),check = True,rows_num=7,
                        column_data =[
                                    ("Food",dp(30)),
                                    ('Calories',dp(30)),
                                    ('Price',dp(30)),
                                    ('Must-Buy ?',dp(30)) ],
                        row_data = [
                                    ("Apple","300",'50','No'),
                                    ("Mango","300",'50','No'),
                                    ("Banana","300",'50','No'),
                                    ("Apple","300",'50','No'),
                                    ("Apple","300",'50','No'),
                                    ("Apple","300",'50','No'),
                                    ("Apple","300",'50','No'),
                                    ("Apple","300",'50','No'),] )
        table.bind(on_check_press = self.check_press)
        table.bind(on_row_press = self.row_press)

        self.help_str.get_screen('hello').add_widget(table)
        return screen
    def check_press(self,instance_table,current_row):
        print(current_row)
        self.help_str.get_screen('bye').ids.tex.text = current_row[0]
        self.help_str.get_screen('bye').manager.current = 'bye'
    def row_press(self,instance_table,current_row):
        pass
            
               
DemoApp().run()