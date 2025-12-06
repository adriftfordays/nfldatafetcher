count = 0
with open('games.txt', 'r') as file:
    for line in file:
        count += 1
print(count)