from flet_core import *


class CreateTaskContainer(Container):
    def __init__(self, page: Page):
        super().__init__(
            height=40,
            width=40,
            content=Text('x'),
            on_click=lambda _: page.go('/')
        )
