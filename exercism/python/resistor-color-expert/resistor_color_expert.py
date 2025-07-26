def resistor_label(colors):
    digit_count = 0
    base_value = 0
    total = 0
    multiplier_color = ''
    tolerance_color = ''
    string_correct_digit_band = ''
    
    digit_mapping = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

    multiplier_mapping = {'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 'yellow': 10000, 'green': 100000, 'blue': 1000000, 'violet': 10000000, 'grey': 100000000, 'white': 1000000000, 'gold': .1, 'silver': .01}

    tolerance_mapping = {'grey': '0.05%', 'violet': '0.1%', 'blue': '0.25%', 'green': '0.5%', 'brown': '1%', 'red': '2%', 'gold': '5%', 'silver': '10%'}

    if len(colors) == 1:
        return '0 ohms'
    elif len(colors) in (2, 3):
        raise TypeError('Invalid band type.')
    else:
        digit_count = 2 if len(colors) == 4 else 3
        digit_string = ''
        for i in range(digit_count):
            digit_string += str(digit_mapping[colors[i]])
        base_value = int(digit_string)
    
        multiplier_color = colors[digit_count]
        tolerance_color = colors[-1]
    
        total = base_value * multiplier_mapping[multiplier_color]

        if total >= 1_000_000:
            value = total/1_000_000
            unit = 'megaohms'
        elif total >= 1_000:
            value = total/1_000
            unit = 'kiloohms'
        else:
            value = total
            unit = 'ohms'
        if isinstance(value, float) and not value.is_integer():
            formatted_value = f"{value:.2f}".rstrip('0').rstrip('.')
        else:
            formatted_value = str(int(value))

        string_correct_digit_band = (
            formatted_value + ' ' + unit + ' ±' + tolerance_mapping[tolerance_color]
            )
    return string_correct_digit_band
