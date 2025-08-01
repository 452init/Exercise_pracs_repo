#!/usr/bin/env python3
result_list = []
the_rhyme_list = [
	'the horse and the hound and the horn that belonged to',
	'the farmer sowing his corn that kept',
	'the rooster that crowed in the morn that woke',
	'the priest all shaven and shorn that married',
	'the man all tattered and torn that kissed',
	'the maiden all forlorn that milked',
	'the cow with the crumpled horn that tossed',
	'the dog that worried',
	'the cat that killed',
	'the rat that ate',
	'the malt that lay in',
	'the house that Jack built.'
]

#result_list.append(the_rhyme_list[0])
num = input(" ")
for i in range(1, 1+1):
	result_list.append("This is " + ' '.join(the_rhyme_list[-i:]))
	cleaned_result_list = [j.replace(',', '') for j in result_list]
print (cleaned_result_list)
