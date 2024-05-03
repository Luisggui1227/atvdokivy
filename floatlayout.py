from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        layout_float = FloatLayout()

        botao = Button(text='clique Aqui', size_hint=(None, None), size=(100, 50), pos_hint={'x':0.5, 'y':0.5})
        layout_float.add_widget(botao)

        return layout_float


MyApp().run()