# Week 2: Python Fundamentals & Project-Based Learning - Comprehensive Review

**Duration:** December 2-8, 2025 (7 days, scattered sessions)  
**Primary Project:** Movie/TV Show Watchlist Tracker (Multi-session)  
**Status:** 🔄 In Progress (Session 2 of 3 incomplete)

---

## Executive Summary

Week 2 focused on reinforcing Python fundamentals through practical project work. Unlike Week 1's rapid progression through multiple small projects, Week 2 adopted a multi-session approach with a single substantial project to improve concept retention. Progress was interrupted by life events (IoT hardware project, weekend commitments), resulting in incomplete session work but valuable real-world debugging experience.

**Key Achievement:** Successfully implemented persistent data storage using JSON, demonstrating understanding of file I/O and data structure preservation.

**Critical Gap Identified:** Conceptual understanding of Python object references and datetime module usage remains weak despite practical implementation.

---

## Self-Assessment: Skill Ratings (1-5 Scale)

### Strong Areas (4-5/5)

- **Dictionaries:** 4/5 - Can create, access, update without reference
- **Lists:** 4/5 - Comfortable with append, enumerate, basic operations
- **Functions:** 4/5 - Can write functions with parameters and return values
- **File I/O:** 5/5 - Solid understanding of `with` statements and file modes
- **JSON:** 4/5 - Understands why to use it and how it maps to Python data

### Development Areas (3/5)

- **Input Validation:** 3/5 - Can follow the pattern, cannot write from scratch

### Critical Gaps (1-2/5)

- **datetime Module:** 1/5 - Used it but doesn't understand how it works
- **Object References:** 1/5 - Fundamental Python concept not yet grasped

---

## Projects Completed

### 1. Log Parsing Fundamentals (Day 1)

**Status:** ✅ Complete  
**Retention:** High - Can replicate `split()` with limit pattern without reference

**Core Pattern Learned:**

```python
# Strategic splitting with limits
log_line = "2025-12-02 14:23:15 INFO Interface Gi0/1 status changed to UP"
parts = log_line.split(" ", 4)  # Split into exactly 5 pieces
# Result: ['2025-12-02', '14:23:15', 'INFO', 'Interface', 'Gi0/1 status changed to UP']
```

**Key Insight:** Don't split everything - split only what you need to separate reliably.

---

### 2. Contact Manager (Day 4)

**Status:** ✅ Complete  
**Retention:** Moderate - Can build from scratch with structural reference

**Skills Demonstrated:**

- Menu-driven program structure
- Basic CRUD operations (Create, Read)
- Understanding of global vs local variable scope
- Debugging infinite loops caused by variable scope errors

**Code Independence:** Could rebuild independently with reference to menu structure pattern.

---

### 3. Movie/TV Show Watchlist Tracker (Days 5-7)

**Status:** 🔄 In Progress (60% complete)  
**Independence Level:** 75% self-directed with guidance

**What Was Built:**

#### Session 1: Foundation ✅

- Data structure design (9-field dictionary)
- `create_item()` function with input validation
- `display_all()` function with formatted output
- Menu-driven interface
- Concepts: dictionaries, lists, functions, enumerate(), string formatting

#### Session 2: Persistence 🔄

- `save_watchlist()` - JSON file writing
- `load_watchlist()` - JSON file reading with error handling
- Auto-save after data changes
- **Bug Fixed:** Missing return statement in load function (student debugged independently)

#### Session 3: Not Started ⏸️

- Mark items as watched
- Add ratings and notes
- Search/filter functionality

**Student Contribution Breakdown:**

- Typed 100% of code manually (no copy/paste)
- Made independent decisions on menu wording and field names
- Debugged syntax errors (indentation, missing returns, typos)
- 25% followed specific instructions for complex logic patterns
- Successfully implemented file persistence after understanding JSON concept

---

## Core Concepts Covered

### 1. Dictionaries - Advanced Usage

**Creating Structured Data:**

```python
item = {
    'title': 'The Matrix',
    'type': 'movie',
    'priority': 1,
    'date_added': '2025-12-07',
    'date_watched': None,  # None vs empty string - semantic meaning
    'rating': None,
    'notes': None,
    'imdb_link': 'https://imdb.com/...'
}
```

