def count_inversions(n):
    n_len = len(n)
    counter = 0
    for a in range(n_len):
        for b in range(a + 1, n_len):
            if (n[a] > n[b]):
                counter += 1
    return counter

print(count_inversions((1, 2, 3, 5, 7, 4)))


# BEST PRACTICE

def count_inversion(nums):
    return sum(a > b for i, a in enumerate(nums) for b in nums[i + 1:])
