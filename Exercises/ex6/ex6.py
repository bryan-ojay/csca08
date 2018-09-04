def copy_me(listA):
    '''(list) -> list
    Takes a list as input and returns a copy of the list with strings converted
    to all uppercase, integers and floats increased by a value of 1, booleans
    negated and lists replaced with the word "List".
    >>> copy_me([[1,2,3], "asdf", 1.5, 44, True])
    ['List', 'ASDF', 2.5, 45, False]
    >>> copy_me([222, 21.455, False, ['a','b','c'], "adsds"])
    [223, 22.455, True, 'List', 'ADSDS']
    '''
    # create empty list to put mutated elements into
    newlist = list()

    # scan all elements in the old list
    for elem in listA:
        # change all string to uppercase
        if type(elem) == str:
            elem = elem.upper()

        # add 1 to ints and floats
        elif (type(elem) == int) or (type(elem) == float):
            elem += 1

        # reverse all booleans
        elif type(elem) == bool:
            elem = not elem

        # change all lists to "List"
        elif type(elem) == list:
            elem = "List"

        # add the (possibly mutated) elem to the new list
        newlist.append(elem)

    return newlist


def mutate_me(listA):
    '''(list) -> NoneType
    Takes a list as input, and mutates the list by converting strings to all
    uppercase, increasing all integers and floats by 1, negating all booleans
    and replacing lists with the word "List".
    >>> listA = [[1,2,3], "asdf", 1.5, 44, True]
    >>> mutate_me(listA)
    >>> listA
    ['List', 'ASDF', 2.5, 45, False]
    '''
    # scan all elements in the list
    for elem in range(len(listA)):
        # change all string to uppercase
        if type(listA[elem]) == str:
            listA[elem] = listA[elem].upper()

        # add 1 to ints and floats
        elif (type(listA[elem]) == int) or (type(listA[elem]) == float):
            listA[elem] += 1

        # reverse all booleans
        elif type(listA[elem]) == bool:
            listA[elem] = not listA[elem]

        # change all lists to "List"
        elif type(listA[elem]) == list:
            listA[elem] = "List"
