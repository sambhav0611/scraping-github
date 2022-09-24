import csv

import aiohttp

from src.parse_utils.beautiful_soup import parse_page
from src.parse_utils.get_topic_data_from_parsed_page import get_topic_wise_data


async def scrap_topics(topic_links, topic_titles):
    with open('final.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["topic_name", "repo_name", "author", "stars", "link"])
        for i, topic_link in enumerate(topic_links):
            async with aiohttp.ClientSession() as session:
                async with session.get(topic_link) as response:
                    parsed_page = await parse_page(await response.text())
            [repo_user_names, repo_links, stars_counts] = get_topic_wise_data(parsed_page)
            for j, repo_user_name in enumerate(repo_user_names):
                writer.writerow(
                    [topic_titles[i], repo_user_names[j][1], repo_user_names[j][0], stars_counts[j], repo_links[j]])
