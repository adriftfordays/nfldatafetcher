import requests

url = "https://www.thesportsdb.com/api/v1/json/123/eventsnextleague.php?id=4391"

try:
    response = requests.get(url)
    data = response.json()

    
    if 'events' not in data:
        print("Error: No events found in API response")
    elif data['events'] is None:
        print("Error: No upcoming games scheduled")
    else:
        with open('nfl_games.txt', 'w') as file:
            for game in data['events'][:5]:
                away = game['strAwayTeam']
                home = game['strHomeTeam']
                line = f"Next Game: {away} @ {home}\n"
                file.write(line)
            
            print("Games saved to nfl_games.txt")
                
except requests.exceptions.RequestException as e:
    print(f"Error connecting to API: {e}")
except KeyError as e:
    print(f"Error: Missing expected data field: {e}")
    


        for game in data ['events'][:5]:
            away = game['strAwayTeam']
            home = game['strHomeTeam']
            print(f"Next Game: {away} @ {home}")
    
except requests.exceptions.RequestException as e:
    print(f"Error connecting to API: {3}")
except KeyError as e:
    print(f"Error: Missing expected data field: {3}")
    
