import os
import random
import time


def generate_sequence(difficulty):
    random_numbers = [random.randint(1, 101) for _ in range(int(difficulty))]
    print(random_numbers)
    time.sleep(0.7)
    return random_numbers


def get_list_from_user(difficulty):
    user_input = []
    user_input = [int(i) for i in user_input]
    print(f"Enter the {difficulty} numbers you remember: ")
    for i in range(0, int(difficulty)):
        ele = int(input())
        user_input.append(ele)
    return user_input


def is_list_equal(user_input, random_numbers):
    random_numbers.sort()
    user_input.sort()
    if random_numbers == user_input:
        return True
    else:
        return False


def play(difficulty):
    user_input = generate_sequence(difficulty)
    print("\n" * 20)
    random_numbers = get_list_from_user(difficulty)

    if is_list_equal(user_input=user_input, random_numbers=random_numbers):
        print(True)
    else:
        print(False)



