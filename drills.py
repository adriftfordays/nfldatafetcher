teams = ['Lions', 'Packers', 'Cowboys', 'Bears', 'Vikings']
print(teams[0])
print(teams[4])
    
for i in reversed(teams):
    print(i)
    
teams.append("Panthers")
print(teams)

teams.remove("Cowboys")
print(teams)

game = {
    "away_team": "Lions",
    "home_team":"Panthers",
    "away_score" : 24,
    "home_score": 30,
}

print(game["away_team"])
    
if game['away_score'] > game['home_score']:
    print(f"{game['away_team']} wins!")
elif game['away_score'] < game['home_score']:
    print(f"{game['home_team']} wins!")
else:
    print("It's a tie!")
        
game["location"] = "Charlotte"
print(game)

game['home_score'] = 27
print(game)

print(game)

game_two = {
    "away_team": "Packers",
    "home_team":"Bears",
    "away_score" : 14,
    "home_score": 21,
}

game_three = {
    "away_team": "Vikings",
    "home_team": "Lions",
    "away_score": 17,
    "home_score": 20,
}

games = [game, game_two, game_three]
print(games)

for g in games:
    print(f"{g['away_team']} @ {g['home_team']}: {g['away_score']}-{g['home_score']}")
    
total = 0
for g in games:
    total += g['home_score']
    total += g['away_score']
print(f"Total points scored: {total}")

highest_scoring_game = 0
winning_team = ""

for g in games:
    if g["away_score"] > highest_scoring_game:
        highest_scoring_game = g['away_score']
        winning_team = g['away_team']
        
    if g["home_score"] > highest_scoring_game:
        highest_scoring_game = g['home_score']
        winning_team = g['home_team']
        
print(f"Highest scoring team: {winning_team} with {highest_scoring_game} points")

