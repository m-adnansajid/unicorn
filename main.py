from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder

Window.size = (350, 550)


class MenuScreen(Screen):
    pass


class ChatApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "LightGreen"
        return Builder.load_file('main.kv')

    def callback(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.current = 'menu'
        return sm

if __name__ == '__main__':
    ChatApp().run()
