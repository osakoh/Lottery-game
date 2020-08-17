# This is a sample Lottery game.
# User can pick 6 numbers
# Lottery calculates 6 random numbers between 1 & 20
# Match users numbers to lottery numbers
# Calculate users winnings based on how many numbers were matched correctly


def get_player_numbers():
    input_csv = input("Enter 6 numbers separated by commas: ")
    number_list = input_csv.split(",")

    return {int(number) for number in number_list}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_player_numbers())

