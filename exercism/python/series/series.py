def slices(series, length):
    if length == 0:
        raise ValueError('slice length cannot be zero')
    if length < 0:
        raise ValueError('slice length cannot be negative')
    if series == '':
        raise ValueError('series cannot be empty')
    if length > len(series):
        raise ValueError('slice length cannot be greater than series length')

    contiguous_substrings = [series[cont:cont+length] for cont in range(len(series) - length+1)]
    return contiguous_substrings
