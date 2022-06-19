import kivymd
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
register_form_helper = """
MDBoxLayout:
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(20)

    # MDToolbar:
    #     title: "UniCorn Chat"
    #     md_bg_color: app.theme_cls.primary_color
    #     elevation: 10
    #     left_action_items: [['menu', lambda x: x]]

    MDTextField:
        hint_text: "Enter name"
        icon_right: "text"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300

    MDTextField:
        hint_text: "Enter surname"
        icon_right: "text"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300

    MDTextField:
        hint_text: "Enter number"
        icon_right: "cellphone"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300

    MDFloatingActionButtonSpeedDial:
        data: {'Top Priority': 'priority-high', 'Low Priority': 'priority-low', 'Accomplished': 'check'}
        rotation_root_button: True
        callback: app.call

    MDFloatingActionButton:
        icon: 'priority-high'
        pos_hint: {"center_x": 0.2, "center_y": .9}
        size_hint_x: None
        width: 200
"""

class DemoApp(MDApp):
    call = "hi"

    def build(self):
        screen = Screen()
        # This is to change the color_theme
        self.theme_cls.primary_palette = "Green"
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Amber"
        # self.theme_cls.primary_hue = "A700
        # username = MDTextField(text='Enter username',
        #                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                        size_hint_x=None, width=300)
        register_form = Builder.load_string(register_form_helper)
        screen.add_widget(register_form)
        return screen

DemoApp().run()
