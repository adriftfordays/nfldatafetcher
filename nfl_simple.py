import requests

url = "https://www.thesportsdb.com/api/v1/json/123/eventsnextleague.php?id=4391"
response = requests.get(url)
data = response.json()

for game in data ['events'][:5]:
    away = game['strAwayTeam']
    home = game['strHomeTeam']
    print(f"Next Game: {away} @ {home}")