from kivy.app import App 
from kivy.uix.label import Label
from kivy.core.window import Window 

class MinhaApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        label = Label(text='Esta é uma tela com fundo branco',color=(0, 0, 0, 1))

        return label
    
if __name__ == "__main__":
    MinhaApp().run()