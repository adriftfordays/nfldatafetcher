# Week 2 - Day 5: Watchlist Tracker Foundation
# Session Date: December 7, 2025
# Goal: Build practical multi-session project while reinforcing core Python fundamentals

---

## Session Overview

**Project:** Movie/TV Show Watchlist Tracker (Session 1 of 3)  
**Focus:** Data structure design, basic CRUD operations, input validation  
**Time Invested:** TBD  
**Confidence Level:** TBD

---

## What I Built

### Core Functionality (Session 1)
- Data structure for tracking movies/TV shows with 9 fields
- `create_item()` - Add new items with validated priority input
- `display_all()` - Formatted display of entire watchlist
- Menu-driven interface with 3 options (add/display/exit)

### Data Fields Tracked
```python
item = {
    'title': str,           # Movie/show name
    'type': str,            # "movie" or "show"
    'recommended_by': str,  # Who suggested it
    'priority': int,        # 1-5 scale (1=highest)
    'date_added': str,      # YYYY-MM-DD format
    'date_watched': None,   # Null until marked watched
    'rating': None,         # 1-5 scale after watching
    'notes': None,          # Thoughts after watching
    'imdb_link': str        # Reference URL
}
```

---

## New Concepts Introduced

### 1. The `datetime` Module
**Purpose:** Handle date/time operations professionally

```python
from datetime import datetime

# Get current date in consistent format
current_date = datetime.now().strftime('%Y-%m-%d')
# Returns: '2025-12-07'
```

**Key insight:** This gives us consistent, sortable dates instead of relying on manual input.

### 2. Using `None` for Empty Values
**Why `None` instead of empty strings?**

```python
# ✅ Semantic meaning: "value doesn't exist yet"
'date_watched': None
'rating': None

# ❌ Less clear: "value exists but is empty"
'date_watched': ""
'rating': ""
```

**Practical benefit:** Clean conditional checks
```python
if item['date_watched']:        # False when None, True when date exists
    print("Already watched!")
```

### 3. Input Validation with Loops
**Pattern:** Keep asking until you get valid input

```python
while True:
    try:
        priority = int(input("Priority (1-5, 1=highest): "))
        if 1 <= priority <= 5:
            break  # Valid input - exit loop
        else:
            print("Priority must be between 1 and 5")
    except ValueError:
        print("Please enter a number between 1 and 5")
```

**Why this works:**
- `try` block attempts to convert input to integer
- `ValueError` catches non-numeric input ("two", "abc", etc.)
- Range check ensures number is 1-5
- Loop continues until both conditions pass

### 4. The `enumerate()` Function
**Purpose:** Get both index AND item when looping

```python
# Without enumerate - only get the item
for item in watchlist:
    print(item['title'])

# With enumerate - get position number too
for idx, item in enumerate(watchlist, 1):
    print(f"{idx}. {item['title']}")
```

**Parameters:**
- First: The list to loop through
- Second: Starting number (1 instead of default 0)

### 5. String Repetition Operator
**Pattern:** Create divider lines quickly

```python
print(f"{'='*80}")
# Output: ================================================================================

print(f"{'-'*40}")
# Output: ----------------------------------------
```

**Why:** Cleaner than typing 80 characters manually

### 6. Chained Comparisons
**Python allows elegant range checks:**

```python
# ✅ Python style - clean and readable
if 1 <= priority <= 5:
    print("Valid")

# ❌ Other languages - verbose
if priority >= 1 and priority <= 5:
    print("Valid")
```

---

## Code Structure

### Complete Working Code

```python
# watchlist.py - Movie/TV Show Watchlist Tracker - Practice Project
# Concepts Covered: Dictionaries, Lists, Functions, File I/O, Input Validation,
# Loops (while/for), datetime module, JSON data structure, enumerate(), string formatting

import json
from datetime import datetime

def create_item():
    """Create a new watchlist item"""
    print("\n--- Add New Item ---")
    
    title = input("Title: ").strip()
    item_type = input("Type (movie/show): ").strip().lower()
    recommended_by = input("Recommended by: ").strip()
    
    # Priority input with validation
    while True:
        try:
            priority = int(input("Priority (1-5, 1=highest): "))
            if 1 <= priority <= 5:
                break
            else:
                print("Priority must be between 1 and 5")
        except ValueError:
            print("Please enter a number between 1 and 5")
    
    imdb_link = input("IMDB link: ").strip()
    
    # Create the item dictionary
    item = {
        'title': title,
        'type': item_type,
        'recommended_by': recommended_by,
        'priority': priority,
        'date_added': datetime.now().strftime('%Y-%m-%d'),
        'date_watched': None,
        'rating': None,
        'notes': None,
        'imdb_link': imdb_link
    }
    
    return item

def display_all(watchlist):
    """Display all items in the watchlist"""
    if not watchlist:
        print("\nYour watchlist is empty!")
        return
    
    print(f"\n{'='*80}")
    print(f"{'WATCHLIST':^80}")
    print(f"{'='*80}\n")
    
    for idx, item in enumerate(watchlist, 1):
        status = "✓ WATCHED" if item['date_watched'] else "⏳ UNWATCHED"
        print(f"{idx}. {item['title']} ({item['type'].upper()}) - Priority: {item['priority']}")
        print(f"   Status: {status}")
        print(f"   Added: {item['date_added']} | Recommended by: {item['recommended_by']}")
        if item['date_watched']:
            print(f"   Watched: {item['date_watched']} | Rating: {item['rating']}/5")
            if item['notes']:
                print(f"   Notes: {item['notes']}")
        print(f"   IMDB: {item['imdb_link']}")
        print()

def main():
    """Main program loop"""
    watchlist = []
    
    print("=" * 80)
    print("MOVIE/TV SHOW WATCHLIST TRACKER".center(80))
    print("=" * 80)
    
    while True:
        print("\n--- MENU ---")
        print("1. Add item to watchlist")
        print("2. Display all items")
        print("3. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == '1':
            item = create_item()
            watchlist.append(item)
            print(f"\n✓ '{item['title']}' added to watchlist!")
        
        elif choice == '2':
            display_all(watchlist)
        
        elif choice == '3':
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
```

