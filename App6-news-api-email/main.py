import requests
from news_mail import send_email

# requests is useful when you want to browse an api

topic = 'tesla'
api_key = '11ec0676293443bbabc7c85e6eb6471c'
url = 'https://newsapi.org/v2/everything?' \
      f'q={topic}&' \
      'sortBy=publishedAt&' \
      'apiKey=11ec0676293443bbabc7c85e6eb6471c&' \
      'language=en'

request = requests.get(url)

# get a dictionary with data
content = request.json()

# access the article titles and description
body = ''
for article in content["articles"][:20]:
    if article['title'] is not None:
        body = "Subject: Today's news" \
               + body + article['title'] \
               + '\n' + article['description'] \
               + '\n' + article['url'] + 2*'\n'

body = body.encode('utf-8')
send_email(message=body, receiver='sparkles.player@gmail.com')
