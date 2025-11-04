from itertools import groupby
def decode(string):

    decode_chars = []
    count_string = ''

    if not string:
        return string

    for char in string:
        if char.isdigit():
            count_string += char
        else:
            if count_string: 
                decode_chars.append(int(count_string)*char)
            else:
                decode_chars.append(char)
            count_string = ''
    return ''.join(decode_chars)

def encode(string):
    compressed_list = []

    for char, group in groupby(string):
        length = len(list(group))
        if length > 1:
            compressed_list.append(str(length))
        compressed_list.append(char)

    return ''.join(compressed_list)
