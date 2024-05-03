from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label

class RotuloApp(App):
    def build(self):
      layout = BoxLayout(orientation='vertical', padding=20)
      slider = Slider(min=0, max=100, value=50, step=1)
      slider.bind(value=self.atualizar_label)
      self.label = Label(text="valor do slider: {}".format(int(slider.value)))
       
      layout.add_widget(slider)
      layout.add_widget(self.label)

      return layout
    
    def atualizar_label(self, instance, valor):
       self.label.text = "valor do slider: {}".format(int(valor))
    
if __name__ == '__main__':
    RotuloApp().run()