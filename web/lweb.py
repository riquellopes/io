import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
from aiohttp import web

async def home(request):
    return web.Response(text="Home")

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
app.router.add_get("/", home)

handler = app.make_handler()
server = loop.create_server(handler, "0.0.0.0", "8080")


server = loop.run_until_complete(server)
try:
    loop.run_forever()
finally:
    server.close()
    loop.close()
