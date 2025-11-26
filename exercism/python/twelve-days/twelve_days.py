day_names = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
                 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
gift_descriptions = ['a Partridge in a Pear Tree', 'two Turtle Doves',
                         'three French Hens', 'four Calling Birds', 'five Gold Rings',
                         'six Geese-a-Laying', 'seven Swans-a-Swimming',
                         'eight Maids-a-Milking', 'nine Ladies Dancing',
                         'ten Lords-a-Leaping', 'eleven Pipers Piping',
                         'twelve Drummers Drumming']

def recite(start_verse, end_verse):
    final_result = []

    for verse in range(start_verse, end_verse+1):
        gift_list_rev = build_one_verse(verse)
        if len(gift_list_rev) > 1:
            modified_gift: str = 'and ' + gift_list_rev[-1]
            gift_list_rev[-1] = modified_gift
        final_result.append(f"On the {day_names[verse - 1]} day of Christmas my true love gave to me: {', '.join(gift_list_rev)}.")
    return final_result

def build_one_verse(verse_num: int) -> list:
    return gift_descriptions[:verse_num][::-1]