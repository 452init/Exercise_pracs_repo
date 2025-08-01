def recite(start_verse, end_verse):
	result_list = []
	clean_result = []
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
	

	for i in range(start_verse, end_verse+1):
		result_list.append('This is ' + ' '.join(the_rhyme_list[-i:]))
	cleaned_result = [x.replace(',', '') for x in result_list]
	return cleaned_result
