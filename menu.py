from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        layout_principal = GridLayout(cols=2)
        coluna_esquerda = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        menu_itens = ['Arquivo', 'Editor', 'Seleção', 'ver', 'Acessar', 'Sair']
        label1 = Label(text='Menu')
        coluna_esquerda.add_widget(label1)
        for item in menu_itens:
            botao = Button(text=item)
            coluna_esquerda.add_widget(botao)
        coluna_direita = GridLayout(cols=1, rows=3)
        for i in range(3):
            botao = Button(text=f'Botão {i+7}')
            coluna_direita.add_widget(botao)
        layout_principal.add_widget(coluna_esquerda)
        layout_principal.add_widget(coluna_direita)

        return layout_principal

if __name__ == "__main__":
    MinhaApp().run()
