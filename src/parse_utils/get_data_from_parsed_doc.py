from src.parse_utils.write_data_csv import write_data_to_csv


def get_modified_data(parsed_page):
    # we can also provide an array of classes to class attr in this dictionary inside find_all
    topic_title_tags = parsed_page.find_all('p', {'class': 'f3 lh-condensed mb-0 mt-1 Link--primary'})
    topic_description_tags = parsed_page.find_all('p', {'class': 'f5 color-fg-muted mb-0 mt-1'})

    # we can get the parent tag of these tags by simply writting (topic_title_tags[0].parent)
    # but to extract link of the topic we will directly use the a tag , we can check these by simply inspecting on that particular website
    topic_link_tags = parsed_page.find_all('a', {"class": "no-underline flex-1 d-flex flex-column"})

    # to generate url of any particular topic we will do
    # url = "http://github.com"+ topic_link_tags[0]["href"]
    # print(url)
    base_url = "http://github.com"
    topic_titles = [topic_title_tag.text for topic_title_tag in topic_title_tags]

    topic_descriptions = [topic_description_tag.text.strip() for topic_description_tag in topic_description_tags]

    topic_links = [base_url + topic_link_tag["href"] for topic_link_tag in topic_link_tags]

    write_data_to_csv(topic_titles=topic_titles, topic_desc=topic_descriptions, topic_links=topic_links)
    return [topic_titles, topic_descriptions, topic_links]
