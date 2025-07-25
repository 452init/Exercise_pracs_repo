def resistor_label(colors):
    string_digit_band = ''
    num_digit_band = 0
    multiplied_digit_band = 0
    correct_digit_band = 0
    string_correct_digit_band = ''
    
    digit_mapping = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

    multiplier_mapping = {'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 'yellow': 10000, 'green': 100000, 'blue': 1000000, 'violet': 10000000, 'grey': 100000000, 'white': 1000000000, 'gold': .1, 'silver': .01}

    tolerance_mapping = {'grey': '0.05%', 'violet': '0.1%', 'blue': '0.25%', 'green': '0.5%', 'brown': '1%', 'red': '2%', 'gold': '5%', 'silver': '10%'}

    if len(colors) == 1:
        return '0 ohms'
    elif len(colors) == 2 or len(colors) == 3:
        raise TypeError ('Invalid band type.')
    elif len(colors) == 4:
        formatted_value = ''
        string_digit_band += str(digit_mapping.get(colors[0]))
        string_digit_band += str(digit_mapping.get(colors[1]))
        num_digit_band = int(string_digit_band)
        multiplied_digit_band = num_digit_band * (multiplier_mapping.get(colors[2]))
        if multiplied_digit_band >= 1000000:
            correct_digit_band = multiplied_digit_band//1000000
            string_correct_digit_band = (str(correct_digit_band) + ' megaohms' + ' ±')
            string_correct_digit_band += tolerance_mapping.get(colors[3])
        elif multiplied_digit_band >= 1000:
            correct_digit_band = multiplied_digit_band/1000
            if correct_digit_band % 1 == 0:
                formatted_value = str(int(correct_digit_band))
            else:
                formatted_value = f"{correct_digit_band:.1f}"
            string_correct_digit_band = (str(formatted_value) + ' kiloohms' + ' ±')
            string_correct_digit_band += tolerance_mapping.get(colors[3])
        else:
            string_correct_digit_band = (str(multiplied_digit_band) + ' ohms' + ' ±')
            string_correct_digit_band += tolerance_mapping.get(colors[3])
    elif len(colors) == 5:
        string_digit_band += str(digit_mapping.get(colors[0]))
        string_digit_band += str(digit_mapping.get(colors[1]))
        string_digit_band += str(digit_mapping.get(colors[2]))
        num_digit_band = int(string_digit_band)
        multiplied_digit_band = num_digit_band * (multiplier_mapping.get(colors[3]))
        if multiplied_digit_band >= 1000000:
            correct_digit_band = multiplied_digit_band/1000000
            string_correct_digit_band = (str(correct_digit_band) + ' megaohms' + ' ±')
            string_correct_digit_band += tolerance_mapping.get(colors[4])
        elif multiplied_digit_band >= 1000:
            correct_digit_band = multiplied_digit_band/1000
            string_correct_digit_band = (str(correct_digit_band) + ' kiloohms' + ' ±')
            string_correct_digit_band += tolerance_mapping.get(colors[4])
        else:
            string_correct_digit_band = (str(multiplied_digit_band) + ' ohms' + ' ±')
            string_correct_digit_band += tolerance_mapping.get(colors[4])
    return string_correct_digit_band
