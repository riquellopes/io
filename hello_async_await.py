import asyncio


async def greet_every_two_seconds():
    while True:
        print("Hello World")
        await asyncio.sleep(2)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(greet_every_two_seconds())
    except:
        loop.close()
