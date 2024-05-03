from kivy.app import App
from kivy.uix.image import Image
class MyApp(App):
    def build(self):
        return Image(source='')
if __name__ == '__main__':
    MyApp().run() 