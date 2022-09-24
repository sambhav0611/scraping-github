def get_topic_wise_data(parsed_page):
    repo_user_names = []
    repo_links = []
    repo_user_names_tags = parsed_page.find_all('h3', {'class': 'f3 color-fg-muted text-normal lh-condensed'})
    for repo_user_names_tag in repo_user_names_tags:
        repo_user_names.append([repo_user_name.text.strip() for repo_user_name in repo_user_names_tag.findChildren()])
        repo_links.append(repo_user_names_tag.findChildren()[1]['href'])
    stars_counts = parsed_page.find_all('span', {'id': 'repo-stars-counter-star'})
    stars_counts = [star_count.text for star_count in stars_counts]
    base_url = "http://github.com"
    repo_links = [base_url+repo_link for repo_link in repo_links]
    return [repo_user_names,repo_links,stars_counts]
