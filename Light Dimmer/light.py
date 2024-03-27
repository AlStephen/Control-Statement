def adjust_light(level):
    # Function to adjust the light based on the provided level
    if level == 0:
        print("Turning off the light.")
    elif level == 1:
        print("Setting light to Low (25%).")
    elif level == 2:
        print("Setting light to Medium (50%).")
    elif level == 3:
        print("Setting light to High (75%).")
    elif level == 4:
        print("Setting light to Maximum (100%).")
    else:
        print("Invalid input. Please enter a number between 0 and 4.")


# Main loop to continuously prompt the user to adjust the light
while True:
    user_input = input("Enter the level to adjust the light (0: Off, 1: Low, 2: Medium, 3: High, 4: Maximum): ")
    # Check if the user input is a digit
    if user_input.isdigit():
        level = int(user_input)  # Convert the user input to an integer
        # Check if the integer is within the valid range (0 to 4)
        if 0 <= level <= 4:
            adjust_light(level)  # Call the adjust_light function with the provided level
            if level == 0:
                break  # Exit the loop if the user chooses to turn off the light
        else:
            print("Invalid input. Please enter a number between 0 and 4.")
    else:
        print("Invalid input. Please enter a number between 0 and 4.")
