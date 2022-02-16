import requests

# may seem inefficient probably is but who cares

url = "https://random-word-api.herokuapp.com/all"
r = requests.get(url)
data = r.json()


