# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
# Sum of positive

from functools import reduce

# Time complexity: O(n)
# Space complexity: O(n)
def positive_sum1(arr):
    # Your code here
    return reduce(lambda x, y: x + y, list(filter(lambda x: x>0, arr)), 0)

# Time complexity: O(n)
# Space complexity: O(n)
def positive_sum3(arr):
    # Filter out negative numbers
		return sum(list(filter(lambda x: x > 0, arr)))

# Time complexity: O(n)
# Space complexity: O(n)
def positive_sum4(arr):
    # Filter out negative numbers
		return sum(map(lambda x: x * 0 if x < 0 else x, arr))

# Time complexity: O(n)
# Space complexity: O(n)
def positive_sum(arr):
    # Filter out negative numbers
		return sum(x for x in arr if x > 0)

# Time complexity: O(n)
# Space complexity: O(n)
def positive_sum2(arr):
    # Filter out negative numbers
		arr1 = []
		for i in arr:
			if i > 0:
				arr1.append(i)
		# Sum the list
		sum = 0
		for i in arr1:
			sum += i
		return sum

print(positive_sum([1,2,3,4,5])) # 15
print(positive_sum([1,-2,3,4,5])) # 13
print(positive_sum([-1,2,3,4,-5]))# 9

# returns 0 when array is empty
print(positive_sum([])) # 0

#returns 0 when all elements are negative
print(positive_sum([-1,-2,-3,-4,-5])) # 0