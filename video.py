from kivy.app import App
from kivy.uix.video import Video
class MyApp(App):
    def build(self):
        return Video(source='caminho/para/seu/video.mp4')
if __name__ == '__main__':
    MyApp().run() 