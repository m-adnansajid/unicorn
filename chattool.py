from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button

from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineAvatarIconListItem, TwoLineIconListItem

KV = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Chats"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "chats"
            
            OneLineListItem:
                text: "Status"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "status"

            OneLineListItem:
                text: "Contacts"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "contacts"
            
MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "UniCornChatTool"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "chats"
                MDGridLayout:
                    x: toolbar.height
                    size_hint_y: 1.0 - toolbar.height/root.height
                    cols: 2
                    row_force_default:True 
                    row_default_height: 40 
                    MDLabel:
                        text: "ProfilImg"
                    MDLabel:
                        text: "Own name" 
                    MDLabel:
                        text: ""
                    MDFillRoundFlatButton:
                        text: "Current state"
                    Widget:
                        id: separator
                        size_hint_y: None
                        height: 6
                        canvas:
                            Color:
                                rgb: 0.33, 0.33, 0.33
                            Rectangle:
                                pos: 0, separator.center_y - 0.1
                                size: 600, 2
                MDList:
                    id: scroll
                    TwoLineIconListItem:
                        text: "Contact 1"
                        secondary_text: "Last message here"

                        IconLeftWidget:
                            icon: "language-python" 
                    
                    TwoLineIconListItem:
                        text: "Contact 2"
                        secondary_text: "Last message here"

                        IconLeftWidget:
                            icon: "language-python" 
                   
                    TwoLineIconListItem:
                        text: "Contact 3"
                        secondary_text: "Last message here"

                        IconLeftWidget:
                            icon: "language-python"      
                                
                MDFloatingActionButton:
                    elevation: 8
                    icon: 'message'
                    pos_hint: {"center_x": 0.9, "center_y": .1}
                    on_press:
                        app.root.current = 'message'
                        root.manager.transition.direction = 'left'
                    
            MDScreen:
                name: "status"

                MDLabel:
                    text: "Status"
                    halign: "center"

            MDScreen:
                name: "contacts"

                MDLabel:
                    text: "Contacts"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

class ListItem(TwoLineIconListItem):
    icon = StringProperty("android")

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

Window.size = (600, 600)

class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)

    # def on_start(self):
    #     icons = list(md_icons.keys())
    #     for i in range(30):
    #         self.root.ids.scroll.add_widget(
    #             ListItem(text=f"Item {i}", secondary_text=f"Item {i}", icon=icons[i])
    #         )

TestNavigationDrawer().run()