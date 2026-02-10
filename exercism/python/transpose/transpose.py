from itertools import zip_longest

def transpose(text):
    list_of_lines = text.splitlines()

    transposed_tuples = list(zip_longest(*list_of_lines, fillvalue=''))

    transposed = '\n'.join(''.join(row) if len(row)>1 else row for row in transposed_tuples)
    return transposed
