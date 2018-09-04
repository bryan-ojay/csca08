def create_dict(file):
    '''(io.TextIOWrapper) -> dict of {str: [str, str, str, int, str]}
    Takes an open file handle, returns a dictionary that maps a person's
    username to a list containing their last and first names, email, age and
    gender.
    REQ: age >= 0
    REQ: gender in [M, F, X]
    '''
    # create an empty dictionary for inputting values
    info_dict = {}

    # read through all the lines in the document
    for next_line in file:
        # separate the person's username and other info
        username = next_line.split()[0]
        info = next_line.split()[1:]

        # assign separate variables to each value
        first_name = info[0]
        last_name = info[1]
        age = int(info[2])  # age must be an integer value
        gender = info[3]
        email = info[4]

        # assign objects to their appropriate places
        info_update = [last_name, first_name, email, age, gender]

        # map the username to the list of info in the dict
        info_dict[username] = info_update

    return info_dict


def update_field(old_dict, username, field_name, new_value):
    '''(dict, str, str, str or int) -> NoneType
    Takes in a dictionary in the same format defined in the create_dict
    function, a person's username, the name of a field, and a new value
    to replace the current value of the field.
    REQ: field_name in ['LAST', 'FIRST', 'E-MAIL', 'AGE', 'GENDER']
    REQ: old_dict[username] must contain fields in field_name
    >>> my_dict = {'sclause':['Clause', 'Santa', 'santa@xmas.np', 450, 'M']}
    >>> update_field(my_dict, 'sclause', 'AGE', 999)
    >>> my_dict == {'sclause': ['Clause', 'Santa', 'santa@xmas.np', 999, 'M']}
    True
    '''
    # create a list for all of the callable field names
    # matches the indices of the fields in old_dict
    field_list = ['LAST', 'FIRST', 'E-MAIL', 'AGE', 'GENDER']

    # assign an index to the chosen field name from the field list
    field_index = field_list.index(field_name)

    # assign the new value at the specified index of the info_list
    old_dict[username][field_index] = new_value


def select(format_dict, field_select, field_check, value_check):
    '''(dict, str, str, str or int) -> set
    Takes in a dictionary as formatted as in the create_dict() function,
    the name of a field to select, the name of a field to check,
    and a value to check for. Returns a set containing the
    selected field data elements from people who match the corresponding value
    from the field to be checked.
    REQ: field_name in ['LAST', 'FIRST', 'E-MAIL', 'AGE', 'GENDER']
    >>> my_dict = {'sclause':['Clause', 'Santa', 'santa@xmas.np', 450, 'M'],
    ... 'ebunny':['Bunny', 'Easter', 'bunny@easter.hop', 99, 'M'],
    ... 'tfairy':['Fairy', 'Tooth', 'fairy@money4teeth.net', 0, 'F']}
    >>> my_select = select(my_dict, 'E-MAIL', 'GENDER', 'M')
    >>> my_select == {'bunny@easter.hop', 'santa@xmas.np'}
    True
    '''
    # create an empty set for the data elements
    data_elements = set()

    # create a list for all of the callable field names
    # matches the indices of the fields in old_dict
    field_list = ['LAST', 'FIRST', 'E-MAIL', 'AGE', 'GENDER']

    # assign an index to the chosen field name from the field list
    check_index = field_list.index(field_check)
    select_index = field_list.index(field_select)

    # run through the whole dictionary
    for person in format_dict:
        # if the person's value matches the value check
        if format_dict[person][check_index] == value_check:
            # add the person's data to the set of data elements
            data_elements.add(format_dict[person][select_index])

    return data_elements