**Key Pattern:** Use `None` for "doesn't exist yet" vs `""` for "exists but empty"

**Why it matters:**

```python
if item['date_watched']:  # False when None, True when date exists
    print("Already watched")
```

---

### 2. Lists - Practical Operations

**enumerate() - Getting Index + Value:**

```python
# Without enumerate
for item in watchlist:
    print(item['title'])

# With enumerate - get position number too
for idx, item in enumerate(watchlist, 1):
    print(f"{idx}. {item['title']}")  # Starts at 1 instead of 0
```

**List Filtering (Comprehension):**

```python
# Get only unwatched items
unwatched = [item for item in watchlist if not item['date_watched']]
```

---

### 3. Functions - Return Values & Parameters

**Function Structure:**

```python
def create_item():
    """Docstring explaining what function does"""
    # Gather data
    # Build structure
    return item  # Return the created object
```

**Key Understanding:** Functions can build complex data structures and return them for use elsewhere.

---

### 4. File I/O - JSON Persistence

**Why JSON over Plain Text:**

- Preserves data structure (lists, dicts, nested data)
- Handles data types automatically (int, str, None → null)
- Human-readable AND machine-parseable
- Industry standard for data exchange

**Saving Data:**

```python
def save_watchlist(watchlist, filename="watchlist.json"):
    """Save watchlist to JSON file"""
    with open(filename, 'w') as file:
        json.dump(watchlist, file, indent=2)  # indent=2 makes it readable
```

**Loading Data:**

```python
def load_watchlist(filename="watchlist.json"):
    """Load watchlist from JSON file"""
    try:
        with open(filename, 'r') as file:
            return json.load(file)  # Returns the loaded data structure
    except FileNotFoundError:
        return []  # Return empty list if file doesn't exist yet
```

**Critical Bug Fixed:**

- Original code created `watchlist` variable but didn't return it
- Function returned `None` by default, causing AttributeError
- Student identified and fixed independently

---

### 5. Input Validation - Pattern Recognition

**The Standard Pattern:**

```python
while True:
    try:
        value = int(input("Enter number (1-5): "))
        if 1 <= value <= 5:
            break  # Valid input - exit loop
        else:
            print("Must be between 1 and 5")
    except ValueError:
        print("Please enter a number")
```

**Why This Works:**

1. `while True` - keeps asking until valid input
2. `try` block - attempts type conversion
3. `ValueError` - catches non-numeric input
4. Range check - ensures number is in valid range
5. `break` - exits loop only when both conditions pass

**Current Skill Level:** Can implement when given the pattern, cannot write from scratch yet.

---

### 6. String Operations - Practical Usage

**String Repetition:**

```python
print(f"{'='*80}")  # Creates 80 equal signs
# Output: ================================================================================
```

**Chained Comparisons (Python-specific):**

```python
# ✅ Python style - elegant
if 1 <= priority <= 5:
    print("Valid")

# ❌ Other languages - verbose
if priority >= 1 and priority <= 5:
    print("Valid")
```

**String Methods:**

```python
text = "  Movie Title  "
text.strip()      # "Movie Title" - removes whitespace
text.lower()      # "  movie title  " - lowercase
text.upper()      # "  MOVIE TITLE  " - uppercase
```

---

## New Concepts Introduced

### 1. The datetime Module (⚠️ Gap Area)

**What It Does:** Provides professional date/time handling with consistent formatting.

**Usage in Project:**

```python
from datetime import datetime

# Get current date in YYYY-MM-DD format
current_date = datetime.now().strftime('%Y-%m-%d')
# Returns: '2025-12-07'
```

**Why We Use It:**

- Consistent date format (sortable, unambiguous)
- Avoids manual date entry errors
- Professional standard for timestamps

**Current Understanding:** Used it successfully but cannot explain how `strftime()` works or what other format codes exist.

**Week 3 Action:** Dedicate drill session to datetime formatting and manipulation.

---

### 2. Object References (⚠️ Critical Gap)

**The Concept:** In Python, variables don't "contain" objects - they reference/point to objects in memory.

