import flet as ft
from classify_page import ClassifyPage

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ClassifyPage()
    )

ft.app(target=main)