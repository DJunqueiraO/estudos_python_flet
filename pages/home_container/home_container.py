from flet_core import *

from pages.whats_up_row.whats_up_row import WhatsUpRow
from utils.colors import *


class HomeContainer(Container):
    def __init__(self, page: Page):
        super().__init__(
            width=400,
            height=850,
            bgcolor=BACKGROUND,
            border_radius=35,
            content=Stack(
                controls=[
                    WhatsUpRow(page)
                ]
            )
        )