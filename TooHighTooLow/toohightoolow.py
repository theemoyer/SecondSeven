# a simple high low number guessing game.
#
import random
class too_high_too_low:
    
    

    def __init__(self):
        # setup self.number to be a random number from 1 to 100
        self.number = random.randint(1, 101)
        # self.guesses to be zero
        self.guesses = 0
        pass

    def play(self):
        while True:
            pass
            # Get a number guess from the user (between 1 and 100)
            guess = int(input("Guess a number between 1 and 100: "))
            # Convert the input to an integer
            guess = int(guess)
            # Increment the number of guesses by 1
            self.guesses += 1
            # Check *if* the guess equals the secret number
            # If correct, print a congratulations message with the number of guesses
            # Exit the loop
            # Check *if* the guess is less than the secret number
            # If so, print "Too low!"
            # Otherwise (the guess must be too high)
            # Print "Too high!"
            if guess < self.number:
                print("Too low!")
            elif guess > self.number:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number in {self.guesses} guesses!")
                break
            # Check *if* the player has made 10 guesses
            # If so, print a message saying they've run out of guesses and reveal the number
            # Exit the loop
            if self.guesses >= 10:
                print(f"Game over! You've run out of guesses. The number was {self.number}.")
                break
            if self.guesses == 5:
                print("Hint: The number is " + ("even." if self.number % 2 == 0 else "odd."))
            if self.guesses == 8:
                print("Hint: The number is " + ("greater than 50." if self.number > 50 else "less than or equal to 50."))
            if self.guesses == 3:
                print("Hint: The number is " + ("a multiple of 5." if self.number % 5 == 0 else "not a multiple of 5."))

            if self.guesses == 1:
                previous_guess = guess
            elif guess == previous_guess:
                print("You've already guessed that number! Try a different one.")
                self.guesses -= 1  # Decrement guesses to account for the invalid guess
            else:
                previous_guess = guess 
                

def main():
    game = too_high_too_low()
    game.play()


if __name__ == "__main__":
    main()
