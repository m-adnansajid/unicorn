from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

KV = """
<Screen_1>:
    MDBottomNavigation:
        panel_color: .2, .2, .2, 1
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Scr1 Tab1'
            # on_enter: root.switch()     
            MDLabel:
                text: 'Screen_1 Tab_1'
                halign: 'center'
                
            Button:
                text: 'Screen_1 Tab_1'
                on_release: root.manager.current = 'screen_2'                   
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Scr1 Tab2'
            on_enter: root.switch()     
            MDLabel:
                text: 'Screen_1 Tab_2 -> Go to Screen_2'
                halign: 'center'
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Scr1 Tab3'
            MDLabel:
                text: 'Screen_1 Tab_3'
                halign: 'center'

<Screen_2>:
    MDBottomNavigation:
        panel_color: .8, .8, .8, 1
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Scr2 Tab1'
            # on_enter: root.switch()     
            MDLabel:
                text: 'Screen_2 Tab_1'
                halign: 'center'                   
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Scr2 Tab2'
            on_enter: root.switch()     

            MDLabel:
                text: 'Screen_2 Tab_2 -> Go to Screen_1'
                halign: 'center'
# <Manager>:
#     id: screen_manager
#     screen_1: screen_1 
#     screen_2: screen_2
#     
#     Screen_1:
#         id: screen_1
#         name: 'screen_1'
#         manager: screen_manager
#     Screen_2:
#         id: screen_2
#         name: 'screen_2'
#         manager: screen_manager


"""


class Screen_1(Screen):
    def switch(self):
        self.parent.current = 'screen_2'


class Screen_2(Screen):
    def switch(self):
        self.parent.current = 'screen_1'


class Manager(ScreenManager):
    # screen_1 = ObjectProperty(None)
    # screen_2 = ObjectProperty(None)
    pass


class MainApp(MDApp):
    # dialog = None

    def build(self):
        Builder.load_string(KV)
        sm = Manager()
        sm.add_widget(Screen_1(name='screen_1'))
        sm.add_widget(Screen_2(name='screen_2'))
        sm.current = 'screen_2'
        return sm


MainApp().run()