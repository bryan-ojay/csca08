"""CSCA08 Assignment 2, Fall 2017
 I hereby agree that the work contained herein is solely my work and that I
 have not received any external help from my peers, nor have I used any
 resources not directly supplied by the course in order to complete this
 assignment. I have not looked at anyone else's solution, and no one has
 looked at mine. I understand that by adding my name to this file, I am
 making a formal declaration, and any subsequent discovery of plagiarism
 or other academic misconduct could result in a charge of perjury in
 addition to other charges under the academic code of conduct of the
 University of Toronto Scarborough Campus
 Name:
 UtorID:
 Student Number:
 Date:
"""
if(__name__ == "__main__"):
    # create a new Male client with ID 12345
    father = Male('12345')
    # create a new Female client with ID 67890
    mother = Female('67890')
    # set chromosome pair 12 position 45 to be AG
    father.set_by_pos(12, 45, 'AG')
    mother.set_by_pos(12, 45, 'CT')
    # set chromosome marker rs12345 to refer to chromosome
    # pair 3, position 97
    father.set_marker('rs12345', 3, 97)

    # set marker rs12345 to be GT
    father.set_by_marker('rs12345', 'GT')
    # this should return "AG"
    result_str = father.get_by_pos(12, 45)
    # this should return "GT"
    result_str2 = father.get_by_marker('rs12345')
    c = father.get_chromosome(3)
    # This will set father's pair 3-85 to be "TA"
    c.set_by_pos(85, 'TA')
    # Now mother and father share a chromosome pair, updating
    # one will update the other
    mother.set_chromosome(7, c)

    # create a new query object
    query = Query()
    query.set_by_pos(12, 45, 'AG')
    # this should return True since 12-45 in the query matches
    # with 12-45 in father
    result = father.test(query)
    query.set_by_pos(12, 45, 'A1')
    query.set_marker('rs12345', 3, 97)
    # now the query will only work if 12-45 is AX and 3-97 is XT for
    # some value of X
    query.set_by_marker('rs12345', '1T')

    # create a new binder object
    binder = Binder()
    # set chromosome pair position 45 to be left maternal
    # (this means that the offspring will have 12-45 equal to CG
    # e.g., gets the left C from mother and the right G from father)
    binder.set_by_pos(12, 45, 'LM')

    # this means any offspring created with this binder will be female
    binder.set_sex("F")
    child = mother.procreate(father, binder)
