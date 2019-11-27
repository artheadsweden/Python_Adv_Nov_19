import asyncio
import time


async def my_co(name, sleep_time):
    print("Starting", name)
    await asyncio.sleep(sleep_time)
    print(name, "is done")


async def many():
    await asyncio.gather(
        my_co("A", 1),
        my_co("B", 5),
        my_co("C", 3)
    )


def main():
    start = time.time()
    asyncio.run(many())
    print("It took", time.time()-start, "seconds")

if __name__ == '__main__':
    main()
