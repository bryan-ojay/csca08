# Global variables. Feel free to play around with these
# but please return them to their original values before you submit.
# HINT: Your code should be using these values, if I change them (and I will)
# your output should change accordingly
a0_weight = 5
a1_weight = 7
a2_weight = 8
term_tests_weight = 25
exam_weight = 40
exercises_weight = 10
quizzes_weight = 5

a0_max_mark = 25
a1_max_mark = 50
a2_max_mark = 100
term_tests_max_mark = 50
exam_max_mark = 100
exercises_max_mark = 10
quizzes_max_mark = 5
exam_pass_mark = 40
overall_pass_mark = 50


def get_max(component_name):
    '''(str) -> float
    Given the name of a course component (component_name),
    return the maximum mark for that component. This is used to allow the GUI
    to display the "out of" text beside each input field.
    REQ: component_name in {'a0', 'a1', 'a2', 'exercises', 'term tests',
    'quizzes', 'exam'}
    >>> get_max('a0')
    25
    >>> get_max('exam')
    100
    '''
    # DO NOT EDIT THIS FUNCTION. This function exists to allow the GUI access
    # to some of the global variables. You can safely ignore this function
    # for the purposes of Ex2.
    if(component_name == 'a0'):
        result = a0_max_mark
    elif(component_name == 'a1'):
        result = a1_max_mark
    elif(component_name == 'a2'):
        result = a2_max_mark
    elif(component_name == 'exercises'):
        result = exercises_max_mark
    elif(component_name == 'term tests'):
        result = term_tests_max_mark
    elif(component_name == 'quizzes'):
        result = quizzes_max_mark
    else:
        result = exam_max_mark

    return result


def percentage(raw_mark, max_mark):
    ''' (float, float) -> float
    Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark of max_mark.
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: raw_mark <= xmax_mark
    >>> percentage(15, 20)
    75.0
    >>> percentage(4.5, 4.5)
    100.0
    '''
    # return percentage: (float1 divided by float2) multiplied by 100%
    return (float(raw_mark)/float(max_mark)) * 100


def contribution(raw_mark, max_mark, weight):
    ''' (float, float, float) -> float
    Given a piece of work where the student earned raw_mark marks out of a
    maximum of max_marks marks possible, return the number of marks it
    contributes to the final course mark if this piece of work is worth weight
    marks in the course marking scheme.
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: weight >= 0
    >>> contribution(13.5, 15, 10)
    9.0
    '''
    result = (raw_mark/max_mark)*weight
    return result


def term_work_mark(a0, a1, a2, exercises, quizzes, term_tests):
    '''(float, float, float, float, float, float) -> float
    Given a student's marks on all coursework components to return the
    cumulative coursework mark comprised of said given components in
    this order: (assignement 0, assignment 1, assignment 2,
    exercises, quizzes, term tests)
    REQ: 0 <= a0 <= a0_max_mark
    REQ: 0 <= a1 <= a1_max_mark
    REQ: 0 <= a2 <= a2_max_mark
    REQ: 0 <= exercises <= exercises_max_mark
    REQ: 0 <= quizzes <= quizzes_max_mark
    REQ: 0 <= term_tests <= term_tests_max_mark
    >>> term_work_mark(25, 50, 100, 10, 5, 50)
    60.0
    >>> term_work_mark(20, 45, 70, 8, 4, 40)
    47.9
    '''
    # Get weighted percentages of coursework components
    # (contribution function)
    a0_mark = contribution(a0, a0_max_mark, a0_weight)
    a1_mark = contribution(a1, a1_max_mark, a1_weight)
    a2_mark = contribution(a2, a2_max_mark, a2_weight)
    exercise_mark = contribution(exercises, exercises_max_mark,
                                 exercises_weight)
    quizzes_mark = contribution(quizzes, quizzes_max_mark, quizzes_weight)
    term_test_mark = contribution(term_tests, term_tests_max_mark,
                                  term_tests_weight)

    # Return term mark out of the set weight percentage
    # (default max value is 60)
    return(a0_mark + a1_mark + a2_mark + exercise_mark +
           quizzes_mark + term_test_mark)


def final_mark(a0, a1, a2, exercises, quizzes, term_tests, exam):
    '''(float, float, float, float, float, float, float) -> float
    Given a student's marks on all coursework components, in this order:
    (assignment 0, assignment 1, assignment 2, exercises, quizzes, term tests,
    exam) to return the cumulative coursework mark comprised of said given
    components.
    REQ: 0 <= a0 <= a0_max_mark
    REQ: 0 <= a1 <= a1_max_mark
    REQ: 0 <= a2 <= a2_max_mark
    REQ: 0 <= exercises <= exercises_max_mark
    REQ: 0 <= quizzes <= quizzes_max_mark
    REQ: 0 <= term_tests <= term_tests_max_mark
    REQ: 0 <= exam <= exam_max_mark
    >>> final_mark(25, 50, 100, 10, 5, 50, 100)
    100.0
    >>> final_mark(20, 45, 70, 8, 4, 40, 73)
    77.1
    '''
    # Get weighted percentages of all coursework components
    # (contribution function)
    pre_exam_mark = term_work_mark(a0, a1, a2, exercises, quizzes, term_tests)
    exam_mark = contribution(exam, exam_max_mark, exam_weight)

    # Return term mark out of 100
    return (pre_exam_mark + exam_mark)


def is_pass(a0, a1, a2, exercises, quizzes, term_tests, exam):
    '''(float, float, float, float, float, float, float) -> bool
    Given a student's marks on all coursework components, in this order:
    (assignment 0, assignment 1, assignment 2, exercises, quizzes, term tests,
    exam), and calculates if the student's marks are sufficient to pass the
    course.
    REQ: 0 <= a0 <= a0_max_mark
    REQ: 0 <= a1 <= a1_max_mark
    REQ: 0 <= a2 <= a2_max_mark
    REQ: 0 <= exercises <= exercises_max_mark
    REQ: 0 <= quizzes <= quizzes_max_mark
    REQ: 0 <= term_tests <= term_tests_max_mark
    REQ: 0 <= exam <= exam_max_mark
    >>> is_pass(20, 45, 70, 8, 4, 40, 41)
    True
    >>> is_pass(20, 45, 70, 8, 4, 40, 39)
    False
    >>> is_pass(10, 21, 12, 2, 1, 15, 23)
    False
    '''
    # Get weighted percentages of all coursework components
    # (contribution function)
    course_mark = final_mark(a0, a1, a2, exercises, quizzes, term_tests, exam)

    # Check boolean conditions: Final mark is above passing grade AND exam mark
    # is above individual passing grade

    final_check = course_mark >= overall_pass_mark
    exam_check = exam >= exam_pass_mark
    pass_check = (exam_check and final_check)
    return pass_check

print (is_pass(110, 21, 12, 2, 1, 15, exam_pass_mark+1))