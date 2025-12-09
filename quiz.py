def get_choices(prompt, options):
    while True:
        print(f"{prompt} Options: {', '.join(options)}")
        choice = input("Enter the color of your choice: ").strip().lower()
        
        if choice in [opt.lower() for opt in options]:
            return choice
        else:
            print(f"Invalid choice. Please try again from the options: {', '.join(options)}")
            
prompt = "What is your favorite color?"
options = ["Red", "Blue", "Green", "Yellow"]
favorite_color = get_choices(prompt, options)
print(f"Your favorite color is: {favorite_color}")
