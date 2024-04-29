'''
    Write a function driving_cost() with input parameters miles_per_gallon, dollars_per_gallon, and miles_driven,
    that returns the dollar cost to drive those miles. All items are of type float. The function called with
    arguments (20.0, 3.1599, 50.0) returns 7.89975.
    Define that function in a program whose inputs are the car's miles per gallon and the price of gas in
    dollars per gallon (both float). Output the gas cost for 10 miles, 50 miles, and 400 miles, by calling
    your driving_cost() function three times.
    Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
    print(f'{your_value:.2f}')
    Ex: If the input is:
        20.0
        3.1599
    the output is:
        1.58
        7.90
        63.20
    Your program must define and call a function:
    def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven)
'''

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    miles_cost = (dollars_per_gallon * miles_driven) / miles_per_gallon
    return miles_cost

if __name__ == '__main__':
    mpg = float(input('Miles per gallon: '))
    dollars_per_gallon = float(input('Dollars per gallon: '))
    # cost for 10 miles
    cost_ten = driving_cost(mpg, dollars_per_gallon, miles_driven=10)
    # cost for 50 miles
    cost_fifty = driving_cost(mpg, dollars_per_gallon, miles_driven=50)
    # cost for 400 miles
    cost_four_hundred = driving_cost(mpg, dollars_per_gallon, miles_driven=400)

    print(f'{cost_ten:.2f}')
    print(f'{cost_fifty:.2f}')
    print(f'{cost_four_hundred:.2f}')