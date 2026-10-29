#Dictionary with DNA codons mapped to full amino acid names.
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


def check_valid_seq(seq):
    # Check if sequence only has valid DNA letters.
    allowed_bases = set("ATGC")
    for base in seq:
        if base not in allowed_bases:
            return False
    return True


def split_into_codons(seq):
    # Slice the sequence into groups of 3 nucleotides
    codon_list = []
    leftover = ""
    
    for i in range(0, len(seq), 3):
        chunk = seq[i:i+3]
        if len(chunk) == 3:
            codon_list.append(chunk)
        else:
            # Catch trailing bases if sequence length isn't a multiple of 3
            leftover = chunk
            
    return codon_list, leftover


# Main program execution
if __name__ == "__main__":
    ask_table = input("Do you want to view the full 64-codon table first? (y/n): ").strip().lower()
    if ask_table == 'y':
        show_full_table()
        
    # Get sequence from user.
    user_seq = input("\nEnter a DNA sequence: ").strip().upper()
    
    if not user_seq:
        print("Empty input! Please enter a valid nucleotide sequence.")
    elif not check_valid_seq(user_seq):
        print("Invalid sequence! Please use only A, T, G, and C.")
    else:
        codons, extra_bases = split_into_codons(user_seq)
        print("Split codons:", codons)
        if extra_bases:
            print(f"Incomplete codon ignored at end: {extra_bases}")