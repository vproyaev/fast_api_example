from starlette.middleware.sessions import SessionMiddleware
from uvicorn import Config, Server

from api.app import app
from api.base_settings import base_settings
from api.module_settings import event_loop

app.add_middleware(SessionMiddleware, secret_key=base_settings.jwt_secret)


@app.on_event('shutdown')
async def shutdown_event():
    pass


@app.on_event('startup')
async def startup_event():
    pass


config = Config(
    app=app,
    loop=event_loop,
    reload=True,
    host=base_settings.server_address,
    port=base_settings.server_port
)

server = Server(config)
