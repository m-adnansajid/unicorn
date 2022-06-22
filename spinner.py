from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('spinner.kv')


class MDScreen(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f'Current State {value}'


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
