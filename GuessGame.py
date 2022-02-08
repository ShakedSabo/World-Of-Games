def generate_number(difficulty):
    import random
    random_number = random.randint(1, int(difficulty))
    return random_number


def get_guess_from_user(difficulty):
    guess = input(f"please choose a number between 1 to {difficulty}")
    return guess


def compare_results(random_number, guess):
    if int(random_number) == int(guess):
        return True
    else:
        return False


def play(difficulty):
    random_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    if compare_results(guess=guess, random_number=random_number):
        print(True)
    else:
        print(False)
