from flet_core import *

from utils.colors import *


class TasksColumn(Column):
    def __init__(self, tasks: list[str]):
        super().__init__(
            height=400,
            scroll=ScrollMode.AUTO,
            controls=list(map(
                lambda task: Container(
                    padding=padding.only(left=45),
                    height=70,
                    width=400,
                    bgcolor=BACKGROUND,
                    border_radius=25,
                    animate=Animation(600, AnimationCurve.DECELERATE),
                    animate_scale=Animation(400, AnimationCurve.DECELERATE),
                    content=Checkbox(
                        active_color=EMPHASIS,
                        width=40,
                        scale=1.2,
                        shape=CircleBorder(),
                        label=task
                    )
                ),
                tasks
            ))
        )