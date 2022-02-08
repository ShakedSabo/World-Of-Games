def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play."


def load_game():
    game = input(
        """please choose a game to play:
        1- Memory Game- a sequence of numbers will appear for 1 second and you have to ges it back
        2- Guess Game- guess a number and see if you chose like the computer
        3-Currency Roulette- try and guess the value of a random amount of USD in ILS
         Enter the number here: """)
    while not game.isdigit() or int(game) > 3 or int(game) < 1:
        print("please choose a number between 1-3: ")
        game = input()
    difficulty = input("please choose game difficulty from 1 to 5: ")
    while not difficulty.isdigit() or int(difficulty) > 5 or int(difficulty) < 1:
        print("please choose a number between 1-5")
        difficulty = input(difficulty)
    if int(game) == 1:
        print("You chose Memory Game")
        print(f"your game difficulty is {difficulty}")
        from project.MemoryGame import play
        play(difficulty)
    elif int(game) == 2:
        print("You chose Guess Game")
        print(f"your game difficulty is {difficulty}")
        from project.GuessGame import play
        play(difficulty)
    else:
        print("You chose Currency Roulette")
        print(f"your game difficulty is {difficulty}")
        from project.CurrencyRouletteGame import play
        play(difficulty)




def main():
    print(welcome("Shaked"))
    load_game()


if __name__ == "__main__":
    main()
