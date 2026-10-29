#Dictionary with DNA codons mapped to full amino acid names
codon_map = {
    # T-block (U-block in RNA)
    "TTT": "Phenylalanine", "TTC": "Phenylalanine", "TTA": "Leucine", "TTG": "Leucine",
    "TCT": "Serine", "TCC": "Serine", "TCA": "Serine", "TCG": "Serine",
    "TAT": "Tyrosine", "TAC": "Tyrosine", "TAA": "Stop", "TAG": "Stop",
    "TGT": "Cysteine", "TGC": "Cysteine", "TGA": "Stop", "TGG": "Tryptophan",
    
    # C-block
    "CTT": "Leucine", "CTC": "Leucine", "CTA": "Leucine", "CTG": "Leucine",
    "CCT": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline",
    "CAT": "Histidine", "CAC": "Histidine", "CAA": "Glutamine", "CAG": "Glutamine",
    "CGT": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine",
    
    # A-block
    "ATT": "Isoleucine", "ATC": "Isoleucine", "ATA": "Isoleucine", "ATG": "Methionine",
    "ACT": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine",
    "AAT": "Asparagine", "AAC": "Asparagine", "AAA": "Lysine", "AAG": "Lysine",
    "AGT": "Serine", "AGC": "Serine", "AGA": "Arginine", "AGG": "Arginine",
    
    # G-block
    "GTT": "Valine", "GTC": "Valine", "GTA": "Valine", "GTG": "Valine",
    "GCT": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",
    "GAT": "Aspartic acid", "GAC": "Aspartic acid", "GAA": "Glutamic acid", "GAG": "Glutamic acid",
    "GGT": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine"
}


def show_full_table():
    # Helper function to print the codon lookup table.
    print("\n--- Standard Genetic Code (64 Codons) ---")
    count = 0
    for codon, amino in codon_map.items():
        print(f"{codon}: {amino:<15}", end=" | ")
        count += 1
        if count % 4 == 0:
            print()  
    print("-" * 73)