**Example from mark_watched() function:**

```python
watchlist = [{'title': 'Test', 'date_watched': None}]

# Create filtered list
unwatched = [item for item in watchlist if not item['date_watched']]

# Get first unwatched item
selected = unwatched[0]

# Modify selected
selected['date_watched'] = '2025-12-07'

# Check original watchlist
print(watchlist[0]['date_watched'])  # '2025-12-07' - IT CHANGED!
```

**Why This Happens:**

- `unwatched` is a list of references to dictionary objects
- `selected` points to the SAME dictionary object that's in `watchlist`
- Modifying `selected` modifies the original object
- You're not making a copy - you're creating another name for the same object

**Visual Analogy:** Think of objects like houses with addresses:

- The house exists at one location (memory)
- Multiple people can know the address (variables)
- If someone goes to that address and paints the house, everyone sees the change
- The house itself didn't move - all the addresses still point to it

**Current Understanding:** Does not grasp this concept yet. Assumed `selected` was a copy that needed to be "put back."

**Week 3 Action:** Dedicated lesson on references, mutability, and when Python copies vs references.

---

## Key Patterns Reinforced

### 1. Menu Loop Pattern

```python
while True:
    # Display options
    print("\n--- MENU ---")
    print("1. Option One")
    print("2. Option Two")
    print("3. Exit")
    
    # Get user choice
    choice = input("\nChoice: ").strip()
    
    # Process choice
    if choice == '1':
        function_one()
    elif choice == '2':
        function_two()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
```

**Used in:** Contact Manager, Watchlist Tracker  
**Retention:** High - can replicate pattern

---

### 2. Function Return Pattern

```python
def build_something():
    # Gather data
    data = input("Enter data: ")
    
    # Build structure
    structure = {'key': data}
    
    # Return for use elsewhere
    return structure

# Use the returned value
result = build_something()
print(result['key'])
```

**Used in:** create_item(), load_watchlist()  
**Retention:** High - understands concept

---

### 3. File Persistence Pattern

```python
# Save after every change
def add_item():
    item = create_item()
    collection.append(item)
    save_to_file(collection)  # Immediate save

# Load on startup
def main():
    collection = load_from_file()  # Load existing data
    # ... rest of program
```

**Why:** Prevents data loss from crashes, power failures, accidents  
**Retention:** High - understood and implemented correctly

---

## Debugging Skills Developed

### 1. Syntax Debugging

**Errors Fixed Independently:**

- Indentation errors (Python-specific)
- Missing return statement in function
- Dictionary syntax (`:` vs `=`)
- String quote mismatches

**Skill Level:** Good - can read error messages and locate issues

---

### 2. Logic Debugging

**Issues Identified:**

- Variable scope (contact manager infinite loop)
- Function return values (None vs expected data)
- File mode selection (read vs write)

**Skill Level:** Developing - asks clarifying questions when stuck

---

### 3. Systematic Approach

**Process Demonstrated:**

1. Read error message carefully
2. Identify line number and error type
3. Check syntax first (simple errors)
4. Add print statements to inspect data
5. Change one thing at a time
6. Test after each change

**This is professional debugging methodology.**

---

## Real-World Application: IoT Project

### Project: Residential Asthma Environmental Monitoring System

**Hardware:**

- Raspberry Pi 4
- Sense HAT (temp, humidity, LED matrix)
- PMS5003 Particulate Matter Sensor
- CP2102 USB-to-UART adapter

**Software Stack:**

- Python (sensor reading, MQTT publishing)
- Mosquitto (MQTT broker)
- Home Assistant (dashboard/visualization)
- Pushover API (mobile alerts)

**Student's Role (Honest Assessment):**

- ✅ System Architecture: Designed hardware layout, identified GPIO conflicts
- ✅ Linux Administration: SSH, permissions, systemd services, MQTT broker config
- ✅ Integration: Home Assistant dashboard, ApexCharts visualization
- ✅ Debugging: Resolved MQTT authentication, USB device paths, permission errors
- ❌ Python Code: 100% AI-generated (paho-mqtt classes, sensor libraries)
- ⚠️ Configuration: Directed AI to refactor to config.json model

