import flet as ft

class ClassifyPage(ft.UserControl):
    def build(self):
        return ft.Container(
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
                            expand=True, spacing=25
                        )
                    ]),
                    padding=70
        
        )