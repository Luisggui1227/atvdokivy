from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class RotuloApp(App):
    def build(self):
        layout_principal = BoxLayout(orientation='vertical')
        self.input_nome = TextInput(hint_text='digite seu nome')
        layout_principal.add_widget(self.input_nome)
        botao_enviar = Button(text='enviar', on_press=self.exibir_mensagem)
        layout_principal.add_widget(botao_enviar)
        self.label_mensagem = Label()
        layout_principal.add_widget(self.label_mensagem)

        return layout_principal
    def exibir_mensagem(self, instance):
        nome_usuario = self.input_nome.text
        mensagem = f'Olá {nome_usuario}, você está avançando no kivy! parabéns'
        self.label_mensagem.text = mensagem

if __name__ == '__main__':
    RotuloApp().run()