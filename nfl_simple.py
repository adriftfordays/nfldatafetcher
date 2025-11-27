import requests

url = "https://www.thesportsdb.com/api/v1/json/3/eventsnextleague.php?id=4291"
response = requests.get(url)
data = response.json()

first_game= data['events'][0]
away = first_game['strAwayTeam']
home = first_game['strHomeTeam']

'print(f"Next Game: {away} @ {home}")'