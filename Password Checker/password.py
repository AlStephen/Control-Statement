def is_password_valid(password, difficulty):
    if difficulty == "Easy":
        # Check if password length is at least 6 characters
        if len(password) >= 6:
            return True
        else:
            # Provide feedback if password length is insufficient
            print("Password must be at least 6 characters long.")
            return False
    elif difficulty == "Medium":
        # Check if password length is at least 8 characters and contains at least one uppercase, one lowercase, and one digit
        if len(password) >= 8 and any(char.isupper() for char in password) \
                and any(char.islower() for char in password) and any(char.isdigit() for char in password):
            return True
        else:
            # Provide feedback on specific requirements not met
            feedback = []
            if len(password) < 8:
                feedback.append("Password must be at least 8 characters long.")
            if not any(char.isupper() for char in password):
                feedback.append("Password must contain at least one uppercase letter.")
            if not any(char.islower() for char in password):
                feedback.append("Password must contain at least one lowercase letter.")
            if not any(char.isdigit() for char in password):
                feedback.append("Password must contain at least one digit.")
            print('\n'.join(feedback))
            return False
    elif difficulty == "Hard":
        # Check if password meets Medium requirements and contains at least one special character
        if len(password) >= 8 and any(char.isupper() for char in password) \
                and any(char.islower() for char in password) and any(char.isdigit() for char in password) \
                and any(not char.isalnum() for char in password):
            return True
        else:
            # Provide feedback on specific requirements not met
            feedback = []
            if len(password) < 8:
                feedback.append("Password must be at least 8 characters long.")
            if not any(char.isupper() for char in password):
                feedback.append("Password must contain at least one uppercase letter.")
            if not any(char.islower() for char in password):
                feedback.append("Password must contain at least one lowercase letter.")
            if not any(char.isdigit() for char in password):
                feedback.append("Password must contain at least one digit.")
            if not any(not char.isalnum() for char in password):
                feedback.append("Password must contain at least one special character.")
            print('\n'.join(feedback))
            return False
    else:
        # Provide feedback for invalid difficulty level
        print("Invalid difficulty level.")
        return False


# Main code
password = input("Enter your password: ")
difficulty = input("Choose difficulty level (Easy, Medium, Hard): ")

if is_password_valid(password, difficulty):
    print("Password meets the complexity requirements for", difficulty)
else:
    print("Password does not meet the complexity requirements for", difficulty)
