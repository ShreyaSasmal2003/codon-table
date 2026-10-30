# Dictionary with DNA codons mapped to full amino acid names.
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

def check_valid_seq(seq):
    # Check if sequence only has valid DNA.
    allowed_bases = set("ATGCU")
    for base in seq:
        if base not in allowed_bases:
            return False
    
    
    if "T" in seq and "U" in seq:
        print("Error: Sequence mixes both T (DNA) and U (RNA) bases.")
        return False
        return True
def split_into_codons(seq):
    # Slice the sequence into groups of 3 nucleotides.
    codon_list = []
    leftover = ""
    
    for i in range(0, len(seq), 3):
        chunk = seq[i:i+3]
        if len(chunk) == 3:
            codon_list.append(chunk)
        else:
            # Catch trailing bases if sequence length isn't a multiple of 3.
            leftover = chunk
            return codon_list, leftover


def translate_sequence(codon_list, is_rna=False):
    aa_chain = []
    found_starts = []
    found_stops = []
    
    stop_codons = ["TAA", "TAG", "TGA"]
    
    for c in codon_list:
        # Look up the codon in our dictionary.
        lookup_key = c.replace("U", "T") if is_rna else c
        amino_acid = codon_map.get(lookup_key, "Unknown")
        aa_chain.append(amino_acid)
        
        # Track start and stop codons
        if lookup_key == "ATG":
            found_starts.append(c)
        elif lookup_key in stop_codons:
            found_stops.append(c)
            
    return aa_chain, found_starts, found_stops


def print_results(codon_list, aa_chain, found_starts, found_stops, leftover):
    print("\n--- Translation Summary ---")
    print(f"Codons: {'-'.join(codon_list)}")
    print(f"Amino acids: {' - '.join(aa_chain)}")
    print(f"Start codon: {', '.join(found_starts) if found_starts else 'None'}")
    print(f"Stop codon: {', '.join(found_stops) if found_stops else 'None'}")
    
    if leftover:
        print(f"\nNote: Ignored incomplete codon at the end: '{leftover}'")
        print("\n--- Detailed Breakdown Table ---")
    print(f"{'Pos':<6} | {'Codon':<8} | {'Amino Acid':<18} | {'Role'}")
    print("-" * 50)
    for idx, (c, aa) in enumerate(zip(codon_list, aa_chain), start=1):
        role = "Coding"
        if c in ["ATG", "AUG"]:
            role = "Start Codon"
        elif aa == "Stop":
            role = "Stop Codon"
        print(f"{idx:<6} | {c:<8} | {aa:<18} | {role}")

# Main program execution.
if __name__ == "__main__":
   
        # Get sequence from user.
    user_seq = input("\nEnter a DNA or RNA sequence: ").strip().upper()
    if not user_seq:
        print("Please enter a valid nucleotide sequence.")
    elif not check_valid_seq(user_seq):
        print("Invalid sequence.")
    else:
        is_rna_seq = "U" in user_seq
        if is_rna_seq:
            print("Detected RNA sequence (contains Uracil).")
        else:
            print("Detected DNA sequence.")
            

# Process and display results.
        codons, extra_bases = split_into_codons(user_seq)
        if not codons:
            print(f"Sequence too short to form a 3-base codon (leftover: {extra_bases}).")
        else:
            translated_aa, starts, stops = translate_sequence(codons, is_rna=is_rna_seq)
            print_results(codons, translated_aa, starts, stops, extra_bases)

            