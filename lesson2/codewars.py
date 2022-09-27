# FizzBuzz
# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
#
# Example 1:
#
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
#
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

num = int(input('Enter a number: '))
arr = []
for i in range(1, num + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        arr.append('FizzBuzz')
    elif i % 3 == 0:
        arr.append('Fizz')
    elif i % 5 == 0:
        arr.append('Buzz')
    else:
        arr.append(str(i))
print(arr)

# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         # ans list
#         ans = []
#
#         for num in range(1,n+1):
#
#             divisible_by_3 = (num % 3 == 0)
#             divisible_by_5 = (num % 5 == 0)
#
#             num_ans_str = ""
#
#             if divisible_by_3:
#                 # Divides by 3
#                 num_ans_str += "Fizz"
#             if divisible_by_5:
#                 # Divides by 5
#                 num_ans_str += "Buzz"
#             if not num_ans_str:
#                 # Not divisible by 3 or 5
#                 num_ans_str = str(num)
#
#             # Append the current answer str to the ans list
#             ans.append(num_ans_str)
#
#         return ans

# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         # ans list
#         ans = []
#
#         # Dictionary to store all fizzbuzz mappings
#         fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}
#
#         # List of divisors which we will iterate over.
#         divisors = [3, 5]
#
#         for num in range(1, n + 1):
#
#             num_ans_str = []
#
#             for key in divisors:
#                 # If the num is divisible by key,
#                 # then add the corresponding string mapping to current num_ans_str
#                 if num % key == 0:
#                     num_ans_str.append(fizz_buzz_dict[key])
#
#             if not num_ans_str:
#                 num_ans_str.append(str(num))
#
#             # Append the current answer str to the ans list
#             ans.append(''.join(num_ans_str))
#
#         return ans

# Fibonacci Sequence
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
#
# Example 1:
#
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:
#
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:
#
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
num = int(input('Enter a number: '))
def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    x, y = 0, 1
    for i in range(n):
        x, y = y, y + x
    return x

print(fibonacci(num))

# class Solution:
#     def fib(self, N: int) -> int:
#         if N <= 1:
#             return N
#         return self.fib(N - 1) + self.fib(N - 2)

