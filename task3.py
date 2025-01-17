import random

def rock_paper_scissors():
    print("Welcome to the Rock-Paper-Scissors Game!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.\n")
    
    # Initialize scores
    user_score = 0
    computer_score = 0

    while True:
        # User input
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Computer's random choice
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display scores
        print(f"Scores: You {user_score} - {computer_score} Computer")

        # Play again?
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\nThank you for playing Rock-Paper-Scissors!")
            print(f"Final Scores: You {user_score} - {computer_score} Computer")
            if user_score > computer_score:
                print("Congratulations, you are the overall winner!")
            elif user_score < computer_score:
                print("Computer is the overall winner. Better luck next time!")
            else:
                print("It's an overall tie!")
            break

if _name_ == "_main_":
    rock_paper_scissors()