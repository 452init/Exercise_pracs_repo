import re

def count_words(sentence: str)->dict:
    partially_cleaned_sentence = re.sub(r"[^a-z0-9'_,\n\t ]+", "", sentence.lower())
    semi_cleaned = re.sub(r"[,_\n]+", ' ', partially_cleaned_sentence)
    quotes_before_word_removed = re.sub(r"(?<![a-z0-9])'+(?=[a-z0-9])", "", semi_cleaned)
    quotes_after_word_removed = re.sub(r"(?<=[a-z0-9])'+(?![a-z0-9])", "", quotes_before_word_removed)
    list_sentence = quotes_after_word_removed.split()
    mapped_words = {}
    for word in list_sentence:
        if word in mapped_words:
            mapped_words[word] += 1
        else:
            mapped_words[word] = 1
    return mapped_words