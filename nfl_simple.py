import requests

url = "https://www.thesportsdb.com/api/v1/json/123/eventsnextleague.php?id=4391"
response = requests.get(url)
data = response.json()

first_game = data['events'][0]
away = first_game['strAwayTeam']
home = first_game['strHomeTeam']

print(f"Next Game: {away} @ {home}")