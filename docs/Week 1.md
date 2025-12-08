# Week 1: Python Fundamentals - Comprehensive Review

**Duration:** December 2025 (5 days + drills)  
**Project:** NFL Data Fetcher  
**Status:** ✅ Complete

---

## Overview

Week 1 focused on Python fundamentals through hands-on project work. Rather than watching tutorials, you built three working programs from scratch, debugged real errors, and learned by doing.

**Projects Built:**
- `nfl_simple.py` - API integration with error handling and file output
- `drills.py` - Six progressive challenges covering core concepts
- `standings.py` - Complete data processing pipeline

---

## Core Concepts

### 1. Variables and Data Types

**What they are:**
- Variables store data
- Python has dynamic typing (type determined at runtime)

**Key types learned:**
```python
# Strings
team = "Lions"
message = 'Hello'

# Integers
score = 24
count = 0

# Lists (ordered, mutable)
teams = ['Lions', 'Packers', 'Bears']

# Dictionaries (key-value pairs, mutable)
game = {'away': 'Lions', 'home': 'Packers', 'score': 24}

# Sets (unique values, unordered)
unique_teams = {'Lions', 'Packers'}  # Duplicates automatically removed
```

**Type checking:**
```python
print(type(teams))  # <class 'list'>
print(type(game))   # <class 'dict'>
```

**Mutable vs Immutable:**
- **Mutable:** Can change after creation (lists, dicts)
- **Immutable:** Cannot change (strings, numbers, tuples)

---

### 2. Lists

**What they are:**
Ordered collections that can hold multiple items.

**Key operations:**
```python
# Creating
teams = ['Lions', 'Packers', 'Cowboys']

# Accessing (zero-indexed)
first = teams[0]      # 'Lions'
last = teams[-1]      # 'Cowboys'
slice = teams[:2]     # ['Lions', 'Packers']

# Modifying
teams.append('Bears')      # Add to end
teams.remove('Cowboys')    # Remove by value
teams[0] = 'Vikings'       # Change by index

# Length
count = len(teams)    # 3

# Looping
for team in teams:
    print(team)
```

**Common patterns:**
```python
# Reverse iteration
for team in reversed(teams):
    print(team)

# Enumerate (get index + value)
for i, team in enumerate(teams):
    print(f"{i}: {team}")
```

---

### 3. Dictionaries

**What they are:**
Key-value pairs for structured data storage.

**Syntax:**
```python
# Creating
game = {
    'away_team': 'Lions',
    'home_team': 'Packers',
    'away_score': 24,
    'home_score': 27
}

# Accessing
away = game['away_team']           # 'Lions'
score = game.get('away_score', 0)  # 24 (with default)

# Adding/modifying
game['location'] = 'Detroit'    # Add new key
game['away_score'] = 28         # Change value

# Checking existence
if 'away_team' in game:
    print("Key exists")

# Looping
for key, value in game.items():
    print(f"{key}: {value}")
```

**Nested dictionaries:**
```python
records = {
    'Lions': {'wins': 3, 'losses': 1},
    'Packers': {'wins': 2, 'losses': 2}
}

lions_wins = records['Lions']['wins']  # 3
```

---

### 4. Loops

**For loops:**
Iterate through sequences (lists, strings, ranges).
```python
# Loop through list
for team in teams:
    print(team)

# Loop through range
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step by 2)
    print(i)

# Loop through dictionary
for key, value in game.items():
    print(f"{key}: {value}")
```

**While loops:**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Critical concept: Indentation**
```python
# ❌ Wrong - print is outside loop
for team in teams:
print(team)

# ✅ Correct - print is inside loop
for team in teams:
    print(team)
```

---

### 5. Conditionals (if/elif/else)

**Basic syntax:**
```python
if away_score > home_score:
    print("Away team wins")
elif away_score < home_score:
    print("Home team wins")
else:
    print("It's a tie")
```

**Comparison operators:**
```python
==  # Equal
!=  # Not equal
>   # Greater than
<   # Less than
>=  # Greater than or equal
<=  # Less than or equal

in  # Check membership
not in  # Check non-membership
```

**Logical operators:**
```python
and  # Both must be true
or   # At least one must be true
not  # Negation

if score > 20 and score < 30:
    print("Score in range")
```

---

### 6. String Operations

