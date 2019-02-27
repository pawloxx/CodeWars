"""
Program that will reverse input list
reverse_list([1,2,3,4]) == [4,3,2,1]
reverse_list([3,1,5,4]) == [4,5,1,3]
"""

l = [1, 2, 3, 4]

def reverse_list(l):
    l.reverse()
    return(l)

print(reverse_list(l))