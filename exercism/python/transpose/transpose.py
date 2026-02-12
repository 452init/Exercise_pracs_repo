from itertools import zip_longest
def transpose(text):
    list_of_lines = text.splitlines()
    lengths = sorted(len(line) for line in list_of_lines)
    transposed_tuples = list(zip_longest(*list_of_lines, fillvalue=' '))
    processed_rows = []
    for indx, row in enumerate(transposed_tuples):
        row_string = ''.join(row)
        if len(lengths) < 2:
            strip_from = 0
        strip_from = lengths[1]
        processed_rows.append(strip_from)
    return '\n'.join(processed_rows)
