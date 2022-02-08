def get_money_interval(difficulty):
    import random
    from currency_converter import CurrencyConverter

    c = CurrencyConverter()
    Currency = c.convert(1, 'USD', 'ILS')
    random_number = random.randint(1, 100)
    t = Currency * random_number
    interval = range(int(t) - (5 - int(difficulty)), int(t) + (5 - int(difficulty)))
    print(f" the number is: {random_number}")
    return interval


def get_guess_from_user(difficulty):
    guess = int(input(f"Please enter your guess of how much it is in ILS:  "))
    return guess


def test(interval, guess):
    if guess in interval:
        return True
    else:
        return False


def play(difficulty):
    interval = get_money_interval(difficulty)
    guess = get_guess_from_user(difficulty)
    if test(interval=interval, guess=guess):
        print(True)
    else:
        print(False)


