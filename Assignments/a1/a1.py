"""CSCA08 Assignment 1, Fall 2017
 I hereby agree that the work contained herein is solely my work and that I
 have not received any external help from my peers, nor have I used any
 resources not directly supplied by the course in order to complete this
 assignment. I have not looked at anyone else's solution, and no one has
 looked at mine. I understand that by adding my name to this file, I am
 making a formal declaration, and any subsequent discovery of plagiarism
 or other academic misconduct could result in a charge of perjury in
 addition to other charges under the academic code of conduct of the
 University of Toronto Scarborough Campus
 Name: Bryan Oladeji
 UtorID: oladejib
 Student Number: 1004112738
 Date: November 2, 2017
"""

# Create a global variable for the nucleotides that pair with each other
# Even-index nucleotides will pair to the odd-indexed nucleotide on the right
# Odd-index nucleotides will pair to the even-indexed nucleotide on the left
NUCLEOS = ['A', 'T', 'C', 'G']

# Create variables to signify the start and end of a multi
# Brackets could be changed to another type, i.e. multis could be {ATG}.
MULTI_START = '['
MULTI_END = ']'

# Create a list of numbers (used for to check for numbers in a mask)
NUM_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# pair_genes and zip_length helper function
def gene_swap(gene):
    '''(str or list) -> str or list
    Helper function used for pair_genes, zip_length and match_mask functions:
    Takes in a gene, returns a gene containing the nucleotides that pair
    with each corresponding nucleotide in the given gene.
    REQ: all elements of gene are in NUCLEOS, NUM_LIST or in ['[', ']', '*'}
    >>> gene_swap("TCAG")
    'AGTC'
    >>> gene_swap("ACTGGATG")
    'TGACCTAC'
    >>> gene_swap("CAATGGATG")
    'GTTACCTAC'
    '''
    # create empty string for new gene
    new_gene = ""

    # run through all the elements in the inputted gene
    for nucleotide in gene:

        # check if the element is a valid nucleotide
        if nucleotide in NUCLEOS:
            nucleo_index = NUCLEOS.index(nucleotide)

            # pairs for even-indexed nucleotides will pair to the next index
            if nucleo_index % 2 == 0:
                new_gene += NUCLEOS[nucleo_index + 1]

            # pairs for odd-indexed nucleotides will pair to the previous index
            elif nucleo_index % 2 == 1:
                    new_gene += NUCLEOS[nucleo_index - 1]

        # if the element is not a valid nucleotide, add to the new gene as is
        else:
            new_gene += nucleotide

    return new_gene


def pair_genes(gene1, gene2):
    '''(str, str) -> bool
    Takes in two strings representing genes, and determines if every
    nucleotide between the two genes pair with each other.
    (Adenine pairs with Thymine, Guanine pairs with Cytosine, and vice versa).
    REQ: gene1 and gene2 only contain elements in NUCLEOS
    >>> pair_genes("TCAG", "AGTC")
    True
    >>> pair_genes("CCTAGTA","TACCAGG")
    False
    '''
    # create an gene string containing the pairs of gene1's nucleotides
    gene_copy = gene_swap(gene1)

    # check if the the pair of gene1 equals gene2 or
    # the reverse of gene2
    # (genes can be read in either direction)
    equal_check = (gene_copy == gene2 or gene_copy == gene2[::-1])

    return equal_check


