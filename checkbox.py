from kivy.app import App
from kivy.uix.checkbox import CheckBox
class MyApp(App):
    def build(self):
        return CheckBox(active=False)
if __name__ == '__main__':
    MyApp().run() 