def line_up(name, number):
    mapping = {'1': 'st', '2': 'nd', '3': 'rd'}
    if number<=3 or number<=10 and str(number)[-2] != '1':
        suffix = mapping.get(str(number)[-1], 'th')
    return f'{name}, you are the {number}{suffix} customer we serve today. Thank you!'
