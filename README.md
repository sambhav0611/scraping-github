# **Agenda : We're going to scrape https://github.com/topics**

1. ## **We'll get a list of topics.** 

### For each topic:

1. we'll get topic title,
2. topic page URL,
3. topic description
4. we'll get the top 25 repositories in the topic from the topic page

### For each repository we'll grab:

1. The repo name
2. username
3. stars 
4. repo URL

### For each topic we'll create a CSV file in the following format:

`Repo Name,Username,Stars,Repo URL`