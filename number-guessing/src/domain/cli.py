import random
from enum import Enum

class Difficulty(Enum):
  EASY = 10
  MEDIUM = 5
  HARD = 3

class Cli:
  def __init__(self):
    self.random_number = random.randrange(0,100,1)
    self.difficulty = 'EASY'
    self.number_of_lives = Difficulty.EASY
    self.is_playing = True

  def set_random_number(self):
    self.random_number = random.randrange(0,100,1)

  def set_difficulty(self, difficulty):
    match difficulty:
      case 'EASY':
        self.difficulty = Difficulty.EASY
      case 'MEDIUM':
        self.difficulty = Difficulty.MEDIUM
      case 'HARD':
        self.difficulty = Difficulty.HARD
      case _:
        print("Difficulty is not allowed, choose from: EASY, MEDIUM and HARD")

  def set_number_of_lives(self):
    self.number_of_lives = Difficulty(self.difficulty).value

  def lose_number_of_lives(self):
    self.number_of_lives-=1

  def exit_game(self):
    self.is_playing = False
  
  def print_welcome_message(self):
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

  def choose_difficulty(self):
    print("Please select the difficulty level:\n")
    counter = 1
    for difficulty in Difficulty:
      print(f"{counter}. {difficulty.name} ({difficulty.value} chances)")
      counter+=1
    while True:
      chosen_difficulty = input("\nEnter your choice: ")
      match chosen_difficulty:
        case '1':
          self.set_difficulty('EASY')
          break
        case '2':
          self.set_difficulty('MEDIUM')
          break
        case '3':
          self.set_difficulty('HARD')
          break
        case _:
          print("Not allowed choice. Please chose one of: 1, 2, 3")
    print("\nGreat! You have selected the Medium difficulty level.")
    print("Let's start the game!")

  def hint(self, guess_number):
    if( self.number_of_lives > 1):
      if guess_number < self.random_number:
        print(f"Incorrect! The number is greater than {guess_number}.")
      else:
        print(f"Incorrect! The number is less than {guess_number}.")
    else:
      print(f"Incorrect! The correct number was {self.random_number}.")
      

  def guess_number(self):
    attempts = 1
    while self.number_of_lives > 0:
      try:
        guess_number = int(input(f"\n(Lives: {self.number_of_lives}) Enter your guess: "))
        if guess_number == self.random_number:
          print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
          break
        else:
          self.hint(guess_number)
          self.lose_number_of_lives()
      except:
        print("You need to type a number.")
      attempts+=1

  def continue_playing(self):
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.upper() == 'YES':
      print("\nGreat let's play again!.")
    elif play_again.upper() == 'NO':
      print("\nThanks for playing. See you soon!")
      print("See you soon!")
      self.exit_game()
    else:
      print("\nI will consider that like a 'No'")
      print("Bye!")
      self.exit_game()
      
  def start(self):
    self.print_welcome_message()
    while self.is_playing:
      self.choose_difficulty()
      self.set_random_number()
      self.set_number_of_lives()
      self.guess_number()
      self.continue_playing()

if __name__ == "__main__":
  cli = Cli()
  cli.start()