import asyncio
import aiohttp
from aiohttp import web
import json

URLS = ['http://example.com/', 'http://dummy-a98x3.org', 'http://example.net/', ]

async def handler(request):
    coroutines = [aiohttp.request("get", url) for url in URLS]

    results = await asyncio.gather(*coroutines, return_exceptions=True)

    respose_data = {
        website: not isinstance(result, Exception) and result.status == 200
        for website, result in zip(URLS, results)
    }

    body = json.dumps(respose_data).encode("utf-8")
    return web.Response(body=body, content_type="application/json")


loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
app.router.add_route("GET", "/", handler)

server = loop.create_server(app.make_handler(), "0.0.0.0", 5000)
print("Server started at http://0.0.0.0:5000")

loop.run_until_complete(server)

try:
    loop.run_forever()
except:
    loop.stop()
