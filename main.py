from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition

class StartScreen(Screen):
    pass
class HomeScreen(Screen):
    pass
class SecondScreen(Screen):
    pass

GUI = Builder.load_file("aukcioner.kv")

class MainApp(App):
    def build(self):
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

MainApp().run()
