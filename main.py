import asyncio

from src.parse_utils.beautiful_soup import parse_page_with_file, parse_page
from src.parse_utils.get_data_from_parsed_doc import get_modified_data
from src.scrap_utils.scrap import scrap
from src.scrap_utils.scrap_topic_utils import scrap_topics


async def web_scrapping():
    url = "https://github.com/topics"
    page = await scrap(url)
    parsed_page = await parse_page(page)
    [topic_titles, topic_descriptions, topic_links] = get_modified_data(parsed_page)
    await scrap_topics(topic_links=topic_links, topic_titles=topic_titles)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(web_scrapping())
