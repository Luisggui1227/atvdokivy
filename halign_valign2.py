from kivy.app import App
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        return Label(
            text='Oi, Sesi',
            halign='left',
            valign='top',
            size_hint=(None, None),
            size=(900, 50),
            text_size=(150, None)
        )
    
if __name__ == '__main__':
    MinhaApp().run()    