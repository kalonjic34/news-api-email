import requests 

api_key = "95c2ea503e8d4c5a80fb9036d9c0c4ea"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-06-08&sortBy=publishedAt&apiKey=95c2ea503e8d4c5a80fb9036d9c0c4ea"


request = requests.get(url)
content = request.text
print(content)