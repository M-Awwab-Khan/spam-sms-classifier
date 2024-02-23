import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Container(
            content=ft.Row([
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
                                    max_lines=15,
                                ),
                                ft.FloatingActionButton(
                                    icon=ft.icons.SETTINGS, text='Classify'
                                )
                            ],
                            width=1100, spacing=25
                        )
                    ]),
                    padding=50
        
        )
        
    )

ft.app(target=main)