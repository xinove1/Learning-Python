def DNA_strand(dna):
    dna_pairs = [
        'T': 'A'
        'A': 'T'
        'C': 'G'
        'G': 'C'    ]
    dna.translate(dna_pairs)
    return(dna)

DNA_strand('ATTGC')   