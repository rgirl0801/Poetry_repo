# Time complexity: O(n)
# Space complexity: O(n)
# Not in place
# https://www.codewars.com/kata/52597aa56021e91c93000cb0/python
def move_zeros2(lst):
    arr1 = list(filter(lambda x: x != 0, lst))
    arr2 = list(filter(lambda x: x == 0, lst))

    return arr1 + arr2 if len(arr1) > 0 else arr2


# Time complexity: O(n)
# Space complexity: O(n)
# In place
# https://leetcode.com/problems/move-zeroes/
def move_zeros(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1

    return arr


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
# [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
print(
    move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
)  # 9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(move_zeros([0, 0]))  # [0, 0]
print(move_zeros([0]))  # [0]
print(move_zeros([]))  # []
