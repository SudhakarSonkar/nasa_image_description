import requests
from send_email import send_email

api_key = "c918085c843043fb9e0cfbf7b7a606a9"
topic = "tesla"
url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=popularity&apiKey=c918085c843043fb9e0cfbf7b7a606a9&language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"]+ 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
