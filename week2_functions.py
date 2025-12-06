def add_numbers(num1, num2):
    return num1 + num2
    

result = add_numbers(5, 10)
print(result)  # Output: 15

def greet_user(name):
    return f"Hello, {name}!"

print(greet_user("Matt"))  # Output: "Hello, Matt!"

def format_game(away_team, home_team, away_score, home_score):
    return f"{away_team} @ {home_team}: {away_score}-{home_score}"

game_text = format_game("Giants", "Eagles", 21, 24)
print(game_text)  # Output: "Giants @ Eagles: 21-24"