def is_pangram(sentence):
    unique_values = "".join(filter(str.isalpha, sentence))
    no_duplicates = set(unique_values.lower())
    if len(no_duplicates) >= 26:
        return True
    else:
        return False
