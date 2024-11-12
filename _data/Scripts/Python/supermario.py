# Declare Variables
character = ""
stage = ""

# Define Yoshi ASCII Art for each color
yoshi_art = {
    "Yellow": [
        "░░░░░░░░░░░░░░░░░░░░",
        "░░░░░░▄▀▀▄▀▀▄░░░░░░░",
        "░░░░░█▒▄░▄░░▒█▄▄▄░░░",
        "░░░▄▄█░▀░▀░░░█▄▓▓█░░",
        "░▄▀▒▒▒▀▄▀▄▄▄▀▒▒▀█▓▄",
        "▄▀▀▒▀▒▒▒▒▒░░░▒▒▒█▓▓█",
        "█▒▒▒▒▒▒▒▒▄░░░░▒▒██▀",
        "▀▄▒▒▒▒▒▒▒█▀░░▒▄█▄▀░░",
        "░░▀▀▄▄▄▄█▄░░▒▒▀▄█▄▄░"
    ],
    "Red": [
        "░░░░░░░░░░░░░░░░░░░░",
        "░░░░░░▄▀▀▄▀▀▄░░░░░░░",
        "░░░░░█▒▄░▄░░▒█▄▄▄░░░",
        "░░░▄▄█░▀░▀░░░█▄▓▓█░░",
        "░▄▀▒▒▒▀▄▀▄▄▄▀▒▒▀█▓▄",
        "▄▀▀▒▀▒▒▒▒▒░░░▒▒▒█▓▓█",
        "█▒▒▒▒▒▒▒▒▄░░░░▒▒██▀",
        "▀▄▒▒▒▒▒▒▒█▀░░▒▄█▄▀░░",
        "░░▀▀▄▄▄▄█▄░░▒▒▀▄█▄▄░"
    ],
    "Blue": [
        "░░░░░░░░░░░░░░░░░░░░",
        "░░░░░░▄▀▀▄▀▀▄░░░░░░░",
        "░░░░░█▒▄░▄░░▒█▄▄▄░░░",
        "░░░▄▄█░▀░▀░░░█▄▓▓█░░",
        "░▄▀▒▒▒▀▄▀▄▄▄▀▒▒▀█▓▄",
        "▄▀▀▒▀▒▒▒▒▒░░░▒▒▒█▓▓█",
        "█▒▒▒▒▒▒▒▒▄░░░░▒▒██▀",
        "▀▄▒▒▒▒▒▒▒█▀░░▒▄█▄▀░░",
        "░░▀▀▄▄▄▄█▄░░▒▒▀▄█▄▄░"
    ],
    "Green": [
        "░░░░░░░░░░░░░░░░░░░░",
        "░░░░░░▄▀▀▄▀▀▄░░░░░░░",
        "░░░░░█▒▄░▄░░▒█▄▄▄░░░",
        "░░░▄▄█░▀░▀░░░█▄▓▓█░░",
        "░▄▀▒▒▒▀▄▀▄▄▄▀▒▒▀█▓▄",
        "▄▀▀▒▀▒▒▒▒▒░░░▒▒▒█▓▓█",
        "█▒▒▒▒▒▒▒▒▄░░░░▒▒██▀",
        "▀▄▒▒▒▒▒▒▒█▀░░▒▄█▄▀░░",
        "░░▀▀▄▄▄▄█▄░░▒▒▀▄█▄▄░"
    ],
    "Purple": [
        "░░░░░░░░░░░░░░░░░░░░",
        "░░░░░░▄▀▀▄▀▀▄░░░░░░░",
        "░░░░░█▒▄░▄░░▒█▄▄▄░░░",
        "░░░▄▄█░▀░▀░░░█▄▓▓█░░",
        "░▄▀▒▒▒▀▄▀▄▄▄▀▒▒▀█▓▄",
        "▄▀▀▒▀▒▒▒▒▒░░░▒▒▒█▓▓█",
        "█▒▒▒▒▒▒▒▒▄░░░░▒▒██▀",
        "▀▄▒▒▒▒▒▒▒█▀░░▒▄█▄▀░░",
        "░░▀▀▄▄▄▄█▄░░▒▒▀▄█▄▄░"
    ],
    "Orange": [
        "░░░░░░░░░░░░░░░░░░░░",
        "░░░░░░▄▀▀▄▀▀▄░░░░░░░",
        "░░░░░█▒▄░▄░░▒█▄▄▄░░░",
        "░░░▄▄█░▀░▀░░░█▄▓▓█░░",
        "░▄▀▒▒▒▀▄▀▄▄▄▀▒▒▀█▓▄",
        "▄▀▀▒▀▒▒▒▒▒░░░▒▒▒█▓▓█",
        "█▒▒▒▒▒▒▒▒▄░░░░▒▒██▀",
        "▀▄▒▒▒▒▒▒▒█▀░░▒▄█▄▀░░",
        "░░▀▀▄▄▄▄█▄░░▒▒▀▄█▄▄░"
    ]
}

# Ask the user to choose their character!
print("Choose your character (player1 = Mario, player2 = Luigi): ")

# User Inputs character choice
character = input()

# Begin If
if character == "player1":
    print("You have selected Mario!")
elif character == "player2":
    print("You have selected Luigi!")
else:
    print("GAME OVER")
    exit()  # Exit the program if invalid character is selected

# Choose Stage!
print("Choose a stage (star1, star2, or star3): ")

# Get Input
stage = input()

# Determine Yoshi Color and Display ASCII Art
yoshi_color = None

if stage == "star1" and character == "player1":
    yoshi_color = "Yellow"
elif stage == "star2" and character == "player1":
    yoshi_color = "Red"
elif stage == "star3" and character == "player1":
    yoshi_color = "Blue"
elif stage == "star1" and character == "player2":
    yoshi_color = "Green"
elif stage == "star2" and character == "player2":
    yoshi_color = "Purple"
elif stage == "star3" and character == "player2":
    yoshi_color = "Orange"
else:
    print("GAME OVER")
    exit()  # Exit the program if an invalid stage is selected

# Display the Yoshi ASCII Art based on the selected color
if yoshi_color:
    print(f"{character} found a {yoshi_color} Yoshi!")
    for line in yoshi_art[yoshi_color]:
        print(line)
