from collections import Counter

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

    counts = Counter(dice)
    max_val = max(counts, key=counts.get)
    frequencies = sorted(counts.values())
    total = 0

    if category == YACHT and frequencies == [5]:
        total = 50
    elif category == FULL_HOUSE and frequencies == [2, 3]:
        total = sum(dice)
    elif category == FOUR_OF_A_KIND and max(counts.values()) >= 4:
        total = max_val*4
    elif category == LITTLE_STRAIGHT and sorted(dice) == [1,2,3,4,5]:
        total = 30
    elif category == BIG_STRAIGHT and sorted(dice) == [2,3,4,5,6]:
        total = 30
    elif category == CHOICE:
        total = sum(dice)
    else:
        if category in set([ONES, TWOS, THREES, FOURS, FIVES, SIXES]):
            total = dice.count(category)*category
    return total
