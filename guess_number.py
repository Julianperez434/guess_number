import sys
import time
import random

class Game:
    """
    A number guessing game between a user and CPU.

    Attributes:
        user_name (str): Name of the user.
        cpu_name (str): Name of the CPU.
        user_score (int): User's current score.
        cpu_score (int): CPU's current score.
        best_score (int): User's best score.
        cpu_best_score (int): CPU's best score.
        difficulty (int): Difficulty level (1: easy, 2: medium, 3: hard).
    """

    def __init__(self, user_name="User", cpu_name="CPU", user_score=0, cpu_score=0, best_score=None, cpu_best_score=None, difficulty=1):
        self.user_name = user_name
        self.cpu_name = cpu_name
        self.user_score = user_score
        self.cpu_score = cpu_score
        self.best_score = best_score if best_score is not None else float('inf')
        self.cpu_best_score = cpu_best_score if cpu_best_score is not None else float('inf')
        self.difficulty = difficulty

    def set_user_name(self):
        """
        Allows the user to set a new username.
        """
        new_name = input("Choose your new name: ")
        try:
            self.user_name = str(new_name).title()
            print("\nUsername changed successfully")
            time.sleep(1)
        except ValueError:
            print("\nUsername not changed")
            time.sleep(1)

    def set_cpu_name(self):
        """
        Allows setting a new name for the CPU.
        """
        new_name = input("Choose CPU's new name: ")
        try:
            self.cpu_name = str(new_name).title()
            print("\nCPU's name changed successfully")
            time.sleep(1)
        except ValueError:
            print("\nCPU's name not changed")
            time.sleep(1)

    def basic_guess(self):
        """
        User tries to guess CPU's number.
        Returns:
            int: Number of tries taken by the user.
        """
        limits = [10, 100, 1000]
        MIN_LIMIT = 0
        MAX_LIMIT = limits[self.difficulty - 1]

        # Game logic
        tries = 0
        memo = set()
        cpu_number = random.randint(MIN_LIMIT, MAX_LIMIT)

        while True:
            user_number = None

            while True:
                try:
                    user_number = int(input(f"Type a number between {MIN_LIMIT} and {MAX_LIMIT}: "))
                    if MIN_LIMIT <= user_number <= MAX_LIMIT:
                        break
                    else:
                        print("Number out of range. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            tries += 1

            if user_number in memo:
                print("You already chose that number. Pick a different one.")
            else:
                memo.add(user_number)

            if user_number == cpu_number:
                print("=" * 30)
                print("You win!")
                print(f"{self.user_name} score: {tries}")
                print("=" * 30)
                time.sleep(4)
                return tries
            elif user_number < cpu_number:
                print(f"{self.cpu_name} number is bigger")
            else:
                print(f"{self.cpu_name} number is smaller")

    def cpu_guess(self):
        """
        CPU tries to guess user's number.
        Returns:
            int: Number of tries taken by the CPU.
        """
        limits = [10, 100, 1000]
        MIN_LIMIT = 0
        MAX_LIMIT = limits[self.difficulty - 1]

        tries = 0
        user_number = None

        while True:
            try:
                user_number = int(input(f"Type a number between {MIN_LIMIT} and {MAX_LIMIT}: "))
                if MIN_LIMIT <= user_number <= MAX_LIMIT:
                    break
                else:
                    print("Number out of range. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        while True:
            cpu_number = random.randint(MIN_LIMIT, MAX_LIMIT)
            tries += 1
            print(f"{self.cpu_name} says {cpu_number}")
            time.sleep(1)

            if cpu_number == user_number:
                print("=" * 30)
                print(f"{self.cpu_name} Wins")
                print(f"{self.cpu_name} Score: {tries}")
                print("=" * 30)
                time.sleep(4)
                return tries
            elif cpu_number < user_number:
                MIN_LIMIT = cpu_number + 1
            else:
                MAX_LIMIT = cpu_number - 1

    def set_difficulty(self):
        """
        Allows the user to set the game difficulty.
        """
        new_difficulty = input("Select a difficulty (1: easy, 2: medium, 3: hard): ")
        try:
            new_difficulty = int(new_difficulty)
            if new_difficulty in [1, 2, 3]:
                self.difficulty = new_difficulty
        except ValueError:
            print("Not a valid difficulty")

    def run(self):
        """
        Main game loop.
        """
        while True:
            self.print_menu()
            choice = input("Select your option: ")
            if choice == '1':
                user_tries = self.basic_guess()
                if user_tries < self.best_score:
                    self.best_score = user_tries
            elif choice == '2':
                cpu_tries = self.cpu_guess()
                if cpu_tries < self.cpu_best_score:
                    self.cpu_best_score = cpu_tries
            elif choice == '3':
                user_tries = self.basic_guess()
                if user_tries < self.best_score:
                    self.best_score = user_tries
                cpu_tries = self.cpu_guess()
                if cpu_tries < self.cpu_best_score:
                    self.cpu_best_score = cpu_tries
                self.print_duel_result(user_tries, cpu_tries)
            elif choice == '4':
                self.set_user_name()
            elif choice == '5':
                self.set_cpu_name()
            elif choice == '6':
                self.set_difficulty()
            elif choice == '7':
                sys.exit("Thanks for playing. Come back again")
            else:
                print("Select a valid number. Try again")
                time.sleep(2)

    def print_menu(self):
        """
        Prints the game menu.
        """
        print("\n" + "=" * 30)
        print("+-- Guess the number game --+\n")
        print(f"Username: {self.user_name}")
        print(f"Cpu name: {self.cpu_name}")
        print(f"{self.user_name.title()} Best score: {self.best_score}")
        print(f"{self.cpu_name.title()} Best score: {self.cpu_best_score}")
        print(f"Difficulty: {self.difficulty}\n")
        print("1. User Guess the Number")
        print("2. CPU Guess the Number")
        print("3. Duel")
        print("4. Change your name")
        print("5. Change CPU's name")
        print("6. Set difficulty")
        print("7. Exit")
        print("=" * 30 + "\n")

    def print_duel_result(self, user_tries, cpu_tries):
        """
        Prints the result of the duel between user and CPU.
        Args:
            user_tries (int): Number of tries taken by the user.
            cpu_tries (int): Number of tries taken by the CPU.
        """
        print("\n" + "=" * 30)
        print("+-- Duel Result --+\n")
        if user_tries < cpu_tries:
            print(f"{self.user_name} Wins!")
        elif cpu_tries < user_tries:
            print(f"{self.cpu_name} Wins!")
        else:
            print("It's a tie!")
        print(f"{self.user_name} score: {user_tries} - {self.cpu_name} score: {cpu_tries}")
        print("=" * 30)
        time.sleep(4)

def main():
    """
    Main function to start the game.
    """
    if len(sys.argv) == 1:
        game = Game()
        game.run()
    else:
        sys.exit("Usage: filename.py with no arguments")

if __name__ == "__main__":
    main()