def zip_length(gene):
    '''(str) -> int
    Takes in a string representing a gene, and returns the maximum number of
    nucleotide pairs that this gene can zip.
    REQ: all elements of gene are in NUCLEOS
    >>> zip_length("AGTCTCGCT")
    2
    >>> zip_length("AGTCGACT")
    4
    >>> zip_length("AGTCTCGCC")
    0
    '''
    # create variable for number of pairs within the gene
    pairs = 0

    # create a gene string containing the pairs of the gene's nucleotides
    pair_gene = gene_swap(gene)

    # create variable for the last character in the gene
    gene_end = len(gene) - 1

    # scan the gene up until the middle of the gene
    index = 0
    gene_scan_limit = (len(gene)//2)
    while index < gene_scan_limit:

        # check if the nucleotides in the start of the given gene
        # match the nucleotides at the end of compare_gene
        equal_check = gene[index] == pair_gene[gene_end - index]

        # if one of these requirements are met, this counts as another pair
        if equal_check:
            pairs += 1

        # if not, the gene cannot be zipped anymore
        else:
            # scan limit is set to index so the while loop can be stopped
            gene_scan_limit = index

        index += 1

    return pairs


# splice_gene helper function
def find_anchors(gene, start, end, reverse):
    '''(list, str, str, bool) -> [int, int]
    Helper function used for splice_gene function:
    Takes in a list representation of a gene, strings representing
    start and end anchor strings, and a boolean choosing whether to check the
    list in reverse.
    Returns a list of two integers:
    - The first integer is the index of the beginning of the first
      start anchor string found in the list. If no start anchor is found, -1 is
      returned.
    - The second integer is the index of the end of the first end anchor
      string found after the first anchor string in the list. If no end anchor
      is found, -1 is returned.
    REQ: len(start) < len(gene)
    REQ: len(end) < len(gene)
    >>> find_anchors(['T', 'G', 'C', 'T', 'A', 'G', 'T'], "AT", "GT", True)
    [0, 4]
    >>> find_anchors(['T', 'G', 'T', 'G', 'G', 'G'], "GT", "GG", False)
    [1, 4]
    >>> find_anchors(['C', 'C', 'A', 'G', 'T', 'A'], "TA", "CC", False)
    [4, -1]
    '''
    # create variables for the indices of the found anchor strings in the gene
    # default to -1 because they have not been found yet
    start_in_gene = -1
    end_in_gene = -1

    # convert the start and end anchors to lists
    start_anchor = list(start)
    end_anchor = list(end)

    # if the list is reversed, switch the start and anchor string
    # (instead of reading from right to left, we will look for the
    # reversed end anchor string first, followed by the reversed
    # start anchor string)
    if (reverse):
        (start_anchor, end_anchor) = (end_anchor[::-1], start_anchor[::-1])

    # run through the gene from the beginning of the gene up to where
    # the end point of the start_anchor meets the end of the gene
    start_anchor_limit = len(gene) - (len(start_anchor) - 1)

    # run through the gene forwards
    start_index = 0
    while start_index < start_anchor_limit:

        # the anchor will span its length from the current index
        anchor_range = start_index + len(start_anchor)

        # find the first index in the gene that matches the start anchor
        if (start_anchor == gene[start_index:anchor_range]):

            # set the start_in_gene index to the found start anchor
            start_in_gene = start_index

            # set the anchor limit to the current index to
            # stop the while loop after the current cycle finishes
            start_anchor_limit = start_index

            # find end anchor

            # anchor check runs from the start of the gene up to where
            # the endpoint of the anchor meets the end of gene
            end_anchor_limit = len(gene) - (len(end_anchor) - 1)

            # run through the gene starting from the element after
            # the endpoint of the start anchor
            end_index = anchor_range
            while end_index < end_anchor_limit:

                # set the range the end anchor will cover from this index
                anchor_range = end_index + len(end_anchor)

                # find the first end index that matches
                if (end_anchor == gene[end_index:anchor_range]):

                    # set the end_in_gene index to the found end anchor
                    end_in_gene = anchor_range - 1

                    # set the anchor limit to the current index to
                    # stop the while loop after the current cycle finishes
                    end_anchor_limit = end_index

                end_index += 1

        start_index += 1

    # arrange the starting index and the ending index into a list
    found_indices = [start_in_gene, end_in_gene]

    return found_indices


def choose_splice(listA, listB):
    '''([int, int], [int, int]) -> int
    Helper function used for splice_gene function:
    Takes and compares two lists containing two integers, the first
    representing the anchor string indices reading forwards, and the second
    representing the anchor string indices reading backwards. Determines which
    of the genes should be used for splicing a gene sequence.
    Returns 0 if the first list should be used, 1 if the second list should be
    used, and -1 if neither of the lists should be used.
    REQ: all elements in listA >= -1
    REQ: all elements in listB >= -1
    >>> choose_splice([0,4], [0,4])
    0
    >>> choose_splice([3,5], [2,6])
    1
    >>> choose_splice([-1, 4], [5, -1])
    -1
    '''
    # check if both anchor strings were found in either listA or listB
    splice_check = ((-1) not in listA or (-1) not in listB)

    # if at least one list finds both anchor strings
    if splice_check:
        # check which list has both anchor strings

        if (-1) in listA:   # if anchor string was not found in listA
            splice = 1   # take listB

        elif (-1) in listB:  # if anchor string was not found in listB
            splice = 0  # take listA

        # both anchor strings were found in listA and listB
        elif ((-1) not in listA and (-1) not in listB):

            # compare the sequences to see which one is the first shortest

            # if the indices are equal or
            # the forward sequence is smaller, take listA
            if (listA == listB) or (listA < listB):
                splice = 0

            # else if the backward sequence is smaller, take the backward one
            elif listA > listB:
                splice = 1

    # if neither sequence found the anchor strings, return -1
    else:
        splice = -1

    return splice


def splice_gene(source, destination, start, end):
    '''(list, list, str, str) -> NoneType
    Takes 2 list representations of genes along with strings representing
    start and end anchor strings. Splices the subsequence of source between
    the anchor strings into destination between the anchor strings.
    If an anchor occurs more than once in a string,
    the first shortest sequence will be used (the sequence from the first
    start anchor to the first end anchor after it).
    REQ: len(start) < min(len(source), len(destination))
    REQ: len(end) < min(len(source), len(destination))
    >>> source = ['T', 'G', 'C', 'T', 'A', 'G', 'T']
    >>> destination = ['T', 'A', 'C', 'A', 'T', 'G', 'T', 'G', 'G', 'G']
    >>> splice_gene (source, destination, "AT", "GT")
    >>> source
    ['G', 'T']
    >>> destination
    ['T', 'A', 'C', 'A', 'T', 'C', 'G', 'T', 'G', 'G', 'G']
    '''
    # use find_anchors function to check for anchors in source and destination
    source_forward = find_anchors(source, start, end, False)
    source_backward = find_anchors(source, start, end, True)
    dest_forward = find_anchors(destination, start, end, False)
    dest_backward = find_anchors(destination, start, end, True)

    # index the anchor checks into separate source and destination list
    # in order to have a reference for them (0 for forward, 1 for backward)
    source_anchors = [source_forward, source_backward]
    dest_anchors = [dest_forward, dest_backward]

    # use choose_splice function to choose which anchor sequence to use
    # represent the variables as an index in each anchors list
    source_index = choose_splice(source_forward, source_backward)
    dest_index = choose_splice(dest_forward, dest_backward)

    # define the start and end indices of the source and destination splices
    source_start = source_anchors[source_index][0]
    source_end = source_anchors[source_index][1]
    dest_start = dest_anchors[dest_index][0]
    dest_end = dest_anchors[dest_index][1]

    # define the splice statements within the source and destination
    source_splice = source[source_start:source_end + 1]
    dest_splice = destination[dest_start:dest_end + 1]

    # check if anchor strings were found either backwards or forwards
    # in both source and destination
    if (source_index != -1) and (dest_index != -1):

        # splice with a flipped source if indices are not equal
        if source_index != dest_index:
            source_splice = source_splice[::-1]

        # create a variable for all elements after the destination splice
        # delete all elements after the destination splice from destinaion
        # delete the destination splice from destination
        dest_extra = destination[dest_end + 1:]
        del(destination[dest_end + 1:])
        del(destination[dest_start:dest_end + 1])

        # add the source splice to the destination
        # add back the elements that were after the destination splice
        # delete the source splice from source
        destination.extend(source_splice)
        destination.extend(dest_extra)
        del(source[source_start:source_end + 1])


def mask_to_list(mask):
    '''(str) -> list
    Helper function used for match_mask function:
    Takes in a string representation of a mask and separates it into separate
    elements in a list.
    REQ: Any integers in mask > 0
    REQ: len(mask) > 0
    REQ: mask.count('[') == mask.count(']')
    REQ: elements of mask in NUCLEOS, NUMLIST or [ '[', ']', '*' ]
    REQ: mask cannot start with element in NUMLIST
    >>> mask_to_list('G[ACT]')
    ['G', ['A', 'C', 'T']]
    >>> mask_to_list('G2C5A4')
    ['G', 'G', 'C', 'C', 'C', 'C', 'C', 'A', 'A', 'A', 'A']
    >>> mask_to_list('G*A4C')
    ['G', '*', 'A', 'A', 'A', 'A', 'C']
    '''
    # create empty list to store elements in mask separately
    mask_list = []

    # create a variable to check for open bracket sequences in the mask
    brackets = 0

    # run through the whole mask

    # set a variable for the index in the mask_list
    # mask_index differs from mask_list_index when a multi or number is passed
    mask_index = 0
    mask_list_index = 0
    while mask_index < len(mask):

        # check for consecutive numbers in mask
        # and index is not at the end of the mask
        if mask[mask_index] in NUM_LIST:

            # create a variable for the element previous to the number
            nucleo_repeat = mask_list[mask_list_index - 1]
            num_string = ''

            # find the next element not in NUM_LIST
            find_not_num = mask_index + 1

            # run from the current mask_index to the end of the mask
            mask_limit = len(mask)
            while find_not_num < mask_limit:

                # check if the next element is a number
                # if it is, find the next element
                # if it's not, stop the while loop by setting the limit equal
                # to the current index
                if mask[find_not_num] in NUM_LIST:
                    find_not_num += 1

                else:
                    mask_limit = find_not_num

            num_string = mask[mask_index:find_not_num]
            for repeat_index in range(int(num_string) - 1):
                mask_list.append(nucleo_repeat)
            mask_index = find_not_num
            mask_list_index = len(mask_list) - 1

        # check if element is a multi-starting sign
        elif mask[mask_index] == MULTI_START:
            # add a multi sequence
            brackets += 1
            multi_check = mask_index + 1

            # create a new multi list to store the elements in the multi
            multi_list = []

            # if there is at least 1 open multi sequence
            while brackets != 0:

                # check if the element is another multi-starting sign
                if mask[multi_check] == MULTI_START:
                    # add another multi sequence
                    brackets += 1

                # if the element is a multi-ending sign
                elif mask[multi_check] == MULTI_END:
                    # subtract a multi sequence
                    brackets -= 1

                # add element to the multi if it is a nucleotide and it is not
                # already in the multi list
                is_unique = mask[multi_check] not in multi_list
                is_nucleotide = mask[multi_check] in NUCLEOS
                is_star = mask[multi_check] == '*'

                if is_unique and (is_nucleotide or is_star):
                    multi_list += mask[multi_check]

                # continue through the list
                multi_check += 1

            # if there is a star in the multi, change the multi to a star
            if '*' in multi_list:
                multi_list = '*'

            mask_list += [multi_list]
            mask_index = multi_check

        # check if the element is a nucleotide
        elif mask[mask_index] in NUCLEOS or mask[mask_index] == '*':
            # add it to the mask_list
            mask_list += mask[mask_index]
            mask_index += 1

        mask_list_index += 1
    return mask_list


def match_mask(gene, mask):
    '''(str, str) -> int
    Takes in a string representations of a gene and a mask, locates the first
    sequence in the gene that matches the mask, and returns the index of the
    first nucleotide in such sequence. Returns -1 if no matching sequence is
    found.
    REQ: Any integers in mask > 0
    REQ: len(gene) > 0
    REQ: len(mask) > 0
    REQ: mask.count('[') == mask.count(']')
    >>> match_mask('ACTGCATCCCCGATG', '[GAC]G4')
    6
    >>> match_mask('GGGGACATCAGGGG', 'C4')
    0
    >>> match_mask('ACTGTACTGTGCATG', '*C2G')
    -1
    '''
    # use the gene_swap function to create a variable that is
    # the equivalent of the pair of the mask, in mask form
    mask_pair = gene_swap(mask)

    # convert the gene to a list
    # convert the mask_pair to a list using mask_to_list function
    gene_list = list(gene)
    mask_pair_forward = mask_to_list(mask_pair)
    mask_pair_backward = mask_pair_forward[::-1]

    # gene scan runs from the start of the gene up to the point where
    # the endpoint of the mask list meets the gene
    # (forward and reverse are same length)
    gene_scan_limit = len(gene) - (len(mask_pair_forward) - 1)

    # create lists for the forwards and backwards masks
    # and the first indices of the nucleotides that match the
    # forward and backward masks
    mask_pairs = [mask_pair_forward, mask_pair_backward]
    found_pairs = [-1, -1]

    # find the pairing index for the forward and backwards masks
    for next_mask in mask_pairs:

        # define if the mask is forward or backward by its index in mask_pairs
        # if the forward and backward masks are identical, the index defaults
        # to the forward direction
        pair_index = mask_pairs.index(next_mask)

        # run the mask from the beginning of the gene to the point where the
        # endpoint of the mask meets the end of the gene
        gene_index = 0
        mask_limit = len(gene) - (len(next_mask) - 1)

        while gene_index < mask_limit:

            # define a sequence index that runs from the current gene_index to
            # the last element the mask meets, starting from the gene_index
            seq_index = gene_index
            mask_index = 0
            mask_range = seq_index + len(next_mask)

            while seq_index < mask_range:

                # check if either:
                # - the nucleotide in gene pairs with the nucleotide in mask
                # - the nucleotide in gene pairs with a multi in the mask
                # - the nucleotide in the mask is a star
                pair_check = gene[seq_index] == next_mask[mask_index]
                multi_check = gene[seq_index] in next_mask[mask_index]
                star_check = next_mask[mask_index] == '*'

                match_check = pair_check or multi_check or star_check
                # if none of these cases are met, stop the while loop
                if not match_check:
                    mask_range = seq_index

                # if at least one of the cases is met and we've reached the
                # last nucleotide, we've found the matching sequence
                elif (match_check) and (seq_index == mask_range - 1):

                    # set the corresponding index in found_pairs to the
                    # index of the first nucleotide of the matching sequence
                    found_pairs[pair_index] = gene_index

                    # stop the two while loops
                    mask_range = seq_index
                    mask_limit = gene_index

                seq_index += 1
                mask_index += 1

            gene_index += 1

    # check if a pair was found in either the forwards or backwards mask
    pair_found = found_pairs[0] != -1 or found_pairs[1] != -1

    # if at least one direction has a pair
    if pair_found:

        # check which direction paired
        # if forwards direction didn't pair, take backwards index
        # elif backwards direction didn't pair, take forwards index
        if found_pairs[0] == -1:
            pair = found_pairs[1]

        elif found_pairs[1] == -1:
            pair = found_pairs[0]

        # elif they both paired, take the smaller of the two
        # elif they're equal take the forward direction
        elif (found_pairs[0] != -1 and found_pairs[1] != -1):

            if (found_pairs[0] == found_pairs[1]):
                pair = found_pairs[0]

            else:
                pair = min(found_pairs[0], found_pairs[1])

    # if neither direction found a pair, return -1
    else:
        pair = -1

    return pair


def process_gene_file(file, gene, mask):
    '''(io.TextIOWrapper, str, str) -> (int, int, int)
    Takes in an file handle open for reading, and string representations of
    both a gene and a mask. Returns a tuple containing 3 integers:
    - First integer: the index of the first line that can pair with the gene
    - Second integer: the index of the first line with a sequence that
      matches the mask
    - Third integer: the index of the line (from the beginning of the file
      up to the point where the first and second integer are found)
      with the longest gene zip.
    Returns -1 for the first or second integer if they are not found.
    REQ: all elements in gene are in NUCLEOS
    REQ: all elements in mask are in NUCLEOS, NUM_LIST, or ['[', ']', '*']
    '''
    # create boolean cases for
    # - if a pair is not found
    # - if a matched mask is not found
    # default to True because they haven't been found yet
    no_pair = True
    no_mask = True

    # define values for the lines that pair, match masks, and zip the longest
    pair_line = -1
    match_line = -1
    max_zip = 0
    max_zip_line = 0

    # define list of all the lines in the file
    file_genes = file.readlines()
    # run through the whole list (or until there is a pair and a mask found)
    line_index = 0

    # remove newline character from file lines
    file_index = 0
    for line in file_genes:
        file_genes[file_index] = line.rstrip('\n')
        file_index += 1

    # check if there is both no pair or mask, and up to the
    # last line in the file
    while (no_pair or no_mask) and line_index < len(file_genes):
        # check if there is not already a pair and if the gene and the current
        # line pair (using pair_genes function)
        if no_pair and pair_genes(file_genes[line_index], gene):
            # if there is a pair, set the pair
            no_pair = False
            pair_line = line_index

        # check if there is not already a match for the mask and if the mask
        # and a sequence in the current line pair (using match_mask function)
        if no_mask and match_mask(file_genes[line_index], mask) != -1:
            no_mask = False
            match_line = line_index

        # use zip_length function to calculate how much the line zips
        line_zip = zip_length(file_genes[line_index])

        # if the zip is longer than the currently longest zip, change the
        # longest zip to the current zip
        if line_zip > max_zip:
            max_zip_line = line_index

        line_index += 1

    return (pair_line, match_line, max_zip_line)
