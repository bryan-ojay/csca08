def function_names(file):
    '''(io.TextIOWrapper) -> list
    Takes a file handle open for reading as a parameter, and returns a list of
    all of the function names in the file.
    '''
    # create empty list for function names
    func_list = []

    # read through all of the lines in the document
    for next_line in file:
        # all lines defining a function start with "def "
        if next_line.startswith("def "):
            # 1. take the line defining the function
            # 2. take everything after "def " on the line (from index 4)
            # 3. split the line at the point where parameters are taken: "("
            # 4. list is created, take the 0th element of that list
            #    which is the name of the function.
            func_name = next_line[4:].split("(")[0]
            func_list.append(func_name)

    # return the function name list
    return func_list


def justified(file):
    '''(io.TextIOWrapper) -> bool
    Takes a file handle open for reading as a parameter, determines if every
    single line in the file is left-justified (meaning every line starts with
    something that is not a space)
    '''
    # read through all of the lines in the document
    for next_line in file:
        # if the current line starts with a space
        if next_line.startswith(' '):
            # the file is not left justified
            return False

    # if the for loop is completed, the file is left-justified
    return True


def section_average(file, section):
    '''(io.TextIOWrapper, str) -> float or NoneType
    Takes a file handle containing information of student's midterm marks open
    for reading and a lecture section code as parameters, and returns the
    average midterm mark for that section, or None if there are no marks
    recorded for that section.
    >>> section_average(open('ex5_grade_file.txt','r'), 'LEC30')
    12.25
    >>> section_average(open('ex5_grade_file.txt','r'), 'LEC20')
    '''
    # create variables for class total and number of marks inputted
    class_total = 0
    mark_inputs = 0
    # read through all of the lines in the document
    for next_line in file:
        # split the line (in string form) by the spaces in the line
        student_info = next_line.split()
        # if the lecture code is the same as the parameter
        if student_info[-2] == section:
            # increase the number of marks inputted and the class total
            mark_inputs += 1
            class_total += float(student_info[-1])
    # check if marks were inputted or not
    if mark_inputs == 0:
        class_avg = None
    else:
        # class average is the total marks divided by the number of inputs
        class_avg = class_total / mark_inputs
    return class_avg
