def recite(start_verse, end_verse):
    final_result = []
    day_names = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
                 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    gift_descriptions = ['a Partridge in a Pear Tree', 'two Turtle Doves',
                         'three French Hens', 'four Calling Birds', 'five Gold Rings',
                         'six Geese-a-Laying', 'seven Swans-a-Swimming',
                         'eight Maids-a-Milking', 'nine Ladies Dancing',
                         'ten Lords-a-Leaping', 'eleven Pipers Piping',
                         'twelve Drummers Drumming']

    for verse_num in range(start_verse, end_verse+1):
        gift_list = []
        for gift_pos in range(verse_num):
            gift_list = [gift_descriptions[gift_pos]] + gift_list
        if verse_num > 1:
            modified_gift: str = 'and ' + gift_list[-1]
            gift_list[-1] = modified_gift

        final_result.append(f"On the {day_names[verse_num-1]} day of Christmas my true love gave to me: {', '.join(gift_list)}.")
    return final_result