"""
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""

def row_sum_odd_numbers(number):
    start = number ** 2 - (number - 1)
    return sum(range(start, start + number * 2, 2))

print(row_sum_odd_numbers(2))





