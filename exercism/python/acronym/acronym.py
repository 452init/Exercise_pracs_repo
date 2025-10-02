# using the extend method '+=' which is much slower
def abbreviate(words):
    acronym = ''
    lowercase = words.replace("'", "").lower()
    titlecase = lowercase.title()
    for acro in titlecase:
        if acro.isupper():
            acronym += acro
    return acronym

#using list comprehension
def abbreviate(words):
    acronym_list = []
    lowercase = words.replace("'", "").lower()
    titlecase = lowercase.title()
    acronym_list = [acro for acro in titlecase if acro.isupper()]
    return ''.join(acronym_list)


#using replace and list comprehension
def abbreviate(words):
    cleaned = words.replace('-', ' ').replace('_', ' ')
    word_list = cleaned.split()
    acronyms = [acro[0] for acro in word_list]
    return ''.join(acronyms).upper()
