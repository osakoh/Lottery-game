# Lottery calculates 6 random numbers between 1 & 20
# Match users numbers to lottery numbers
# Calculate users winnings based on how many numbers were matched correctly
import random


def menu():
    user_numbers = get_player_numbers()

    lottery_numbers = create_lottery_numbers()

    numbers_matched = user_numbers.intersection(lottery_numbers)
    print("You matched {}: {}\n".format(len(numbers_matched), numbers_matched))
    print("Amount won: £{}".format(100**len(numbers_matched)))  # 100^len(numbers_matched)


# get six numbers from user
def get_player_numbers():
    input_csv = input("Enter 6 numbers (between 1 & 20) separated by commas: ")
    number_list = input_csv.split(",")

    # number_set = set()
    # for number in number_list:
    #     number_set.add(int(number))
    # return number_set

    return {int(number) for number in number_list}


# generates 6 random numbers in a set between 1 & 20
def create_lottery_numbers():

    lottery_set = set()
    while len(lottery_set) != 6:
        lottery_set.add(random.randint(1, 20))

    return lottery_set


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()

