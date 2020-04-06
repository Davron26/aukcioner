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
tr = NoTransition()
class MainApp(App):
    def build(self):
        return GUI
    def change_screen(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.transition = tr
        screen_manager.current = screen_name


MainApp().run()
