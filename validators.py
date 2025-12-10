# Integer Range Validator
def get_valid_integer(prompt, min_value, max_value):
    while True:
        print(f"{prompt} (between {min_value} and {max_value}): ")
        try:
            value = int(input()) # Get user input and convert to integer
            if min_value <= value <= max_value: # Check if within range
                return value
            else:
                print(f"Please enter an integer between {min_value} and {max_value}.")
        except ValueError: # Handle non-integer inputs
            print("Invalid input. Please enter a valid integer.")
            

value = get_valid_integer(f"Enter an integer:", min_value=1, max_value=100) 
print(f"You entered: {value}") 

# Yes/No Validator
def get_yes_no(prompt):
    while True:
        choice = input(f"{prompt} (yes/no): ").strip().lower() # Get user input and normalize
        if input = "Yes, y, No, n":
            return choice
        else:
            print("Invalid input. Please enter 'yes' or 'no'.") 
    
choice = get_yes_no("Do you want to continue?") #
print(f"You chose: {choice}")



# Choice Validator
def get_choice(prompt, options): 
    while True:
        print(f"{prompt} ({', '.join(options)})")
        choice = input(prompt).strip().lower()
        
        if choice in [opt.lower() for opt in options]:
            return choice
        else:
            print(f"Invalid choice. Please choose from: {', '.join(options)}")
        
options = ["fire", "water", "grass"]
choice = get_choice("Choose a Pokemon type:", options)
print(f"You chose: {choice}")