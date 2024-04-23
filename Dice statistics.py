import random

statistics = {
    2: '', 3: '', 4: '', 5: '', 6: '',
    7: '', 8: '', 9: '', 10: '', 11: '', 12: ''
}

keep_going = True
roll_total = 0

while keep_going:
    num_rolls = int(input("How many dice rolls? "))
    for i in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'1: {die1} 2: {die2}')
        roll_total = die1 + die2
        if roll_total in statistics:
            statistics[roll_total] += '*'

    response = input("Would you like to roll again? (y/n) ")
    if response == 'n':
        print('Goodbye!')
        keep_going = False
        break

    reset_stats = input('Would you like to reset your stats? (y/n) ')
    if reset_stats == 'y':
        statistics = {
            2: '', 3: '', 4: '', 5: '', 6: '',
            7: '', 8: '', 9: '', 10: '', 11: '', 12: ''
        }

for stat in statistics:
    print(f'{stat}: {statistics[stat]}')







#
#             if roll_total == 2:
#                 total_sums["2"] += '*'
#             if roll_total == 3:
#                 total_sums["3"] += '*'
#             if roll_total == 4:
#                 total_sums["4"] += '*'
#             if roll_total == 5:
#                 total_sums["5"] += '*'
#             if roll_total == 6:
#                 total_sums["6"] += '*'
#             if roll_total == 7:
#                 total_sums["7"] += '*'
#             if roll_total == 8:
#                 total_sums["8"] += '*'
#             if roll_total == 9:
#                 total_sums["9"] += '*'
#             if roll_total == 10:
#                 total_sums["10"] += '*'
#             if roll_total == 11:
#                 total_sums["11"] += '*'
#             if roll_total == 12:
#                 total_sums["12"] += '*'
#     else:
#         print('Invalid number of rolls. Try again.')
#
#     print('\nDice roll statistics:')
#     print('2s:', total_sums["2"])
#     print('3s:', total_sums["3"])
#     print('4s:', total_sums["4"])
#     print('5s:', total_sums["5"])
#     print('6s:', total_sums["6"])
#     print('7s:', total_sums["7"])
#     print('8s:', total_sums["8"])
#     print('9s:', total_sums["9"])
#     print('10s:', total_sums["10"])
#     print('11s:', total_sums["11"])
#     print('12s:', total_sums["12"])
#
#     usr_prompt = input('Continue? Y or N:')
#     if usr_prompt == 'N':
#         exit()
#     reset_stats = input('Reset stats? Y or N:')
#     if reset_stats == 'Y':
#         total_sums = {
#             "2": '', "3": '',
#             "4": '', "5": '',
#             "6": '', "7": '',
#             "8": '', "9": '',
#             "10": '', "11": '',
#             "12": ''
#         }
#         continue
