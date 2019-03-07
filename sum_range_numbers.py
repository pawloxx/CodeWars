# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same


def get_sum(a, b):
    if a < b:
        return sum([i for i in range(a, b + 1)])
    else:
        return sum([i for i in range(b, a + 1)])


print(get_sum(0, -2))