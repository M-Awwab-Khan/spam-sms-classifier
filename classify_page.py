import flet as ft
from classify import classify_msg

class ClassifyPage(ft.UserControl):
    def build(self):
        self.msg_box = ft.TextField(
                    label="Enter message body",
                    multiline=True,
                    min_lines=1,
                    max_lines=15,
                )
        self.prediction = ft.Text(
                            size=30,
                            weight=ft.FontWeight.BOLD,
                        )
        return ft.Container(
            content=ft.Row([
                        ft.Column(
                            [
                                ft.Text(
                                    "SMS/Email Spam Classifier",
                                    size=40,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                self.msg_box,
                                ft.FloatingActionButton(
                                    icon=ft.icons.SETTINGS, 
                                    text='Classify',
                                    on_click=self.show_classification
                                ),
                                self.prediction
                            ],
                            expand=True, spacing=25
                        )
                    ]),
                    padding=70
        
        )
    
    def show_classification(self, e):
        msg = self.msg_box.value
        prediction = classify_msg(msg)
        self.prediction.value = prediction
        self.update()
