def find_anagrams(word, candidates):
	word_case = word.lower()
	sorted_word_case = sorted(word_case)
	final_anagram_list = []

	for i in candidates:
		comparison_case = i.lower()
		if len(i) != len(word) or word_case == comparison_case:
			continue
		else:
			sorted_comparison_case = sorted(comparison_case)
			if sorted_comparison_case == sorted_word_case:
				final_anagram_list.append(i)
	return final_anagram_list
