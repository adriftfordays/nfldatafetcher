# Week 3 - Day 2: Building Reusable Validation Library
# Session Date: December 10, 2025
# Goal: Write validation functions from memory and build reusable library

---

## Session Overview

**Focus:** Input validation pattern mastery + building reusable code library  
**Time Invested:** ~3 hours (9:00pm-12:18am - stayed up too late)  
**Completion Status:** 80% - core functions written, needs bug fixes and file separation  
**External Accountability:** Joined Discord VC with other developers

---

## What I Built

### validators.py Library (In Progress)

**Three validation functions:**
1. `get_valid_integer(prompt, min_value, max_value)` - ✅ Works correctly
2. `get_yes_no(prompt)` - ⚠️ Bug: returns string instead of boolean
3. `get_choice(prompt, options)` - ⚠️ Bug: case sensitivity issue

---

## Key Concept: Boolean Returns vs String Returns

### The Problem I Had

**My buggy code:**
```python
def get_yes_no(prompt):
    while True:
        choice = input(f"{prompt} (yes/no): ").strip().lower()
        if choice in ['yes', 'y', 'no', 'n']:
            return choice  # BUG: Returns "yes" or "no" string
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
```

**Why this is wrong:**
- Returns the actual string the user typed ("yes", "y", "no", "n")
- Makes the calling code awkward to use
- Have to check again: `if answer in ['yes', 'y']:`

---

### The Correct Approach

**Fixed code:**
```python
def get_yes_no(prompt):
    while True:
        choice = input(f"{prompt} (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return True  # Convert to boolean
        elif choice in ['no', 'n']:
            return False  # Convert to boolean
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
```

**Why this is better:**
- Returns `True` or `False` (boolean values)
- Calling code is clean: `if get_yes_no("Continue?"):`
- Function handles all the string checking internally

---

### Understanding Booleans

**What is a boolean?**
- A data type with only TWO possible values: `True` or `False`
- Used for yes/no, on/off, valid/invalid decisions
- NOT a string - it's its own type

**Examples:**
```python
# Boolean values
is_valid = True
should_continue = False

# Strings that LOOK like booleans (but aren't)
answer = "true"   # This is a STRING, not a boolean
result = "False"  # This is a STRING, not a boolean

# Check the type
print(type(True))      # <class 'bool'>
print(type("true"))    # <class 'str'>
```

---

### Why Return Boolean Instead of String?

**Bad pattern (returning string):**
```python
answer = get_yes_no("Delete file?")  # Returns "yes" or "no"

# Now you have to check the string
if answer == "yes" or answer == "y":
    delete_file()
```

**Good pattern (returning boolean):**
```python
answer = get_yes_no("Delete file?")  # Returns True or False

# Clean conditional
if answer:
    delete_file()
```

**The function "translates" user input into a boolean:**
- User types: "yes", "y", "YES", "Y" → Function returns: `True`
- User types: "no", "n", "NO", "N" → Function returns: `False`

---

## Boolean Drill Exercises

### Exercise 1: Predict the Output

```python
def get_yes_no(prompt):
    choice = input(f"{prompt} (yes/no): ").strip().lower()
    if choice in ['yes', 'y']:
        return True
    elif choice in ['no', 'n']:
        return False

# User types "yes"
result = get_yes_no("Continue?")
print(type(result))  # What prints?
print(result)        # What prints?

# User types "no"
result = get_yes_no("Continue?")
print(type(result))  # What prints?
print(result)        # What prints?
```

**Answers:**
- First: `<class 'bool'>` and `True`
- Second: `<class 'bool'>` and `False`

---

### Exercise 2: Using Boolean Returns

```python
def should_save():
    """Ask user if they want to save"""
    choice = input("Save changes? (yes/no): ").strip().lower()
    if choice in ['yes', 'y']:
        return True
    elif choice in ['no', 'n']:
        return False

# Use it in code
if should_save():
    print("Saving...")
else:
    print("Not saving")
```

**Why this is clean:**
- `if should_save():` reads like English
- No need to check `== True` - booleans work directly in conditions

---

### Exercise 3: Common Boolean Mistakes

**Mistake 1: Checking == True (unnecessary)**
```python
# ❌ Redundant
if get_yes_no("Continue?") == True:
    do_something()

# ✅ Better
if get_yes_no("Continue?"):
    do_something()
```

**Mistake 2: Returning string instead of boolean**
```python
# ❌ Wrong - returns string
def is_adult(age):
    if age >= 18:
        return "yes"
    return "no"

# ✅ Correct - returns boolean
def is_adult(age):
    if age >= 18:
        return True
    return False

# ✅ Even better - direct boolean expression
def is_adult(age):
    return age >= 18
```

**Mistake 3: Confusing string "True" with boolean True**
```python
result = "True"  # This is a STRING

if result:  # This is True because non-empty strings are truthy
    print("Runs")

if result == True:  # This is False because "True" != True
    print("Doesn't run")
```

