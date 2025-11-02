def decode(string):
    my_list = []
    char_str = ''
    next_char = ''
    prev_char = ''
    two_ahead = ''
    processed = set()

    if string == '':
        return string

    for pos, char in enumerate(string):
        if pos in processed:
            continue
        if pos + 1 < len(string):
            next_char = string[pos+1]
        if pos > 0:
            prev_char = string[pos-1]
        if pos + 2 < len(string):
            two_ahead = string[pos+2]

        if char.isdigit() and not next_char.isdigit():
            my_list.append(int(char)*next_char)
            processed.add(pos)
            processed.add(pos + 1)
        elif char.isdigit() and next_char.isdigit():
            char_str = char + next_char
            my_list.append(int(char_str)*two_ahead)
            processed.add(pos)
            processed.add(pos+1)
            processed.add(pos+2)
        elif not char.isdigit() and not prev_char.isdigit():
            my_list.append(char)
            processed.add(pos)
    return ''.join(my_list)

def encode(string):
    compressed_list = []
    counter = 0

    if string == '':
        return string

    prev_char = string[0]

    for value in range(len(string)):
        if string[value] == prev_char:
            counter += 1
        elif string[value] != prev_char:
            if counter > 1:
                compressed_list.append(str(counter))
                counter = 1
            compressed_list.append(prev_char)
        prev_char = string[value]
    if counter > 1:
        compressed_list.append(str(counter))
    compressed_list.append(prev_char)

    return ''.join(compressed_list)
