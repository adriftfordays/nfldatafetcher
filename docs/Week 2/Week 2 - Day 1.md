`# LOG PARSING FUNDAMENTALS - REFERENCE GUIDE
# Session Date: December 2, 2025
# Goal: Master the fundamental pattern of converting unstructured text to structured data

"""
KEY INSIGHT: This pattern (split + limit + dictionary) is used everywhere in 
professional development - logs, CSV files, configuration files, API responses.
Master this pattern and you'll recognize it in countless real-world scenarios.
"""

# ============================================================================
# CORE CONCEPT: Strategic Splitting with Limits
# ============================================================================

# THE PROBLEM: Standard split() creates chaos with multi-word fields
log_line = "2025-12-02 14:23:15 INFO Interface Gi0/1 status changed to UP"

# ❌BAD APPROACH - splits everything:
```python
bad_split = log_line.split(" ")
print("Bad split result:", bad_split)
```
# Result: ['2025-12-02', '14:23:15', 'INFO', 'Interface', 'Gi0/1', 'status', 'changed', 'to', 'UP']
# Problem: Too many pieces, can't reliably access specific fields

# ✅GOOD APPROACH - split with limit:
```python
parts = log_line.split(" ", 4)  # Split on spaces, but only make 4 splits (5 pieces total)
print("Smart split result:", parts)
```
# Result: ['2025-12-02', '14:23:15', 'INFO', 'Interface', 'Gi0/1 status changed to UP']

# WHY THIS WORKS:
# - First 4 fields are predictable (date, time, level, interface)  
# - Everything else goes into the last piece as the "message"
# - Now we can reliably access each component

# ============================================================================
# FUNDAMENTAL PATTERN: List to Dictionary Conversion
# ============================================================================

# Step 1: Access individual pieces using list indexing

```cpp
`date = parts[0]        # '2025-12-02'`
`time = parts[1]        # '14:23:15'`  
`level = parts[2]       # 'INFO'`
`interface = parts[3]   # 'Interface'`
`message = parts[4]     # 'Gi0/1 status changed to UP'`
```


# Step 2: Create structured data with meaningful labels
```cpp
log_info = {
    "date": parts[0],
    "time": parts[1], 
    "level": parts[2],
    "interface": parts[3],
    "message": parts[4]
}

print("Structured log data:", log_info)
```


# Step 3: Access structured data using meaningful keys
```cpp

`print("Event occurred on:", log_info["date"] + " at " + log_info["time"])`
`print("Severity level:", log_info["level"])`
`print("Full message:", log_info["message"])`
```
# ============================================================================
# KEY INSIGHTS FROM TODAY'S SESSION
# ============================================================================

"""
1. PATTERN RECOGNITION: The key skill is learning to see structure in 
   unstructured text. Look for consistent separators and field positions.

2. STRATEGIC LIMITING: Don't split everything - split only what you need to 
   separate reliably. Let complex fields remain together in the final piece.

3. MEANINGFUL NAMES: Use descriptive dictionary keys that make code self-documenting.
   ***"date" is better than "field1" or "parts[0]"***

4. BUILD IN STEPS: 
   - First understand the data structure
   - Then write the split logic  
   - Then create the dictionary
   - Finally access the data you need

5. PROFESSIONAL DEBUGGING: When code gets messy, step back and document what 
   works before moving forward. This prevents the "spaghetti code" trap.
"""

# ============================================================================
# SYNTAX REMINDERS - COMMON MISTAKES TO AVOID
# ============================================================================

# DICTIONARY CREATION - Common errors:
# ❌ WRONG: 
```cpp
log_info = {"date" = parts[0]}     # Using = instead of :
```
# ❌ WRONG: 
```cpp
log_info = {date: parts[0]}        # Missing quotes on key
```
# ✅ RIGHT: 
```cpp
log_info = {"date": parts[0]}      # Colon for assignment, quotes for string keys
```

# DICTIONARY ACCESS - Common errors:  
# ❌ WRONG: 
```cpp
log_info.date                      # Using dot notation (wrong language)
```
# ❌ WRONG: 
```cpp
log_info[date]                     # Missing quotes
```
# ✅ RIGHT: 
```cpp
log_info["date"]                   # Square brackets with quoted key
```

# SPLIT WITH LIMIT - Common errors:
# ❌ WRONG: 
```cpp
parts = log_line.split("", 4)      # Empty string delimiter
```  
# ❌ WRONG:
```cpp
parts = log_line.split(" ", "4")   # Number as string
```
# ✅ RIGHT: 
```python
`parts = log_line.split(" ", 4)     # Space delimiter, integer limit`
```

# ============================================================================
# TOMORROW'S PRACTICE DIRECTION
# ============================================================================

"""
GOAL: Apply this same pattern to different types of structured text data.
Practice until you can see the pattern instantly and implement without reference.

PRACTICE AREAS:
1. Different log formats (Apache, system logs, application logs)
2. Configuration files (key=value pairs)
3. CSV-like data with embedded spaces
4. Network protocol messages
5. Error messages with consistent structure

SKILL BUILDING FOCUS:
- Recognize patterns quickly
- Choose optimal split strategies
- Create meaningful data structures  
- Access data efficiently

Remember: The syntax is easy once you understand the pattern. 
Focus on pattern recognition and logical structure first.
"""

# ============================================================================
# EXAMPLES FOR SELF-TESTING
# ============================================================================

# Try these examples to test your understanding:

example1 = "192.168.1.100 - user [02/Dec/2025:14:23:15] GET /api/status 200"
example2 = "CRITICAL: Database connection failed after 3 retry attempts"  
example3 = "eth0: Link speed changed from 100Mbps to 1000Mbps full duplex"

# Questions for each:
# 1. What are the distinct pieces of information?
# 2. Where should you place your split limit?
# 3. What meaningful names would you give each piece?
# 4. How would you access the most important data points?`