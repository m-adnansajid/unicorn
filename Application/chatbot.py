from kivy.clock import Clock
from kivymd.app import  MDApp
from  kivy.lang import Builder
from  kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase
Window.size = (350, 550)
# main=Builder.load_string("""
# <MDScreen>:
#     name: "main"
#     bot_name: bot_name
#     MDFloatLayout:
#         md_bg_color: 1,1,1,1
#         Image:
#             source: "unicorn.jpg"
#             size_hint: .8, .5
#             pos_hint: {"center_x": .5, "center_y": .8}
#         MDLabel:
#             text: "Hello Sir!"
#             font_size: "35sp"
#             font_name: "Poppins-SemiBold.ttf"
#             pos_hint: {"center_x": .5, "center_y": .58}
#             halign: "center"
#             theme_text_color: "Color"
#             text_color: 53/255, 56/255, 60/255, 1
#         MDLabel:
#             text: "Your Digital Assistant to guide you through our Products & Services."
#             size_hint_x: .9
#             pos_hint: {"center_x": .5, "center_y": .58}
#             font_name: "Poppins"
#             font_size: "18sp"
#             halign: "center"
#             theme_text_color: "Color"
#             text_color: 53/255, 56/255, 60/255, 1
#         MDLabel:
#             text: "Read Me First"
#             font_name: "Poppins"
#             font_size: "18sp"
#             pos_hint: {"center_x": .5, "center_y": .33}
#             halign: "center"
#             underline: "True"
#             theme_text_color: "Custom"
#             text_color: 1/255, 170/255, 23/255, 1
#         MDFloatLayout:
#             sizehint: .85, .08
#             pos_hint: {"center_x": .5, "center_y": .33}
#             canvas:
#                 Color:
#                     rgb: (238/255, 238/255, 238/255, 1)
#                 RoundedRectangle:
#                     size: self.size
#                     pos: self.pos
#                     radius: [22,22,22,22]
#                     TextInput:
#                         id: bot_name
#                         hint_text: "Chatbot Name"
#                         size_hint: 1, None
#                         pos_hint: {"center_x": .5, "center_y": .5}
#                         font_size: "18sp"
#                         height: self.minimum_height
#                         cursor_color: 1, 170/255, 23/255, 1
#                         cursor_width: "2sp"
#                         foreground_color: 1, 170/255, 23/255, 1
#                         background_color: 0,0,0,0
#                         padding: 15
#                         font_name: "Poppins"
#         MDFloatLayout:
#             sizehint: .85, .08
#                 pos_hint: {"center_x": .5, "center_y": .1}
#                 canvas:
#                 Color:
#                     rgb: (1, 170/255, 23/255, 1)
#                 RoundedRectangle:
#                     size: self.size
#                     pos: self.pos
#                     radius: [22,22,22,22]
#         Button:
#             text: ""
#             size_hint: .45, .08
#             pos_hint: {"center_x": .5, "center_y": .1}
#             background_color: 0,0,0,0
#             on_release:
#                 app.bot_name()
#         MDLabel:
#             text: "LET'S CHAT"
#             halign: "center"
#             pos_hint: {"center_y": .1}
#             font_name: "Poppins-Semibold.ttf"
#             font_size: "18sp"
#             color: 1,1,1,1
#  """)

class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty
    font_name = "Poppins"
    font_size = 17


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty
    font_name = "Poppins"
    font_size = 17

class ChatBot(MDApp):

    def change_screen(self,name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        #screen_manager.add_widget(main)
        #screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats.kv"))
        return screen_manager

    def bot_name(self):
        if screen_manager.get_screen('main').bot_name.text != "":
            screen_manager.get_screen('chats').bot_name.text = screen_manager.get_screen('main').bot_name.text
            screen_manager.current = "chats"

    def response(self, *args):
        response = ""
        if value == "Hello" or value == "hello":
            response = f"Hello. I am you personal assistant {screen_manager.get_screen('chats').bot_name.text}."
        elif value == "How are you?" or "how are you?":
            response = "I'm doint well. Thanks!"
        else:
            response = "Sorry could you say that again?"
            screen_manager.get_screen('chats').chat_list.add_widget(Response(text=response, size_hint_x= .75))

    def send(self):
        global size, halign, value
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) < 6:
                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen_manager.get_screen('chats').chat_list.add_widget(Command(text=value, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response, 2)
            screen_manager.get_screen('chats').text_input.text= ""

if __name__ == '__main__':
    LabelBase.register(name="Poppins", fn_regular="Poppins-Regular.ttf")
    ChatBot().run()
