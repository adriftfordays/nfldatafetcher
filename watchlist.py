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
        
def mark_watched (watchlist):
    """Mark an item as watched and add rating/notes"""
    if not watchlist:
        print("\nYour watchlist is empty!")
        return
    
    # Show unwatched items only
    unwatched = [item for item in watchlist if not item['date_watched']]
    
    if not unwatched:
        print("\nNo Unwatched Items!")
        return
    
    print("\n===UNWATCHED ITEMS===")
    for idx, item in enumerate(unwatched, 1):
        print(f"{idx}, {item['title']} ({item['type']}) - Priority: {item['priority']}")
        
    #Get User Selection
        while True:
            try:
                choice = int(input("\nWhich item did you watch? (number): "))
                if 1 <= choice <= len(unwatched):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(unwatched)}")
            except ValueError:
                print("Please enter a valid number")
                
#Get Selected Item
    selected = unwatched[choice - 1]

# Mark as watched with today's date
    selected['date_watched'] = datetime.now().strftime('%Y-%m-%d')

#Get Rating
    while True:
        try:
            rating = int(input("Rating (1-5): "))
            if 1 <= rating <= 5:
                selected['rating'] = rating
                break
            else:
                print("Rating must be between 1 and 5")
        except ValueError:
            print("Please enter a number between 1 and 5")
        
#Get Notes (Optional)
    notes = input("Notes (press Enter to skip): ").strip()
    if notes:
        selected['notes'] = notes
    
    print(f"\n✓ Marked '{selected['title']}' as watched!")
    
def search_filter(watchlist):
    """Search and filter the watchlist"""
    if not watchlist:
        print("\nYour watchlist is empty!")
        return
    
    print("\n--- Search & Filter ---")
    print("1. Search by Title")
    print("2. Show unwatched only")
    print("3. Show watched only")
    print("4. Sort by Priority")
    print("5. Back to Main Menu")
    
    choice = input("\nChoice: ").strip()
    
    if choice == '1':
        #Search By Title
        search_term = input("Enter search term: ").strip().lower()
        results = [item for item in watchlist if search_term in item['title'].lower()]
        
        if results:
            print(f"\n ---Found {len(results)} match(es) ---")
            for idx, item in enumerate(results, 1):
                status = "✓" if item['date_watched'] else "⏳"
                print(f"{idx}. {status} {item['title']} - Priority: {item['priority']}")
                
        else:
            print("\nNo Matches Found")
            
    if choice == '2':
        #Show Unwatched Items
        unwatched = [item for item in watchlist if not item['date_watched']]
        
        if unwatched:
            print("\n=== Unwatched Items ===")
            for idx, item in enumerate(unwatched, 1):
                print(f"{idx}. {item['title']} - Priority: {item['priority']}")
                
        else:
            print("\nNo Unwatched Items!")
            
    if choice == '3':
        #Show Watched Items
        watched = [item for item in watchlist if item['date_watched']]
        
        if watched:
            print(f"\n=== Watched Items ===")
            for idx, item in enumerate(watched, 1):
               print(f"{idx}. {item['title']} - Priority: {item['priority']}")
               
        else:
            print("\nNo Watched Items!")
            
    if choice == '4':
        #Show By Priority
        sorted_list = sorted(watchlist, key=lambda x: x['priority'])
        
        if sorted_list:
            print(f"\n===List Sorted by Priority===")
            for idx, item in enumerate(sorted_list, 1):
                status = "✓" if item['date_watched'] else "⏳"
                print(f"{idx}. {status} {item['title']} - Priority: {item['priority']}")
            
        else:
            print("\nNo List Items!")
            
    elif choice == '5':
        return
                           
        
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
        print("4. Mark Item as Watched")
        print("5. Search Watchlist")
        
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
        
        elif choice == '4':
            mark_watched(watchlist)
            save_watchlist(watchlist)
            
        elif choice == '5':
            search_filter(watchlist)
            
        else:
            print("Invalid Choice. Please a choice between 1 and 5.")
            
if __name__ == "__main__":
    main()
    