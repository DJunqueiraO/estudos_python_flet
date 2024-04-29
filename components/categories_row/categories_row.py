from flet_core import *

from utils.colors import *


class CategoriesRow(Row):
    def __init__(self, categories: list[str]):
        super().__init__(
            scroll=ScrollMode.AUTO,
            controls=list(map(
                lambda enumerated_category: Container(
                    bgcolor=BACKGROUND,
                    height=110,
                    width=170,
                    padding=15,
                    border_radius=20,
                    content=Column(
                        controls=[
                            Text('40 Tasks'),
                            Text(enumerated_category[1]),
                            Container(
                                width=160,
                                height=5,
                                bgcolor='white12',
                                border_radius=20,
                                padding=padding.only(right=enumerated_category[0]*30),
                                content=Container(
                                    bgcolor=EMPHASIS
                                )
                            )
                        ]
                    )
                ),
                enumerate(categories)
            ))
        )