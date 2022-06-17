from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Video about navigation between screens
#https://www.youtube.com/watch?v=xaYn4XdieCs

# Video about popups
# https://www.youtube.com/watch?v=PpLuyOzCKTQ

# Home -> letzen Kontakte?
class MainWindow(Screen):
    pass

# Status anpassen
class SecondWindow(Screen):
    pass

class RegisterWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()




























# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.button import Button
#
# from kivy.app import App
#
# from kivy.uix.boxlayout import BoxLayout
#
# from kivy.lang import Builder
#
# Builder.load_string("""
#
# <KivyButton>:
#
#     Button:
#
#         text: "Hello Button!"
#
#         size_hint: .12, .12
#
#         Image:
#
#             source: 'images.jpg'
#
#             center_x: self.parent.center_x
#
#             center_y: self.parent.center_y
#
# """)
#
#
# class KivyButton(App, BoxLayout):
#
#     def build(self):
#         return self
#
#
# KivyButton().run()
# # class FirstKivy(App):
# #     def build(self):
# #         return Button(text="Welcome to UniCornChat!", pos=(300, 350), size_hint=(.25, .18))
# #         # return Label(text="Hello Kivy!")
# #
# #
# # FirstKivy().run()

