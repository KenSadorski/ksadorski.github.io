# Constants for the correct username and password
CORRECT_USERNAME = "h"
CORRECT_PASSWORD = "m"
MAX_ATTEMPTS = 5

def authenticate():
    attempts = 0
    
    while attempts < MAX_ATTEMPTS:
        username = input("Please enter username: ")
        password = input("Please enter password: ")
        
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            print("Welcome to the program!")
            return True
        else:
            attempts += 1
            remaining_attempts = MAX_ATTEMPTS - attempts
            print("Authentication Failed.")
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} attempt(s) remaining.")
            else:
                print("Locked Out.")
    
    return False

# Run the authentication function
if __name__ == "__main__":
    authenticate()
