from itertools import zip_longest

def transpose(text):
    list_of_lines = text.splitlines()

    transposed_tuples = list(zip_longest(*list_of_lines, fillvalue=' '))

    processed_rows = []
    for indx, row in enumerate(transposed_tuples):
        row_string = ''.join(row)
        
        if indx == len(transposed_tuples)-1:
            row_string = row_string.rstrip()
        processed_rows.append(row_string)
    return '\n'.join(processed_rows)
