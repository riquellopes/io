import asyncio
from aiohttp import web


async def home(request):
    return web.Response(text="Home")

app = web.Application()
app.router.add_get("/", home)

web.run_app(app)
