from kivy.app import App
from kivy.uix.image import Image, AsyncImage
class MyApp(App):
    def build(self):
        return AsyncImage(source='https://correiodecarajas.com.br/wp-content/uploads/2024/04/gabi.webp')
if __name__ == '__main__':
    MyApp().run() 