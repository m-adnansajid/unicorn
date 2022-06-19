from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

class MainWindow(MDScreen):
    pass

# Status anpassen
class SecondWindow(MDScreen):
    pass

class RegisterWindow(MDScreen):
    pass

class ContactMgmt(MDScreen):
    pass


kv = Builder.load_file("home.kv")

class MyMainApp(MDApp):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()