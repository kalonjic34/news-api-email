import requests 

api_key = "95c2ea503e8d4c5a80fb9036d9c0c4ea"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-06-08&sortBy=publishedAt&apiKey=95c2ea503e8d4c5a80fb9036d9c0c4ea"


# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

# access article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])