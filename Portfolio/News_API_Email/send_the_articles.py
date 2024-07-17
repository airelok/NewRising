import requests

api_key = "63b79d35895e465b83739d1dc74dbff7"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=63b79d35895e465b83739d1dc74dbff7"

#   Creates a request object type
request = requests.get(url)

#   Get a dictionary with data
content = request.json()

#   Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])