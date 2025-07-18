def to_rna(dna_strand):
	rna_strand = ''
	for i in dna_strand:
		if i == 'G':
			rna_strand += 'C'
		elif i == 'C':
			rna_strand += 'G'
		elif i == 'T':
			rna_strand += 'A'
		elif i == 'A':
			rna_strand += 'U'
		else:
		 	return rna_strand
	return rna_strand