**F-strings (formatted string literals):**
```python
team = "Lions"
score = 24

# F-string (preferred)
message = f"Next Game: {team} scored {score} points"

# Old style (avoid)
message = "Next Game: " + team + " scored " + str(score) + " points"
```

**String methods:**
```python
text = "  Hello World  "

text.strip()           # "Hello World" (remove whitespace)
text.split()           # ['Hello', 'World']
text.replace('o', 'x') # "Hellx Wxrld"
text.upper()           # "  HELLO WORLD  "
text.lower()           # "  hello world  "

# Joining
words = ['Hello', 'World']
sentence = ' '.join(words)  # "Hello World"
```

**Slicing:**
```python
text = "Hello World"
text[0]      # 'H'
text[-1]     # 'd'
text[0:5]    # 'Hello'
text[6:]     # 'World'
```

---

### 7. File Operations

**Reading files:**
```python
# Read entire file
with open('data.txt', 'r') as file:
    content = file.read()

# Read line by line
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Read all lines into list
with open('data.txt', 'r') as file:
    lines = file.readlines()
```

**Writing files:**
```python
# Write (overwrites existing)
with open('output.txt', 'w') as file:
    file.write("Hello World\n")
    file.write("Second line\n")

# Append (adds to end)
with open('output.txt', 'a') as file:
    file.write("Additional line\n")
```

**File modes:**
- `'r'` - Read (default)
- `'w'` - Write (overwrites)
- `'a'` - Append
- `'r+'` - Read and write

**Why use `with`:**
- Automatically closes file (even if error occurs)
- Prevents file corruption
- Professional best practice

---

### 8. Error Handling

**try/except blocks:**
```python
try:
    response = requests.get(url)
    data = response.json()
    print(data['key'])
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
except KeyError as e:
    print(f"Missing key: {e}")
```

**When to use try/except vs if:**

**Use try/except for unpredictable failures:**
```python
# ✅ Can't predict network failures
try:
    response = requests.get(url)
except requests.exceptions.RequestException:
    print("Connection failed")
```

**Use if statements for predictable checks:**
```python
# ✅ Can check before accessing
if 'events' in data:
    games = data['events']
```

**Common exception types:**
- `KeyError` - Dictionary key doesn't exist
- `IndexError` - List index out of range
- `ValueError` - Invalid value conversion
- `FileNotFoundError` - File doesn't exist
- `TypeError` - Wrong type used

---

### 9. API Integration

**Making HTTP requests:**
```python
import requests

url = "https://api.example.com/data"

# GET request
response = requests.get(url)

# Check if successful
if response.ok:
    data = response.json()  # Parse JSON to Python dict/list
else:
    print(f"Error: {response.status_code}")
```

**Working with JSON:**
```python
# JSON structure maps to Python types:
# {} -> dict
# [] -> list
# "text" -> str
# 123 -> int
# true/false -> True/False

data = {
    "events": [
        {"team": "Lions", "score": 24},
        {"team": "Packers", "score": 27}
    ]
}

first_game = data['events'][0]
team_name = first_game['team']
```

---

### 10. Data Transformation

**Removing duplicates:**
```python
teams = ['Lions', 'Packers', 'Lions', 'Bears']

# Method 1: Convert to set then back to list
unique_teams = list(set(teams))

# Method 2: Manual loop
unique = []
for team in teams:
    if team not in unique:
        unique.append(team)
```

**Sorting:**
```python
# Sort list in place
teams.sort()

# Sort and return new list
sorted_teams = sorted(teams)

# Sort in reverse
teams.sort(reverse=True)

# Sort by custom key (e.g., by wins)
sorted_records = sorted(records.items(), key=lambda x: x[1]['wins'], reverse=True)
```

**String parsing:**
```python
line = "Next Game: Green Bay Packers 24 @ Detroit Lions 27"

# Split by delimiter
parts = line.split("@")
# ['Next Game: Green Bay Packers 24 ', ' Detroit Lions 27']

# Extract components
left_parts = parts[0].split()
away_score = int(left_parts[-1])  # Last element
away_team = ' '.join(left_parts[2:-1])  # Middle elements
```

---

## Common Mistakes & Solutions

### 1. Indentation Errors
```python
# ❌ Wrong
for item in list:
print(item)

# ✅ Correct
for item in list:
    print(item)
```

