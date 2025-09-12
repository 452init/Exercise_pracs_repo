def proteins(strand):
	rna_sequence = {
			'Methionine': 'AUG',
			'Tryptophan': 'UGG',
			'Phenylalanine': ('UUU', 'UUC'),
			'Leucine': ('UUA', 'UUG'),
			'Serine': ('UCU', 'UCC', 'UCA', 'UCG'),
			'STOP': ('UAA', 'UAG', 'UGA'),
			'Tyrosine': ('UAU', 'UAC'),
			'Cysteine': ('UGC', 'UGU')
			}

	codons = []
	protein_names = []

	if len(strand) < 3:
		raise TypeError('Invalid DNA strand')
	else:
		for x in range(0, len(strand), 3):
			codons.append(strand[x:x+3])
			for i in codons:
				if i in rna_sequence['STOP']:
					break
				for key, value in rna_sequence.items():
					if i in value:
						protein_names.append(key)
				codons.clear()
		return protein_names
