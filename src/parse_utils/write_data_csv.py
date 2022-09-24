import pandas as pd


def write_data_to_csv(topic_titles,topic_desc,topic_links):
    data_to_be_written_in_csv = pd.DataFrame({'topic': topic_titles, "description": topic_desc, "link": topic_links})
    # print(data_to_be_written_in_csv)
    data_to_be_written_in_csv.to_csv('topics_data.csv', index=True)
