from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.app import App
# BEISPIELE
#https://likegeeks.com/kivy-tutorial/
class KivyButton():

    def build(self):
        return Button(text="Welcome to UniCornChat!", pos=(300, 350), size_hint=(.25, .18))
        # return Label(text="Hello Kivy!")


KivyButton().run()
