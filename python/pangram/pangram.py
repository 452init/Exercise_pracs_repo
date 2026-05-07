def is_pangram(sentence):
    unique_values = "".join(filter(str.isalpha, sentence))
    no_duplicates = set(unique_values.lower())
    return len(no_duplicates) >= 26
