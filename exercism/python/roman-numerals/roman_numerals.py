def roman(number: int)-> str:
    roman_mapping = {1000: 'M',	900: 'CM', 500: 'D', 400: 'CD',
                     100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                     10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    roman_result: str = ''

    for num in roman_mapping:
        quotient, number = divmod(number, num)
        roman_result += roman_mapping[num] * quotient
    return roman_result