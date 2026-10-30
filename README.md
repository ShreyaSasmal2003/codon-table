# Python - Codon Table Pipeline

## Project Overview
In biology, genetic information is stored in DNA and RNA sequences made up of four chemical bases. During protein synthesis, cells read these sequences in groups of three bases called **codons**. Each 3-letter codon corresponds to a specific amino acid or a signal to start or stop building a protein.

This project is a Python-based command-line program (`condon.py`) that builds the complete 64-codon standard genetic code dictionary from scratch. It takes any DNA or RNA sequence entered by the user, checks if it is valid, splits it into groups of three, and translates it into a readable chain of amino acids while highlighting start and stop signals.

## Objective
Develop a Python program that generates a 64-codon lookup table and identifies the corresponding amino acid for each codon in a given DNA or RNA sequence:
- Create a dictionary containing all 64 possible codons and their full amino acid names.
- Validate the user input so only valid DNA (A, T, G, C) or RNA (A, U, G, C) nucleotides are accepted.
- Divide the sequence into codons in groups of three nucleotides and handle incomplete codons at the end cleanly.
- Identify start codons (ATG / AUG) and stop codons (TAA, TAG, TGA / UAA, UAG, UGA).
- Display both a hyphenated translation summary and a formatted breakdown table.

## Tools & Technologies
- **Programming Language:** Python 3.x (Dictionaries, Lists, Sets, Loops, String Manipulation, Conditional Statements)
- **Code Editor:** Visual Studio Code (VS Code)
- **Version Control:** Git & GitHub

## Methodology
The program is divided into five main steps inside `condon.py`:

1. **Creating the Codon Dictionary (`codon_map`):** Stores all 64 DNA triplets as keys and their full amino acid names as values (e.g., `"ATG": "Methionine"`, `"TAA": "Stop"`).
2. **Input & Validation (`check_valid_seq`):** Converts user input to uppercase, removes extra spaces, and checks that every character is a valid DNA or RNA base. It also prevents mixing DNA (`T`) and RNA (`U`) in the same sequence.
3. **Splitting into Triplets (`split_into_codons`):** Slices the sequence into 3-letter chunks using a loop (`range(0, len(seq), 3)`). If the sequence length is not divisible by 3, any trailing 1 or 2 letters are caught separately as leftover bases.
4. **Translation & Signal Detection (`translate_sequence`):** Matches each 3-letter codon against `codon_map` (converting `U` to `T` dynamically if the input is RNA) and records start and stop codons.
5. **Displaying the Output (`print_results` & `show_full_table`):** Prints the optional 64-codon reference grid, the hyphenated summary lines, and a formatted breakdown table.

### Comparison with Online GitHub Codon Table Repositories
- **Full Names vs. 1-Letter Codes:** Standard bioinformatics repositories on GitHub (like Biopython) map codons to 1-letter symbols (`"ATG": "M"`, `"TAA": "*"`) for memory efficiency. Our project maps codons to full amino acid names (`"Methionine"`, `"Stop"`) so the output is clear and easy for students to read.
- **Unified DNA/RNA Handling:** Many beginner repositories duplicate the 64-item dictionary twice (one for DNA and one for RNA). Our program uses a single 64-codon dictionary and handles RNA sequences dynamically without repeating code.

## Sample Input and Expected Output

**Sample Input:**

Do you want to view the full 64-codon table first? (y/n): n
Enter a DNA or RNA sequence: ATGGCTTTTTAA


**Expected Output:**

Detected DNA sequence.

--- Translation Summary ---
Codons: ATG-GCT-TTT-TAA
Amino acids: Methionine - Alanine - Phenylalanine - Stop
Start codon: ATG
Stop codon: TAA

--- Detailed Breakdown Table ---
Pos    | Codon    | Amino Acid         | Role
--------------------------------------------------
1      | ATG      | Methionine         | Start Codon


## Applications and Limitations

**Applications:**
- **Educational Tool:** Helps students easily visualize how DNA and RNA sequences translate into amino acid chains.
- **Quick Sequence Verification:** Useful for checking small gene sequences, finding start and stop signals, and spotting incomplete codons during lab exercises.

**Limitations:**
- **Single Reading Frame:** Reads the sequence starting only from the first nucleotide (Frame +1) rather than scanning all 6 reading frames.
- **Translates Past Stop Codons:** Translates all triplets in the input string for demonstration rather than halting translation immediately at the first stop codon.
- **Manual Terminal Input:** Requires typing or pasting sequences into the terminal instead of reading directly from `.fasta` genome files.

## Future Improvements
- **FASTA File Support:** Add file-reading support so users can load long DNA/RNA sequences from `.fasta` or `.txt` files.
- **Open Reading Frame (ORF) Finder:** Automatically scan a long sequence, begin translation only when a start codon (`ATG`/`AUG`) is found, and stop when a stop codon is reached.
- **6-Frame Translation:** Generate the reverse complement of the DNA sequence and translate all three forward and three reverse reading frames.
- **Graphical User Interface (GUI):** Create a simple web or desktop app using Streamlit or Tkinter with color-coded codons and amino acid properties.
