import requests 
from send_email import send_email

api_key = "95c2ea503e8d4c5a80fb9036d9c0c4ea"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-06-08&sortBy=publishedAt&apiKey=95c2ea503e8d4c5a80fb9036d9c0c4ea"


# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# access article title and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:  
        body = body + article["title"] +"\n"+ article["description"] + 2*"\n"
        
body = body.encode("utf-8")   
send_email(message=body)