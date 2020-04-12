from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition
import datetime

class StartScreen(Screen):
    pass
class HomeScreen(Screen):
    pass
class SecondScreen(Screen):
    pass

GUI = Builder.load_file("aukcioner.kv")

class MainApp(App):
    def build(self):
        self.count = -1
        return GUI
    def change_screen(self, screen_name):
        tr = NoTransition()
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.transition = tr
        screen_manager.current = screen_name
    def change_text(self, label_text):
        second_screen = self.root.ids["second_screen"]
        menu_label = second_screen.ids["menu_label"]
        menu_label.text = label_text
    def change_name(self, label_name):
        home_screen = self.root.ids["home_screen"]
        menu_name = home_screen.ids["menu_name"]
        menu_name.text = label_name
    def change_time(self):
        home_screen = self.root.ids["home_screen"]
        self.menu_time = home_screen.ids["menu_time"]
        self.menu_time.text = str(datetime.date.today())
    def change_count(self):
        home_screen = self.root.ids["home_screen"]
        menu_count = home_screen.ids["menu_count"]
        self.count += 1
        menu_count.text = str(self.count)

MainApp().run()