### 2. Using Wrong File Mode
```python
# ❌ Wrong - overwrites file when you want to read
with open("data.txt", "w") as file:
    content = file.read()

# ✅ Correct
with open("data.txt", "r") as file:
    content = file.read()
```

### 3. Forgetting to Convert Types
```python
# ❌ Wrong - can't do math on strings
score = "24"
total = score + 10  # TypeError

# ✅ Correct
score = int("24")
total = score + 10  # 34
```

### 4. Index Out of Range
```python
teams = ['Lions', 'Packers']

# ❌ Wrong
for i in range(len(teams)):
    print(teams[i + 1])  # Error when i=1

# ✅ Correct - step by 2 for pairs
for i in range(0, len(teams), 2):
    print(teams[i], teams[i + 1])
```

### 5. Forgetting Newlines in File Writing
```python
# ❌ Wrong - all on one line
file.write("Line 1")
file.write("Line 2")

# ✅ Correct
file.write("Line 1\n")
file.write("Line 2\n")
```

---

## Key Takeaways

### Programming Principles

**1. Start simple, build complexity**
- Don't try to write the perfect solution first
- Get something working, then improve it

**2. Debug systematically**
- Read error messages carefully
- Add print statements to inspect data
- Change one thing at a time

**3. Type matters**
- Use `type()` to check what you're working with
- Convert types explicitly when needed

**4. Indentation is syntax**
- Python uses whitespace to define code blocks
- Be consistent (4 spaces is standard)

### Best Practices

**1. Use meaningful variable names**
```python
# ❌ Bad
x = 24
y = 'Lions'

# ✅ Good
score = 24
team_name = 'Lions'
```

**2. Comment complex logic**
```python
# Extract score (last element after splitting)
score = parts[0].split()[-1]
```

**3. Use context managers for files**
```python
# ✅ Always use with
with open('file.txt', 'r') as file:
    content = file.read()
```

**4. Handle errors gracefully**
```python
try:
    # risky operation
except SpecificError:
    # handle it
```

---

## Git Commands Used
```bash
# Initialize repository
git init

# Check status
git status

# Stage files
git add filename.py
git add .  # Stage all files

# Commit with message
git commit -m "Descriptive message"

# Push to remote
git push

# Pull latest changes
git pull

# View commit history
git log
```

---

## Week 1 Project Statistics

**Code written:** ~200+ lines (typed manually, not copy/pasted)
**Programs created:** 3 (nfl_simple.py, drills.py, standings.py)
**Errors debugged:** 15+
**Concepts mastered:** 10+
**GitHub commits:** 8+
**Perfect knowledge check:** 5/5 ✅

---

## Skills Acquired

By the end of Week 1, you can:

- [x] ✅ Read and write files
- [x] ✅ Make API requests and parse JSON
- [x] ✅ Use loops to process data
- [x] ✅ Store data in lists and dictionaries
- [x] ✅ Handle errors gracefully
- [x] ✅ Parse and transform strings
- [x] ✅ Write clean, working Python code
- [x] ✅ Debug systematically
- [x] ✅ Use Git for version control
- [x] ✅ Document code professionally

---

## What's Next: Week 2

**Topic:** Python Functions & Modules

**Why it matters:**
Functions let you write reusable, organized code. Every professional program uses them.

**What you'll learn:**
- Writing functions with parameters
- Return values
- Function scope
- Organizing code into modules
- Refactoring existing code

**Project:**
Refactor Week 1 code to use clean, reusable functions.

---

## Quick Reference

### Most Used Patterns

**Loop through list:**
```python
for item in my_list:
    print(item)
```

**Loop through dictionary:**
```python
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

**Read file:**
```python
with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

**Write file:**
```python
with open('file.txt', 'w') as file:
    file.write("content\n")
```

**Error handling:**
```python
try:
    # risky code
except SpecificError as e:
    print(f"Error: {e}")
```

**API call:**
```python
import requests
response = requests.get(url)
data = response.json()
```

---

## Resources

**Official Documentation:**
- [Python Docs](https://docs.python.org/3/)
- [Requests Library](https://requests.readthedocs.io/)

**Your Projects:**
- [GitHub Repository](https://github.com/adriftfordays/nfl-data-fetcher)

**Next Steps:**
- Week 2: Functions & Modules
- Week 3-4: Classes & OOP
- Week 5-8: Linux Fundamentals

---

*Week 1 completed: December 2025*  
*Next review: After Week 2*