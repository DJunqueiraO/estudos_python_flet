from flet_core import *

from components.categories_row.categories_row import CategoriesRow
from components.tasks_column.tasks_column import TasksColumn
from utils.colors import *


class WhatsUpRow(Row):
    def __init__(self, page: Page):
        self.page = page
        categories = ['Business', 'Family', 'Friends']
        second_page_contents = Container(
            content=Column(
                controls=[
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Container(
                                on_click=lambda event: self.shrink(event),
                                content=Icon(
                                    icons.MENU
                                )
                            ),
                            Row(
                                controls=[
                                    Icon(icons.SEARCH),
                                    Icon(icons.NOTIFICATIONS_OUTLINED)
                                ]
                            )
                        ]
                    ),
                    Text(
                        value='What\'s up, Josicleison!'
                    ),
                    Text(
                        value='CATEGORIES'
                    ),
                    Container(
                        padding=padding.only(top=10, bottom=20),
                        content=CategoriesRow(categories)
                    ),
                    Container(
                        padding=padding.only(top=20)
                    ),
                    Text(value="TODAY'S TASKS"),
                    Stack(
                        controls=[
                            TasksColumn(['1','2','3','4','5','5','5','5','5','5','5','5','5']),
                            FloatingActionButton(
                                # bottom=2,
                                right=20,
                                icon=icons.ADD,
                                on_click=lambda _: self.page.go('/create_task')
                            )
                        ]
                    )
                ]
            )
        )
        super().__init__(
            alignment=MainAxisAlignment.END,
            controls=[
                Container(
                    animate=Animation(600, AnimationCurve.DECELERATE),
                    animate_scale=Animation(400, curve=AnimationCurve.DECELERATE),
                    width=400,
                    height=850,
                    bgcolor=FOREGROUND,
                    border_radius=35,
                    padding=padding.only(
                        top=50,
                        left=20,
                        right=20,
                        bottom=5
                    ),
                    content=Column(
                        controls=[
                            second_page_contents
                        ]
                    )
                )
            ]
        )

    def shrink(self, event):
        self.controls[0].width = 120
        self.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right
        )
        self.update()

    def restore(self, event):
        self.controls[0].width = 400
        self.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right
        )
        self.update()