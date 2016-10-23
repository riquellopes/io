import asyncio


def print_hand_repeat(loop):
    print("Hello World")
    loop.call_later(2, print_hand_repeat, loop)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    print_hand_repeat(loop)

    try:
        loop.run_forever()
    except:
        loop.close()
