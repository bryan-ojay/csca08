"""CSCA08 Assignment 0, Fall 2017
 I hereby agree that the work contained herein is solely my work and that I
 have not received any external help from my peers, nor have I used any
 resources not directly supplied by the course in order to complete this
 assignment. I have not looked at anyone else's solution, and no one has
 looked at mine. I understand that by adding my name to this file, I am
 making a formal declaration, and any subsequent discovery of plagiarism
 or other academic misconduct could result in a charge of perjury in
 addition to other charges under the academic code of conduct of the
 University of Toronto Scarborough Campus.
 Name: Bryan Oladeji
 UtorID: oladejib
 Student Number: 1004112738
 Date: October 11, 2017
"""


def split_input(dna):
    '''(str) -> list
    Given a DNA sequence as a string, returns a list with:
    - the upstream data (every nucleotide before the first ATG sequence) of
    the gene,
    - the gene itself (everything from the first ATG sequence to the second),
    - and the downstream data of the gene (everything after the second ATG
    sequence).
    REQ: dna only contains letters in ['A', 'T', 'C', 'G']
    >>> split_input("ATCTATACTATGATCATACTGATGACATCATCA")
    ['ATCTATACT', 'ATGATCATACTG', 'ATGACATCATCA']
    >>> split_input("TACTGTGACTATCG")
    ['TACTGTGACTATCG', '', '']
    >>> split_input("ATGTACTATACATCATGTACTATCACT")
    ['', 'ATGTACTATACATC', 'ATGTACTATCACT']
    '''
    # create return variable for the upstream, the gene and downstream data
    dna_split = ['', '', '']

    # split the sequence by ATG
    gene_split = dna.split("ATG", 2)

    # create cases for 0, 1 and more than 2 ATG sequences

    # 0 ATG sequences (only upstream data)
    if dna.count("ATG") == 0:
        dna_split[0] += gene_split[0]

    # 1 ATG sequences (no downstream data)
    elif dna.count("ATG") == 1:
        dna_split[0] += gene_split[0]
        dna_split[1] += "ATG" + gene_split[1]

    # 2 or more ATG sequences
    else:
        dna_split[0] += gene_split[0]
        dna_split[1] += "ATG" + gene_split[1]
        dna_split[2] += "ATG" + gene_split[2]

    return dna_split


def get_gene(dna):
    '''(str) -> str
    Given a DNA sequence as a string, returns a string representation of a gene
    if one is present in the sequence, and returns ERROR if there is none.
    REQ: dna only contains letters in ['A', 'T', 'C', 'G']
    >>> get_gene("ACTCTAGTACTAGACTGATGATGCCGACGACAGCA")
    'ATG'
    >>> get_gene("ACTGTGATCATGCACTGATCGTACATAT")
    'ATGCACTGATCGTACATAT'
    >>> get_gene("ACTCTACTACGTACTACTACTACG")
    'ERROR'
    '''
    # use the split_gene function to separate the dna into
    # upstream, gene and downstream
    dna_sequence = split_input(dna)

    # extract the string form of the gene from the split input.
    gene = dna_sequence[1]

    # check if there is or isn't a gene in the input and return the
    # appropriate statement.
    if gene == '':
        return "ERROR"

    else:
        return gene


def validate_gene(gene):
    '''(str) -> bool
    Given a gene represented as a string, determines if it is a valid gene and
    returns the corresponding result. The gene must:
    - start with the start codon (3 character sequence) ATG
    - contain at least one codon after the start codon
    - contain only full codons (cannot end mid-way through a 3 character codon)
    - never contain four consecutive identical nucleotides.
    REQ: dna only contains letters in ['A', 'T', 'C', 'G']
    >>> validate_gene("ATGGCATAGGGA")
    True
    >>> validate_gene("CATGACTGA")
    False
    >>> validate_gene("ATG")
    False
    >>> validate_gene("ATGCATCAGT")
    False
    >>> validate_gene("ATGGGG")
    False
'''
    # create boolean for each requirement of a valid gene

    # starts with ATG (and no other ATG in gene)
    atg_check = (gene[0:3] == "ATG" and gene.count("ATG") == 1)

    # contains at least one codon after ATG
    afteratg_check = len(gene) >= 6

    # contains only full codons
    fullcodon_check = len(gene) % 3 == 0

    # never contains four consecutive indentical nucleotides
    fourinarow_check = (gene.count("AAAA") == gene.count("CCCC") ==
                        gene.count("TTTT") == gene.count("GGGG") == 0)

    valid_check = (atg_check and afteratg_check and
                   fullcodon_check and fourinarow_check)

    return valid_check


def is_palindromic(gene):
    '''(str) -> bool
    Given a gene represented as a string, determines if the gene is palindromic
    and returns the corresponding result.
    >>> is_palindromic("ATGGTA")
    True
    >>> is_palindromic("CATCTCTAC")
    True
    >>> is_palindromic("ATACTGATCATCT")
    False
    '''
    # check if the gene is the same if it is reversed
    reverse_check = gene == gene[::-1]

    return reverse_check


def evaluate_sequence(dna):
    '''(str) -> str
    Given a DNA sequence as a string, determines whether there is no gene in
    the sequence, an invalid gene, a valid gene, or a valid palindromic gene.
    REQ: dna only contains letters in ['A', 'T', 'C', 'G']
    >>> evaluate_sequence("CCCATTATC")
    'No Gene Found'
    >>> evaluate_sequence("AAAATGCTAGAATG")
    'Invalid Gene'
    >>> evaluate_sequence("CTAGGTGATGTACACATTC")
    'Valid Gene Found'
    >>> evaluate_sequence("TCAATGGTAATGCACTACAGT")
    'Valid Palindromic Gene Found'
    '''
    # Locate the gene with the get_gene function
    gene = get_gene(dna)

    # Set variables for boolean cases
    valid_check = validate_gene(gene)
    palindrome_check = is_palindromic(gene)

    # Case for "No Gene Found" (gene doesn't exist)
    if gene == "ERROR":
        result = "No Gene Found"

    # Case for "Invalid Gene" (gene exists, is invalid)
    elif (gene != "ERROR") and (not valid_check):
        result = "Invalid Gene"

    # Case for Valid Gene Found (gene exists, is valid, is not palindrome)
    elif (gene != "ERROR") and (valid_check) and (not palindrome_check):
        result = "Valid Gene Found"

    # Case for Valid Palindromic Gene Found
    # (gene exists, is valid, is palindrome)
    elif (gene != "ERROR") and (valid_check) and (palindrome_check):
        result = "Valid Palindromic Gene Found"

    return result
