import flet as ft

def main(page: ft.Page):
    page.title = "Layouts Básicos"
    page.padding = 20

    titulo = ft.Text(
        "Organizando Elementos na Tela",
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    linha_botoes = ft.Row(
        controls=[
            ft.ElevatedButton("Botão 1", bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
            ft.ElevatedButton("Botão 2", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
            ft.ElevatedButton("Botão 3", bgcolor=ft.Colors.RED, color=ft.Colors.WHITE)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    caixa1 = ft.Container(
        content=ft.Text("Caixa 1", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.PURPLE,
        width=200,
        height=50,
        alignment=ft.alignment.center,
        border_radius=5
    )

    caixa2 = ft.Container(
        content=ft.Text("Caixa 2", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.ORANGE,
        width=200,
        height=50,
        alignment=ft.alignment.center,
        border_radius=5
    )

    coluna_caixas = ft.Column(
        controls=[caixa1, caixa2],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    layout_principal = ft.Column(
        controls=[
            titulo,
            ft.Text("Linha horizontal de botôes:", size=16),
            coluna_caixas,
            ft.Text("Layout organizado!", size=14, color=ft.Colors.GREEN)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=25
    )

    page.add(layout_principal)

ft.app(target=main)