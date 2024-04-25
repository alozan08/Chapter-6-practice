'''
Write a program that takes in a positive integer as input,
and outputs a string of 1's and 0's representing the integer
in reverse binary. For an integer x, the algorithm is:
    As long as x is greater than 0
        Output x modulo 2 (remainder is either 0 or 1)
        Assign x with x divided by 2
    example input: 6
        output: 011

'''
x = int(input("Enter a positive integer: "))
binary = ''
while x > 0:
    binary += str(x % 2)
    x = x // 2
if not(binary == ''):
    print(binary)