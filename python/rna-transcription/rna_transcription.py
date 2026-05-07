def to_rna(dna_strand):
	rna_strand = str.maketrans('GCTA', 'CGAU')
	return dna_strand.translate(rna_strand)