---

## Key Patterns Reinforced

### 1. Dictionary Creation Pattern
```python
# Build structured data with meaningful keys
item = {
    'key1': value1,
    'key2': value2,
    'key3': value3
}
```

### 2. List Management Pattern
```python
# Initialize empty list
watchlist = []

# Add items
watchlist.append(new_item)

# Loop through items
for item in watchlist:
    process(item)
```

### 3. Menu Loop Pattern
```python
while True:
    # Display options
    # Get user choice
    # Process choice
    # Break on exit condition
```

### 4. Function Return Pattern
```python
def create_item():
    # Gather data
    # Build structure
    return item  # Return the created object
```

---

## What I Learned

### Technical Skills
1. **Input validation** - Using while loops + try/except to ensure clean data
2. **Date handling** - Using datetime module for consistent timestamps
3. **None vs empty strings** - Semantic difference in data representation
4. **enumerate()** - Getting index + value in loops
5. **String operators** - Using `*` for repetition

### Programming Concepts
1. **Data structure design** - Choosing what fields to track
2. **Validation strategy** - Checking data BEFORE storing it
3. **User experience** - Clear prompts and formatted output
4. **Code organization** - Separating concerns into functions

### Debugging Practice
1. Read error messages carefully (syntax errors in example code)
2. Test each function independently
3. Verify data structure before processing

---

## Common Mistakes to Avoid

### 1. Wrong Dictionary Syntax
```python
# ❌ WRONG - Using = instead of :
item = {'title' = 'Movie'}

# ✅ CORRECT
item = {'title': 'Movie'}
```

### 2. Forgetting Quotes on Dictionary Keys
```python
# ❌ WRONG - Missing quotes
item = {title: 'Movie'}

# ✅ CORRECT
item = {'title': 'Movie'}
```

### 3. Using Dot Notation for Dictionary Access
```python
# ❌ WRONG - Python doesn't use dot notation for dicts
print(item.title)

# ✅ CORRECT - Use square brackets
print(item['title'])
```

### 4. Not Validating User Input
```python
# ❌ WRONG - Assumes user enters valid number
priority = int(input("Priority: "))  # Crashes on "abc"

# ✅ CORRECT - Validate with try/except
try:
    priority = int(input("Priority: "))
except ValueError:
    print("Please enter a number")
```

---

## Next Session Preview

**Session 2 Goals:**
- Save watchlist to file (JSON format)
- Load watchlist on startup
- Mark items as watched
- Add ratings and notes to watched items
- Search/filter functionality

**New concepts coming:**
- JSON file operations
- Data persistence
- Updating dictionary values
- List filtering/searching

---

## Self-Assessment Questions

Test your understanding:

1. **Why use `None` instead of `""` for `date_watched`?**
   - Answer: Semantic clarity - `None` means "doesn't exist yet" vs `""` means "exists but empty"

2. **What does `enumerate(watchlist, 1)` do?**
   - Answer: Loops through watchlist, provides both index (starting at 1) and item

3. **Why is the validation in a `while True` loop?**
   - Answer: Keeps asking until valid input is received, then breaks

4. **What happens if you forget the `break` in the validation loop?**
   - Answer: Infinite loop - even valid input won't exit

5. **What does `datetime.now().strftime('%Y-%m-%d')` return?**
   - Answer: Current date as string in YYYY-MM-DD format (e.g., '2025-12-07')

---

## Practice Challenges

Try these on your own:

1. **Add input validation** for item_type to only accept "movie" or "show"
2. **Enhance display** to show items sorted by priority (highest first)
3. **Add a counter** showing total unwatched vs watched items
4. **Create a function** to find items by title (search feature)

---

## Git Reminder

**Before ending session:**
```bash
git add watchlist.py
git commit -m "Session 1: Basic watchlist with add/display functions"
git push
```

---

## Session Notes

**What worked well:**
- TBD after session

**What was challenging:**
- TBD after session

**Questions for next session:**
- TBD after session

**Energy level at end:**
- TBD after session

---

*Session 1 of 3 - Foundation Complete ✅*  
*Next: File I/O and data persistence*
