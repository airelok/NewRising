import requests
from news_to_email import send_an_email


api_key = "63b79d35895e465b83739d1dc74dbff7"

topic = "startup"

#   Added a parameter to the url
url = "https://newsapi.org/v2/top-headlines?" \
      f"q={topic}&" \
      "sources=techcrunch&" \
      "apiKey=63b79d35895e465b83739d1dc74dbff7&" \
      "language=en"

#   Creates a request object type
request = requests.get(url)

#   Get a dictionary with data
content = request.json()

#   Access the article titles and descriptions
body = ""
for article in content["articles"][:3]:
    #   Check for articles that have a None Type for article["title"]
    if article["title"] is not None:
        body = "Subject: Today's News" + "\n" \
               + body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2 * "\n"
    print(body)

body = body.encode("utf-8")
send_an_email(message = body)