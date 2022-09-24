import aiohttp
from .write_data import write


async def scrap(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            html = await response.text()
    # write(html)
    return html
