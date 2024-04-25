'''
    When analyzing data sets, such as data for human heights or for human weights,
    a common step is to adjust the data. This adjustment can be done by normalizing
    to values between 0 and 1, or throwing away outliers.
    For this program, adjust the values by dividing all values by the largest value.
    The input begins with an integer indicating the number of floating-point values that follow.
    Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
    print(f'{your_value:.2f}')
        example input:
            5       The 5 indicates that there are five floating-point values in the list
            30.0
            50.0
            10.0
            100.0
            65.0
                    30.0, 50.0, 10.0, 100.0, and 65.0.
                    100.0 is the largest value in the list, so each value is divided by 100.0.
        expected output:
            0.30
            0.50
            0.10
            1.00
            0.65
'''

num_values = int(input("Enter the number of values you'd like to have in your list: "))
counter = 1
num_values_list = []

# collects user values and adds them to a list
while counter <= num_values:
    value = input("Enter your value: ")
    num_values_list.append(float(value))
    counter += 1

# finds the max value of the set
max_val = max(num_values_list)

# calculates each value divided by the largest and stores it in a new list
# prints the value - formatted to 2 decimal places
new_values = []
for val in num_values_list:
    new_val = val / max_val
    new_values.append(new_val)
    print(f'{new_val:.2f}')

