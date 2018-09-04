def calc(num1, num2, operator):
    '''(float, float, str) -> float
    Returns the result of a basic operation given two numbers and the operand.
    REQ: operator == ('+' or '-' or '*' or '/' or '//' or '**' or '%')
    >>> calc (2, 10, '+')
    12
    >>> calc (2, 10, '&')
    wrong operator
    '''
    # check if first two variables are integers, wrong input type if true

    if (type(num1) != int) or (type(num2) != int):
        return "Wrong input type"

    # check if third variable is a valid operator
    valid_operators == ['+', '-', '*', '/', '//', '**', '%']
    
    elif (operator not in valid_operators):
        return "Wrong operator"

    # if none of these cases, continue with the calculator
    # return num1 (operator) num2 for each case

    else:
        if operator == "+":
            return (num1 + num2)
        elif operator == "-":
            return (num1 - num2)
        elif operator == "*":
            return (num1 * num2)
        elif operator == "/":
            if num2 == 0:
                return "Undefined."
            else:
                return (num1 / num2)
        elif operator == "//":
            if num2 == 0:
                return "Undefined"
            else:
                return (num1 // num2)
        elif operator == "**":
            return (num1 ** num2)
        elif operator == "%":
            if num2 == 0:
                return "Undefined"
            else:
                return (num1 % num2)
