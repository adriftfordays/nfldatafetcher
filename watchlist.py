# watchlist.py - Movie/TV Show Watchlist Tracker - Practice Project
# Concepts Covered: Dictionaries, Lists, Functions, File I/O, Input Validation, 
# Loops (while/for), datetime module, JSON data structure, enumerate(), string formatting


import json
from datetime import datetime

def load_watchlist(filename="watchlist.json"):
    """Load the watchlist from a JSON file"""
    try:
        with open(filename, 'r') as file:
           return json.load(file)
    except FileNotFoundError:
        # If file not found or doesn't exist, return empty list
        return []

def save_watchlist(watchlist, filename="watchlist.json"):
    """Save the watchlist to a JSON file"""
    with open(filename, 'w') as file:
        json.dump(watchlist, file, indent=2)
    print(f"\n✓ Watchlist saved to {filename}.")
   
def create_item():
    """Create a new watchlist item"""
    print("\n--- Add New Item ---")
    
    title = input("Title: ").strip()
    item_type = input("Type (Movie/TV Show): ").strip().lower()
    recommended_by = input("Recommended by: ").strip()
    
    # Priority input validation
    while True:
        try:
            priority = int(input("Priority (1-5, 1=highest): " ))
            if 1 <= priority <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            
    imdb_link = input("IMDb Link: ").strip()
    
    #Create the item dictionary
    item = {
        "title": title,
        "type": item_type,
        "recommended_by": recommended_by,
        "priority": priority,
        "date_added": datetime.now().strftime('%Y-%m-%d'),
        "date_watched": None,
        "rating": None,
        "notes": None,      
        "imdb_link": imdb_link,
    }
    
    return item

def display_all(watchlist):
    """Display all items in the watchlist"""
    if not watchlist:
        print("\n Your Watchlist is empty!")
        return
    
    print(f"\n{'='*80}")
    print(f"{'WATCHLIST':^80}")
    print(f"{'='*80}\n")
    
    for idx, item in enumerate(watchlist, 1):
        status = "✓ WATCHED" if item['date_watched'] else "⏳ UNWATCHED"
        print(f"{idx}, {item['title']} ({item['type'].upper()}) - Priority: {item['priority']}")
        print(f" Status : {status}")
        print(f" Added: {item['date_added']} | Recommended by: {item['recommended_by']}")
        if item['date_watched']:
            print(f" Watched on: {item['date_watched']}) | Rating: {item['rating']}/5")
            if item ['notes']:
                print(f" Notes: {item['notes']}")
        print(f" IMDb: {item['imdb_link']}")
        print()
        
def main():
    """Main Program Loop"""
    watchlist = load_watchlist() # Load existing watchlist or start new
    
    if watchlist:
        print(f"\n✓ Loaded {len(watchlist)} items from watchlist.")      
       
    print("=" * 80)
    print("MOVIE/TV SHOW WATCHLIST TRACKER".center(80))
    print("=" * 80)
    
    while True:
        print("\n--- MENU ---")
        print("1. Add New Item to Watchlist")
        print("2. Display All Items")
        print("3. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == '1':
            item = create_item()
            watchlist.append(item)
            print(f"\n✓  '{item['title']}' added to watchlist!")
            save_watchlist(watchlist) # Save immediately after adding new item
            
        elif choice == '2':
            display_all(watchlist)
            
        elif choice == '3':
            print("\nGoodbye!")
            break
            
        else:
            print("Invalid Choice. Please enter 1, 2, or 3.")
            
if __name__ == "__main__":
    main()
    