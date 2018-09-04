def percent_to_gpv(grade):
    '''
    (int) -> float
    Given a percentage grade, returns the corresponding grade point average.
    REQ: 0 <= grade <= 100
    >>> percent_to_gpv(44)
    0.0
    >>> percent_to_gpv(70)
    2.7
    >>> percent_to_gpv(89)
    4.0
    '''
    # Create if statements for all grade cases, assign matching value to gpv
    if (85 <= grade <= 100):
        gpv = 4.0
    elif (80 <= grade <= 84):
        gpv = 3.7
    elif (77 <= grade <= 79):
        gpv = 3.3
    elif (73 <= grade <= 76):
        gpv = 3.0
    elif (70 <= grade <= 72):
        gpv = 2.7
    elif (67 <= grade <= 69):
        gpv = 2.3
    elif (63 <= grade <= 66):
        gpv = 2.0
    elif (60 <= grade <= 62):
        gpv = 1.7
    elif (57 <= grade <= 59):
        gpv = 1.3
    elif (53 <= grade <= 56):
        gpv = 1.0
    elif (50 <= grade <= 52):
        gpv = 0.7
    elif (0 <= grade <= 49):
        gpv = 0.0
    return gpv


def card_namer(value, suit):
    '''
    (str, str) -> str
    Given two single character strings (one for card value and
    one for suit value), returns the full name of the card.
    REQ: value in {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T',
    'J', 'Q', 'K'}
    >>> card_namer('Q','D')
    'Queen of Diamonds'
    >>> card_namer('9','S')
    '9 of Spades'
    >>> card_namer('8','T')
    'CHEATER!'
    '''
    # Create lists for single characters values and suits
    value_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9',
                       'T', 'J', 'Q', 'K']
    suit_list = ['D', 'C', 'H', 'S']

    # Create lists for full names of values and suits
    full_value_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                       '10', 'Jack', 'Queen', 'King']

    full_suit_list = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

    # Check if valid suit list is entered. If not, return 'CHEATER!'
    if (suit not in suit_list):
        return 'CHEATER!'

    # If valid suit is entered, return the full name of the card.
    else:
        # Get the full value/suit of list by finding the index
        # of the short version in the short list, than substitute it into the
        # full value/suit index.

        full_value = full_value_list[value_list.index(value)]
        full_suit = full_suit_list[suit_list.index(suit)]
        return (full_value + ' of ' + full_suit)


def my_str(obj):
    '''(object) -> str
    Converts a given object into a custom designed string output.
    >>> my_str("Hello")
    'Hello'
    >>> my_str(False)
    'NO'
    >>> my_str(42)
    'Medium Number'
    >>> my_str(42.0)
    '42.0'
    >>> my_str(3.1415926)
    '3.14'
    >>> my_str([1, 2, 3])
    'I dunno'
    '''
    # Create cases for all data types
    # -------
    # str
    if type(obj) == str:
        return obj

    # bool
    elif type(obj) == bool:
        if obj is True:
            return "YES"
        else:
            return "NO"

    # float
    elif type(obj) == float:
        return str(round(obj, 2))

    # int
    elif type(obj) == int:
        if (obj <= 10):
            return "Small Number"
        elif (11 <= obj <= 99):
            return "Medium Number"
        elif (obj >= 100):
            return "Large Number"

    # other data types
    else:
        return "I dunno"
