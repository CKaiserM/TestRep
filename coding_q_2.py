"""

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

"""

"""
memo = {}

def fact_recursive(n):                              #recursive
    if n < 2:
        return 1                                    #if n is smaller than 2 function returns factorial equal to 1
    return n * fact_recursive(n - 1)                #if factorial number n is greater than 1, function will execute itself until n = 1


def fact_for_loop(n):                               #computing factorial with 'for' loop
    result = 1
    if n < 2:
        return 1                                    #if n is smaller than 2 function returns factorial equal to 1
    for i in range(1,n+1):                          #for i in range 1 to n+1 (1, 2, 3, 4, ..., n)
        result *= i                                 #return factorial result (1 * 2 * 3 * ... * n)
    return result

n = int(input("Give a number to compute your factorial: "))     #user input
print(fact_recursive(n))                                        #returns result
#print(fact_for_loop(n))
