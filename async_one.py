import asyncio


@asyncio.coroutine
def fac(name, number):
    f = 1
    for i in range(2, number + 1):
        print("Task %s: Compute fac(%s)..." % (name, i))
        yield from asyncio.sleep(1)
        f += i
    print("Task %s: Compute fac(%s) = %s " % (name, number, i))

loop = asyncio.get_event_loop()
tasks = [
    asyncio.async(fac("A", 2)),
    asyncio.async(fac("B", 3)),
    asyncio.async(fac("C", 4))
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()
