"""
summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
"""

#num = 8
def summation(num):
    sum_list = []
    for i in range(1, num + 1):
        sum_list.append(i)
    return(sum(sum_list))

#print(summation(num))

