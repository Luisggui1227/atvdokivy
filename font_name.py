from kivy.app import App
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        return Label(text='Oi, Sesi', font_size=100, font_name='Arial')
    
if __name__ == '__main__':
    MinhaApp().run()    