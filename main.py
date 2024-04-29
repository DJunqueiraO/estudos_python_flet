from flet_core import *
from flet_runtime import app

from pages.create_task_container.create_task_container import CreateTaskContainer
from pages.home_container.home_container import HomeContainer


def main(page: Page):

    pages = {
        '/': HomeContainer(page),
        '/create_task': CreateTaskContainer(page)
    }

    def on_route_change(event: RouteChangeEvent):
        page.views.clear()
        page.views.append(
            View(
                event.route,
                controls=[pages[event.route]]
            )
        )
        page.add(pages[event.route])

    page.on_route_change = on_route_change
    page.go('/')


if __name__ == '__main__':
    app(target=main)