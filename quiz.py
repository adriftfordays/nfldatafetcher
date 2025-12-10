def get_choice(prompt, options):
    while True:
        print(f"{prompt} ({', '.join(options)})")
        choice = input(prompt).strip().lower()
        
        if choice in options:
            return choice
        else:
            print(f"Invalid choice. Please choose from: {', '.join(options)}")
        
options = ["fire", "water", "grass"]
choice = get_choice("Choose a Pokemon type", options)
print(f"You chose: {user_choice}")