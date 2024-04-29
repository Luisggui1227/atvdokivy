from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='clique aqui', font_size=50)

if __name__ == '__main__':
    MyApp().run()    