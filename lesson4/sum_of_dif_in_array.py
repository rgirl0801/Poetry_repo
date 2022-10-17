# https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/train/python

# Time complexity: O(n)
# Space complexity: O(n)
def sum_of_differences2(arr):
    return max(arr) - min(arr) if arr else 0


# Time complexity: O(n)
# Space complexity: O(n)
def sum_of_differences(arr):
    if len(arr) <= 1:
        return 0

    arr.sort(reverse=True)
    diff = []
    for i in range(len(arr)):
        if (i + 1) < len(arr):
            t = abs(arr[i] - arr[i + 1])
            diff.append(t)
    return sum(diff)


print(sum_of_differences([1, 2, 10]), 9)
print(sum_of_differences([-3, -2, -1]), 2)
print(sum_of_differences([1, 1, 1, 1, 1]), 0)
print(sum_of_differences([-17, 17]), 34)
print(sum_of_differences([]), 0)
print(sum_of_differences([0]), 0)
print(sum_of_differences([1]), 0)
print(
    sum_of_differences([-11, -8, -14, 16, 6, 14, -19, -7, 8, 21, -14, -2, 10, 15, 0]),
    36,
)
