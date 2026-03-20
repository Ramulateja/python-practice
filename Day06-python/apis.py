import requests
res = requests.get("https://official-joke-api.appspot.com/random_joke")
data = res.json()
print(data["setup"])
print(data["punchline"])