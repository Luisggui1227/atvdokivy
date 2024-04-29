from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RotuloApp(App):
    def build(self):
      layout = BoxLayout(orientation='vertical')
      self.lab1 = Label(
         text='Senai', color=[1, 0, 0, 1],
         font_size=40, bold=True
   )
      self.lab2 = Label(
        text='Sesi', color=[0, 1, 0, 1],
        font_size=40, italic=True
    )
      self.lab3 = Label(
      text='Enem', color=[0, 0, 1, 1],
      font_size=40, font_name='Arial',
      underline=True
   )        
      layout.add_widget(self.lab1)
      layout.add_widget(self.lab2)
      layout.add_widget(self.lab3)
      return layout
    
if __name__ == '__main__':
    RotuloApp().run()