---

## Bugs to Fix Tomorrow

### Bug 1: Double prompt in get_valid_integer
```python
# Current (wrong):
print(f"{prompt} (between {min_value} and {max_value}): ")
value = int(input(prompt))  # User sees prompt TWICE

# Fixed:
value = int(input(f"{prompt} (between {min_value} and {max_value}): "))
```

### Bug 2: Boolean return in get_yes_no
```python
# Current (wrong):
return choice  # Returns "yes" or "no" string

# Fixed:
if choice in ['yes', 'y']:
    return True
elif choice in ['no', 'n']:
    return False
```

### Bug 3: Case sensitivity in get_choice
```python
# Current (wrong):
if choice in options:  # Fails if options = ["Fire"] and user types "fire"

# Fixed:
if choice in [opt.lower() for opt in options]:
```

---

## File Structure to Implement Tomorrow

**Current:** Everything in one file (messy)

**Target structure:**
```
project/
├── validators.py       # Library - functions only, no test code
└── test_validators.py  # Test file - imports and tests functions
```

**validators.py should contain:**
```python
"""
Reusable input validation functions
"""

def get_valid_integer(prompt, min_value, max_value):
    """Get integer within range"""
    # function only

def get_yes_no(prompt):
    """Get yes/no answer, returns boolean"""
    # function only

def get_choice(prompt, options):
    """Get choice from list of options"""
    # function only
```

**test_validators.py should contain:**
```python
from validators import get_valid_integer, get_yes_no, get_choice

# Test each function
value = get_valid_integer("Enter number", 1, 100)
print(f"You entered: {value}")

answer = get_yes_no("Continue?")
print(f"Boolean result: {answer}")

choice = get_choice("Pick color", ["red", "blue", "green"])
print(f"You chose: {choice}")
```

---

## Discord VC Learnings

**Experience:**
- Joined Discord VC with other developers
- Much of the conversation was over my head (JavaScript, advanced concepts)
- Picked up some terminology even if details unclear
- Realized: it's okay to work alongside others even if not following every detail

**Key Insight:**
External accountability helps with consistency, even if the technical discussion is above current level.

---

## Tomorrow Morning Tasks

**Priority 1: Fix bugs in validators.py**
1. Remove double prompt in get_valid_integer
2. Fix boolean return in get_yes_no
3. Fix case sensitivity in get_choice

**Priority 2: Separate into two files**
1. Create clean validators.py (functions only)
2. Create test_validators.py (import and test)

**Priority 3: Test thoroughly**
1. Run test file
2. Try edge cases (invalid inputs, case variations)
3. Verify all three functions work correctly

**Time estimate:** 30 minutes fresh in the morning

---

## Pattern Recognition from Tonight

**Common validation structure:**
```python
def validate_something(prompt, validation_params):
    while True:
        # Get user input
        user_input = input(prompt)
        
        # Validate it
        if is_valid(user_input, validation_params):
            # Convert to appropriate type if needed
            return processed_value
        else:
            # Show error and loop
            print("Error message")
```

**What changes per validator:**
- The validation check (`is_valid` logic)
- The return type (int, bool, string)
- The error message

**What stays the same:**
- `while True` loop structure
- Get input → check → return or error pattern

---

## Retention Check for Tomorrow

**Can you explain without looking:**

1. **Why return `True/False` instead of "yes"/"no" string?**
   - Answer: Cleaner calling code, direct use in conditionals

2. **What's the difference between `True` and `"True"`?**
   - Answer: `True` is boolean type, `"True"` is string type

3. **Why did you keep writing `if input in options:` instead of `if choice in options:`?**
   - Answer: Mental confusion between `input` (function) and `choice` (variable)

---

## Session Statistics

**Time Invested:** 3+ hours (too long, stayed up past bedtime)  
**Functions Written:** 3 (all from memory)  
**Bugs Introduced:** 3 (fixable tomorrow)  
**External Accountability:** Discord VC session  
**GitHub Commit:** ✅ Pushed (WIP state)

**Energy Level:** 2/10 by end (too tired, making simple mistakes)  
**Learning Quality:** 7/10 (good retention, but quality degraded after 2 hours)

---

## Key Takeaways

1. **Stop when tired:** Quality drops sharply after ~2 hours of focused coding
2. **Boolean vs string returns matter:** Affects code usability significantly  
3. **Library code should be clean:** Separate functions from test code
4. **External accountability works:** Discord VC helped maintain focus
5. **Fresh eyes fix bugs fast:** Don't debug when exhausted

---

*Session completed: December 10, 2025 at 12:18am EST*  
*Over-stayed by 1.5 hours - remember to set hard stop time*  
*Tomorrow: 30-minute cleanup session (9:30am or 9:00pm)*
