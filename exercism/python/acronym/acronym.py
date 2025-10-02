def abbreviate(words):
    cleaned = words.replace('-', ' ').replace('_', ' ')
    word_list = cleaned.split()
    acronyms = [acro[0] for acro in word_list]
    return ''.join(acronyms).upper()