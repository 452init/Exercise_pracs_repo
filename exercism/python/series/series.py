def slices(series, length):
    if length == 0:
        raise ValueError('slice length cannot be zero')
    if length < 0:
        raise ValueError('slice length cannot be negative')
    if series == '':
        raise ValueError('series cannot be empty')
    if length > len(series):
        raise ValueError('slice length cannot be greater than series length')

    result = slice_generator(series, length)

    return [const for const in result]

def slice_generator(string, str_len):
    for const in range(len(string) - str_len+1):
        yield string[const:const+str_len]


#   return [series[cont:cont+length] for cont in range(len(series) - length+1)]