**Key Insight:** Operates as "System Integrator" - excellent at deploying and connecting systems, but still building foundational Python coding skills.

**Relevance to Career Goals:** This is exactly the type of work DevOps engineers do - integrating systems, troubleshooting infrastructure, automating workflows. The Python syntax will come with practice.

---

## Common Mistakes & Solutions

### 1. Forgetting Return Statements

```python
# ❌ WRONG - function returns None
def load_data():
    try:
        data = get_data()
    except:
        return []

# ✅ CORRECT - return in both cases
def load_data():
    try:
        return get_data()
    except:
        return []
```

### 2. Dictionary Syntax Errors

```python
# ❌ WRONG - using = instead of :
item = {'title' = 'Movie'}

# ✅ CORRECT
item = {'title': 'Movie'}
```

### 3. Not Saving After Changes

```python
# ❌ WRONG - only save on exit (data lost if crash)
if choice == '3':
    save_data()
    exit()

# ✅ CORRECT - save after each change
if choice == '1':
    add_item()
    save_data()  # Immediate persistence
```

---

## What Actually Works for Your Learning Style

### ✅ Effective Methods

1. **Multi-session projects** - Better retention than rapid fire
2. **Typing code manually** - No copy/paste, forces engagement
3. **Debugging own errors** - Builds problem-solving skills
4. **Real-world applications** - IoT project more engaging than abstract exercises
5. **Honest self-assessment** - Identifying gaps prevents false confidence

### ❌ Less Effective

1. **Abstract concept explanations** - Need concrete examples first
2. **Late night sessions when tired** - Recognized need to stop when not absorbing
3. **Rushing through concepts** - Better to drill fundamentals than move forward

---

## Git Workflow Progress

### Week 2 Commits

```bash
# Session 1
git add watchlist.py
git commit -m "Session 1: Basic watchlist with add/display functions"
git push

# Session 2 Part 1
git add watchlist.py
git commit -m "Session 2 Part 1: Added JSON file persistence (save/load)"
git push
```

**Habit Building:** Successfully pushed after both sessions (improvement from Week 1 missed push).

---

## Week 2 Statistics

**Sessions Completed:** 3 partial sessions (life interruptions)  
**Code Written:** ~150 lines (watchlist.py, manually typed)  
**Functions Created:** 4 (create_item, display_all, save_watchlist, load_watchlist)  
**Bugs Debugged:** 8+ (syntax, logic, missing returns)  
**Concepts Introduced:** 6 (datetime, JSON, None semantics, enumerate, object refs, validation)  
**GitHub Commits:** 2 ✅  
**Real-World Project:** 1 (IoT monitoring system - integration role)

---

## Critical Skills Assessment

### Can Do Confidently (No Reference)

- [x] Create and manipulate dictionaries
- [x] Loop through lists with enumerate
- [x] Write basic functions with returns
- [x] Read/write files with proper error handling
- [x] Save/load JSON data
- [x] Use f-strings for formatting
- [x] Debug syntax errors from error messages

### Can Do With Reference

- [x] Input validation pattern (while + try/except)
- [x] Menu-driven program structure
- [x] List comprehensions for filtering
- [x] Build multi-field data structures

### Cannot Do Yet

- [ ] Write input validation from scratch
- [ ] Explain datetime formatting codes
- [ ] Understand object references vs copies
- [ ] Design complex data structures independently
- [ ] Write MQTT/API integration code (IoT project)

---

## Week 3 Priorities

### 1. Close Knowledge Gaps (High Priority)

**Object References - Dedicated Lesson**

- Understand references vs copies
- When Python copies vs references
- Mutability implications
- Practical exercises with lists and dicts

**datetime Module - Practical Drill**

- Common format codes (%Y, %m, %d, %H, %M, %S)
- Parsing dates from strings
- Date arithmetic (adding days, comparing dates)
- Use cases in real projects

**Input Validation - Pattern Mastery**

- Write validation from scratch (no reference)
- Multiple validation patterns
- Custom error messages
- Integration into projects

---

### 2. Complete Watchlist Project

**Session 2 Completion:**

- Add mark_watched() function
- Test ratings and notes
- Verify file persistence works correctly

