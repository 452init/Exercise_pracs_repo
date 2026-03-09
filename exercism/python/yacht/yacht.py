YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "same_threes_and_twos"
FOUR_OF_A_KIND = "same_four_numbers"
LITTLE_STRAIGHT = "from_1_to_5"
BIG_STRAIGHT = "from_2_to_6"
CHOICE = "any_combination"


def score(dice, category):
    if not dice:
			return 0

    first_num = dice[0]
    total = 0

    if category == YACHT:
			total = 50
    else:
			total = dice.count(category)*category
    return total
