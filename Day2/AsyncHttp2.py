from aiohttp import ClientSession
import asyncio


async def get(session, url):
    async with session.get(url) as response:
        return await response.text()


async def fetch(url):
    async with ClientSession() as session:
        print("Fetching", url)
        html = await get(session, url)
        print(url, "is done")
        return html


async def print_when_done(tasks):
    result = [await res for res in asyncio.as_completed(tasks)]

    print("Got", len(result), "pages")
    print("They got the titles")
    for page in result:
        title_index = page.index("<title>")
        title_end_index = page.index("</title>")
        title = page[title_index+7: title_end_index]
        print(title.strip())


async def get_urls():
    urls = ["http://cnn.com", "http://bbc.com", "http://aljazeera.com"]
    tasks = [fetch(url) for url in urls]
    await print_when_done(tasks)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_urls())


if __name__ == '__main__':
    main()
