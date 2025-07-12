def is_isogram(string):
    isogram_set = set(filter(str.isalpha, string.lower()))
    isogram = list(isogram_set)
    for i in string:
        if i == " " or i == "-":
            isogram += i
    return len(isogram) == len(string)
