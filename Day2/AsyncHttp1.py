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

async def get_urls():
    result = await asyncio.gather(
        fetch("http://cnn.com"),
        fetch("http://bbc.com"),
        fetch("http://aljazeera.com")
    )

    print("Got", len(result), "pages")
    print("They got the titles")
    for page in result:
        title_index = page.index("<title>")
        title_end_index = page.index("</title>")
        title = page[title_index+7: title_end_index]
        print(title.strip())


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_urls())


if __name__ == '__main__':
    main()
