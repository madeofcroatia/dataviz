def is_valid_sequence(seq):
    """Ensure valid sequence of amino acids."""
    for aa in seq:
        if aa not in "ARNDCQEGHILKMFPSTWYV":
            raise RuntimeError(aa + ' is not a valid amino acid.')

def number_negatives(seq):
    """Number of negative residues a protein sequence"""
    # Convert sequence to upper case
    seq = seq.upper()
    # Check for valid sequence
    is_valid_sequence(seq)

    # Count E's and D's, since these are the negative residues
    return seq.count('E') + seq.count('D')


def number_positives(seq):
    """Number of positive residues in a protein sequence"""
    seq = seq.upper()
    
    is_valid_sequence(seq)
    
    return seq.count('R') + seq.count('K') + seq.count('H')
