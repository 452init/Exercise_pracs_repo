from itertools import zip_longest
def transpose(text):
    list_of_lines = text.splitlines()
    lengths = sorted(len(line) for line in list_of_lines)
    transposed_list = list(zip_longest(*list_of_lines, fillvalue=' '))
    processed_rows = []

    if len(lengths) < 2:
            strip_from = len(transposed_list)-1
    else:
        strip_from = lengths[1]
    
    for indx, row in enumerate(transposed_list):
        row_string = ''.join(row)
        if indx >= strip_from:
            row_string = row_string.rstrip()
        processed_rows.append(row_string)
    return '\n'.join(processed_rows)
