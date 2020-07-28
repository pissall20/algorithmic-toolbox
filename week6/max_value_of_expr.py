# Uses python3

"""Maximum Value of an Arithmetic Expression

    Task: Find the maximum value of an arithmetic expression by specifying
    the order of applying its arithmeticoperations using additional parentheses.
    Input Format: The only line of the input contains a string s of length2n+ 1for some n,
    with symbols s0, s1, . . . , s2n. Each symbol at an even position of s is a digit
    (that is, an integer from 0 to 9) whileeach symbol at an odd position is one of three
    operations from{+,-,*}."""


# using https://github.com/taochenshh/Maximize-the-Value-of-an-Arithmetic-Expression-with-Dynamic-Programming/blob/master/placing_parentheses.cpp


def evalt(a, b, op):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '*':
        return int(a) * int(b)
    else:
        assert False


def get_maximum_value(equation):
    length = (len(equation) + 1) // 2

    # arrange arrays for mins and maxes filled with zeros
    min_array = [[0 for i in range(length)] for i in range(length)]
    max_array = [[0 for i in range(length)] for i in range(length)]

    # fill the diagonal with numbers from equations
    for i in range(length):
        min_array[i][i] = equation[2 * i]
        max_array[i][i] = equation[2 * i]

    for s in range(length - 1):
        for i in range(length - s - 1):
            j = i + s + 1
            # set bounds
            min_val = float('inf')
            max_val = float('-inf')

            # find the minimum and maximum values for the expression
            # between the ith number and jth number
            for k in range(i, j):
                a = evalt(min_array[i][k], min_array[k + 1][j], equation[2 * k + 1])
                b = evalt(min_array[i][k], max_array[k + 1][j], equation[2 * k + 1])
                c = evalt(max_array[i][k], min_array[k + 1][j], equation[2 * k + 1])
                d = evalt(max_array[i][k], max_array[k + 1][j], equation[2 * k + 1])
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)

            min_array[i][j] = min_val
            max_array[i][j] = max_val

    return max_array[0][length - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
