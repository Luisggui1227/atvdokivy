from kivy.app import App
from kivy.uix.button import Button
class MyApp(App):
    def build(self):
        return Button(text='clique aqui!', size_hint=(0.5, 0.2))
if __name__ == '__main__':
    MyApp().run() 