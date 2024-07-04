import random

class Mastermind:
    def __init__(self, secret_length):
        self.secret_length = secret_length
        self.secret_number = self.generate_secret_number()
        self.num_attempts = 0

    def generate_secret_number(self):
        return "".join(str(random.randint(0, 9)) for _ in range(self.secret_length))

    def hint(self, guess):
        correct_digits = [digit for digit in guess if digit in self.secret_number]
        correct_positions = [digit for digit in guess if digit == self.secret_number[guess.index(digit)]]
        return correct_digits, correct_positions

    def play(self, player):
        while True:
            guess = input(f"Player {player}, enter your guess ({self.secret_length}-digit number): ").strip()
            while len(guess) != self.secret_length:
                guess = input(f"Invalid guess. Enter your guess ({self.secret_length}-digit number): ").strip()

            correct_digits, correct_positions = self.hint(guess)
            print(f"Correct digits: {correct_digits}")
            print(f"Correct digits in correct positions: {correct_positions}")

            self.num_attempts += 1
            if guess == self.secret_number:
                print(f"Player {player} wins!")
                print(f"Number of attempts: {self.num_attempts}")
                break

def play_mastermind():
    secret_length = int(input("Enter the length of the secret number: "))
    game = Mastermind(secret_length)

    for player in range(1, 3):
        print(f"\nPlayer {player}'s turn")
        game.play(player)

if __name__ == "__main__":
    play_mastermind()