**Session 3: Enhancement**

- Search/filter by priority
- Sort by different fields
- Generate reports (unwatched count, top rated)
- **Then:** Line-by-line code review where YOU explain every line

---

### 3. Consolidation Exercises

**Mini-Projects (1-2 hour builds):**

- Simple expense tracker (practice datetime + file I/O)
- Quiz program (practice validation + scoring)
- Gym workout logger (practice data structures)

**Goal:** Build without instructions, only high-level requirements

---

### 4. Python Fundamentals Drills

**30-Minute Daily Challenges:**

- Write 5 different validation functions
- Parse 5 different log formats
- Create 5 different data structures
- Practice datetime operations

**Focus:** Speed and pattern recognition, not new concepts

---

## Recommended Study Approach

### Daily Structure (Weekdays - Limited Time)

- **15 min:** Review one previous concept (flashcard style)
- **30 min:** One focused drill (validation, datetime, or parsing)
- **5 min:** Document what you learned

### Weekend Structure (More Time Available)

- **Session 1 (2 hours):** Continue multi-session project
- **Break (1 hour)**
- **Session 2 (1 hour):** Concept drill or gap closure
- **15 min:** Week documentation and GitHub push

---

## Honest Assessment: Where You Stand

### Your Actual Skill Level

**Python Beginner+**: You're past "hello world" but not yet at "build anything independently."

**Specific Position:**

- Comfortable with basic syntax and data structures
- Can follow patterns and implement with guidance
- Good debugging instincts for syntax errors
- Struggle with conceptual gaps (references, datetime)
- Excellent at system integration (hardware, Linux, dashboards)

### Comparison to Your Goals

**Target Role:** DevOps/Cloud Engineer (18-month timeline)

**Relevant Skills Already Strong:**

- Linux system administration ✅
- Troubleshooting methodology ✅
- Hardware integration ✅
- Service management (systemd) ✅
- MQTT/IoT concepts ✅

**Skills Still Developing:**

- Python scripting fundamentals (in progress)
- Automation scripting (next phase)
- Infrastructure as Code (future: Terraform)
- Container orchestration (future: Kubernetes)

**Reality Check:** Your IoT project shows you're already functioning at a "Junior DevOps" level for system integration. The Python syntax will catch up with continued practice. Don't let imposter syndrome about "not writing the code" diminish what you actually accomplished - integration and troubleshooting ARE the job.

---

## Key Takeaways for Week 3

### 1. Drill the Gaps

Don't move forward until datetime and object references are solid. These are foundational concepts that will create confusion in advanced topics.

### 2. Build Without Instructions

Week 3 projects should start with requirements only: "Build a workout tracker that saves to JSON." Figure out the structure yourself, ask for help when stuck.

### 3. Focus on Pattern Recognition

You don't need to memorize syntax - you need to recognize "this is a validation situation" or "this needs file persistence."

### 4. Leverage Your Strengths

You're strong at integration and troubleshooting. Projects that combine Python + Linux + hardware will be more engaging than pure coding exercises.

### 5. Be Honest About Learning Speed

You're not racing anyone. A solid foundation now prevents having to relearn basics later while trying to understand AWS or Kubernetes.

---

## Resources Used

**Official Documentation:**

- Python docs (dictionaries, file I/O)
- JSON documentation

**Projects:**

- Week 2 daily notes (Day 1, Day 4, Day 5)
- Watchlist tracker code
- IoT project documentation

**AI Assistance:**

- Claude: Instruction, debugging, concept explanation
- Gemini: IoT project Python code generation

---

## Next Session Preview

**Monday/Tuesday Priority:** Complete Watchlist Session 2

- Add mark_watched() function (code already provided)
- Test functionality
- Line-by-line code review

**Wednesday-Friday:** Dedicated concept drills

- Object references lesson
- datetime module practice
- Validation pattern mastery

**Weekend:** Watchlist Session 3 + Weekly review

---

_Week 2 Review Completed: December 8, 2025_  
_Status: Foundational skills solid, critical gaps identified, ready for targeted improvement_  
_Next Focus: Close knowledge gaps before advancing to new concepts_