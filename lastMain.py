from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder

Window.size = (350, 550)


class HomeScreen(Screen):
    pass


class ContactScreen(Screen):
    pass


class StatusScreen(Screen):
    pass


class ChatScreen(Screen):
    pass


class RegisterScreen(Screen):
    pass


class Manager(ScreenManager):
    pass


class Test(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        Builder.load_file('main.kv')
        sm = Manager()
        sm.add_widget(HomeScreen(name='home_screen'))
        sm.add_widget(ContactScreen(name='contact'))
        sm.add_widget(StatusScreen(name='status'))
        sm.add_widget(ChatScreen(name='chat'))
        sm.add_widget(RegisterScreen(name='register'))
        return


Test().run()
