import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"


    page.add(
        ft.Column(
            [
                ft.Text(
                    "SMS/Email Spam Classifier",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.TextField(
                    label="Enter message body",
                    multiline=True,
                    min_lines=1,
                    max_lines=8,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)