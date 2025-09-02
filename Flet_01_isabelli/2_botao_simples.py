import flet as ft

def main(page: ft.Page):
    page.title = "Meu primeiro Botão"
    page.padding = 20

    # Criando um texto que será modificado pelo botão
    mensagem = ft.Text(
        value="Clique no botão abaixo",
        size=20,
        text_align=ft.TextAlign.CENTER
    )

    def botao_clicado(evento):

        # Mudando o texto da mensagem
        mensagem.value = "Parabéns, você clicou no botão!"
        mensagem.color = ft.Colors.GREEN

        # IMPORTANTE: Sempre que modificamos elementos da interface, precisamos chamar page.update() para que as mudanças apareçam na tela
        page.update()

    # Criando nosso botão
    meu_botao = ft.ElevatedButton(
        text="Clique em mim",
        on_click=botao_clicado,
        width=200,
        height=50,
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
    )

    # Adicionando os elementos
    page.add(mensagem)
    page.add(meu_botao)

ft.app(target=main)