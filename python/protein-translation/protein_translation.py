from itertools import takewhile
def proteins(strand):
	RNA_SEQUENCE = {
			'AUG': 'Methionine',
			'UGG': 'Tryptophan',
			'UUU': 'Phenylalanine',
			'UUC': 'Phenylalanine',
			'UUA': 'Leucine',
			'UUG': 'Leucine',
			'UCU': 'Serine',
			'UCA': 'Serine',
			'UCC': 'Serine',
			'UCG': 'Serine',
			'UAU': 'Tyrosine',
			'UAC': 'Tyrosine',
			'UGC': 'Cysteine',
			'UGU': 'Cysteine'
			}

	stop_codons = {'UAA', 'UAG', 'UGA'}
	protein_names = []

	codon = [strand[x:x+3] for x in range(0, len(strand), 3)]

	valid_codons = takewhile(
			lambda codon: codon not in stop_codons and codon in RNA_SEQUENCE,
			codon
			)
	protein_names = [RNA_SEQUENCE[codon] for codon in valid_codons]
	return protein_names
