def parse_game_line(line):
        parts = line.strip().split("@")
        # Split first part to get team and score
        left_parts = parts[0].strip().split()
        away_score = int(left_parts[-1])  # Last element = score
        away_team = ' '.join(left_parts[2:-1])  # Skip "Next Game:" and score

        # Split second part
        right_parts = parts[1].strip().split()
        home_score = int(right_parts[-1])  # Last element = score
        home_team = ' '.join(right_parts[:-1])  # Everything except score

        return away_team, away_score, home_team, home_score
    
def calculate_records(teams, scores):
    
    records = {}
    
    for i in range(0, len(teams), 2):
        away = teams[i]
        home = teams[i + 1]
        away_sc = int(scores[i])
        home_sc = int(scores[i + 1])
    
    # Initialize records if team not present
        if away not in records:
            records[away] = {"wins": 0, "losses": 0}
        if home not in records:
            records[home] = {"wins": 0, "losses": 0}
        
    # Update records based on scores
        if away_sc > home_sc:
            records[away]["wins"] += 1
            records[home]["losses"] += 1
        else:
            records[home]["wins"] += 1  
            records[away]["losses"] += 1
        
    return records

def winning_teams(records):
    standings = []
    for team, record in records.items():
        standings.append((team, record["wins"], record["losses"]))
    standings.sort(key=lambda x: x[1], reverse=True)
    return standings

teams = [] #Start with an empty list
score = [] #Start with an empty list


with open ("nfl_games.txt", "r") as file:
    for line in file:
        away_team, away_score, home_team, home_score = parse_game_line(line)
        teams.append(away_team)
        teams.append(home_team)
        score.append(away_score)
        score.append(home_score)
       
       
records = calculate_records(teams, score)
     
with open('standings.txt', 'w') as f:
    for team, wins, losses in winning_teams(records):
        f.write(f"{team}: {wins} wins, {losses} losses\n")