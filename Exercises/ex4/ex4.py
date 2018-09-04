def insert(listA, listB, index):
    '''(list or str, list or str, int) -> list or str
    Given two lists or two strings, and an index, returns a combined version
    of the two strings, where the second parameter is added to the first
    parameter at the specified index.
    >>> insert([1, 2, 3], ['a', 'b', 'c'], 2)
    [1, 2, 'a', 'b', 'c', 3]
    >>> insert("123","abc",2)
    '12abc3'
    '''
    # define new variable for spliced lists
    # first part of listA + list A + second part of list A

    newlist = listA[0:index] + listB + listA[index:len(listA)]
    return newlist


def up_to_first(listA, obj):
    '''(list or str, obj) -> list or str
    Given a list/string and an object, returns a copy of the list/string
    up to the first occurence of the object. If not, it will return the
    same list/string.
    >>> up_to_first([1, 2, 3, 4], 3)
    [1, 2]
    >>> up_to_first([1, 2, 3, 4], 9)
    [1, 2, 3, 4]
    >>> up_to_first('abcdef', 'd')
    'abc'
    '''
    # return the same list/string if obj is not in list/string
    if obj not in listA:
        newlist = listA

    # return the truncated list/string if obj is in list/string
    else:
        newlist = listA[0:listA.index(obj)]

    return newlist


def cut_list(listA, index):
    '''(list or str, int) -> list or str
    Given a list/string and an object, returns a copy of the list/string sliced
    at a specified index. The elements before and after the index will be
    swapped.
    REQ: 0 <= index
    >>> cut_list([0,1,2,3,4,5,6,7,8,9], 3)
    [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]
    >>> cut_list("ABCDEFGX1234",7)
    '1234XABCDEFG'
    '''

    # convert negative index to corresponding positive index
    if -len(listA) < index < 0:
        index = len(listA) + index

    # new list = elements after index + index + elements before index
    newlist = listA[index+1:len(listA)] + listA[index:index+1] + listA[0:index]
    return newlist
