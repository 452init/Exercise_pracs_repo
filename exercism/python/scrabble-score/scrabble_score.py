def score(word: str) -> int:
    letter_value_mapping = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
                            2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'],
                            4: ['F', 'H', 'V', 'W', 'Y'], 5: 'K', 8: ['J', 'X'],
                            10: ['Q', 'Z']}
    letter_count = 0

    for letter in word.upper():
        for key, value in letter_value_mapping.items():
            if letter in letter_value_mapping[key]:
                letter_count += key
    return letter_count