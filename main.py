import tkinter as tk
import random

# Define the gestures
gestures = ["rock", "paper", "scissors"]

# Function to play the game
def play_game(player_choice):
    # Get the computer's choice
    computer_choice = random.choice(gestures)

    # Determine the winner
    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        result_label.config(text="You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        result_label.config(text="You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        result_label.config(text="You win!")
    else:
        result_label.config(text="You lose!")

    choices_label.config(text="You chose " + player_choice + " and the computer chose " + computer_choice + ".")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x300+0+0")

# Create the labels
result_label = tk.Label(root, text="Make your choice")
result_label.pack()

choices_label = tk.Label(root, text="")
choices_label.pack()

# Create the buttons
rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.pack()

# Start the main loop
root.mainloop()
