import requests

# requests is useful when you want to browse an api

api_key = '11ec0676293443bbabc7c85e6eb6471c'
url = 'https://newsapi.org/v2/everything?q=tesla&' \
      'from=2023-06-02&sortBy=publishedAt&apiKey=' \
      '11ec0676293443bbabc7c85e6eb6471c'

request = requests.get(url)

# get a dictionary with data
content = request.json()

# access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
