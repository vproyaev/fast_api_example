import asyncio

from api.app import init_routers
from api.module_settings import event_loop
from api.server import server


class WebServer:

    def __init__(self) -> None:
        self._loop = event_loop

    def run(self) -> None:
        init_routers()

        self._loop.create_task(server.serve())

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        return self._loop


web_server = WebServer()
web_server.run()
web_server.loop.run_forever()
