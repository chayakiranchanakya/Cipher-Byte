import random

class RockPaperScissor:
    def __init__(self):
        self.choices = ["rock", "paper", "scissor"]
        self.winning_rules = {
            "rock": "scissor",
            "paper": "rock",
            "scissor": "paper"
        }

    def play(self):
        user_choice = input("Enter your choice (rock/paper/scissor): ").lower()
        while user_choice not in self.choices:
            user_choice = input("Invalid choice. Enter your choice (rock/paper/scissor): ").lower()

        computer_choice = random.choice(self.choices)
        print(f"\nComputer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif self.winning_rules[user_choice] == computer_choice:
            print("You win!")
        else:
            print("You lose!")

    def play_again(self):
        play_again = input("Play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid choice. Play again? (yes/no): ").lower()

        if play_again == "yes":
            self.play()
        else:
            print("Thanks for playing!")

if __name__ == "__main__":
    game = RockPaperScissor()
    game.play()
    game.play_again()