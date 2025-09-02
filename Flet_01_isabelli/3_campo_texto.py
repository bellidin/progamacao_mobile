import flet as ft

def main(page: ft.Page):
    page.title = "Campo de Texto"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

    campo_nome = ft.TextField(
        label="Digite seu nome aqui",
        width=300,
        border_color=ft.Colors.BLUE
    )

    resposta = ft.Text(
        value="",
        size=18,
        text_align=ft.TextAlign.CENTER
    )

    def processar_nome(evento):
        nome_digitado = campo_nome.value

        if nome_digitado == "" or nome_digitado is None:
            resposta.value = "Por favor, digite seu nome"
            resposta.color = ft.Colors.RED
        elif len(nome_digitado) < 2:
            resposta.value = "Nome muito curto"
            resposta.color = ft.Colors.ORANGE
        else:
            resposta.value = f"Olá, {nome_digitado}. Prazer em conhecê-lo(a)!"
            resposta.color = ft.Colors.GREEN

        page.update()
    botao_ok = ft.ElevatedButton(
        text="Confirmar",
        on_click=processar_nome,
        width=150
    )

    page.add(
        ft.Text("Vamos nos conhecer!", size=22, weight=ft.FontWeight.BOLD),
        campo_nome,
        botao_ok,
        resposta
    )

ft.app(target=main)