"""

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
Consider use range(#begin, #end) method

"""

result = []                                         #creating empty list to store result
for i in range(2000, 3201):                         #iterating in given range from 2000 to 3200 (2000 < 3201)
    if i%7 == 0 and i%5 != 0:                       #if remainder of 7 and i equals to zero AND remainder of 5 and i not equals to 0
        result.append(str(i))                       #then append result of if statement to a list

print(', '.join(result))                            #printing result in a comma-separated sequence
