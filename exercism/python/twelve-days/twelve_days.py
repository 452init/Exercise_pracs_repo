from typing import final

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
        gift_list_rev = [_ for _ in build_one_verse(verse)]
        final_gift_list = gift_list_rev[-1]
        if len(gift_list_rev) > 1:
            modified_gift: str = 'and ' + final_gift_list[-1]
            final_gift_list[-1] = modified_gift
        final_result.append(f"On the {day_names[verse - 1]} day of Christmas my true love gave to me: {', '.join(final_gift_list)}.")
    return final_result

def build_one_verse(verse_num: int):

    for gift in range(verse_num+1):
        if gift > 0:
            yield gift_descriptions[:gift][::-1]