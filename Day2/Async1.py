import asyncio


async def my_co(name, sleep_time):
    print("Starting", name)
    await asyncio.sleep(sleep_time)
    print(name, "is done")


def main():
    # task = asyncio.ensure_future(my_co("A", 2))
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(task)
    # loop.close()

    # 3.7+
    asyncio.run(my_co("A", 2))

if __name__ == '__main__':
    main()
