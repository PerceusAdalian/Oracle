# Dynamic Programming Techniques in Python

# Fibonacci Sequence (Simple)
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# Knapsack Problem
'''Given a list of weights and values of items, and a maximum capacity, determine the maximum value that can be obtained by selecting items without exceeding the capacity.
Example: weights = [10, 20, 30], values = [60, 100, 120], capacity = 50
Output: 220 (items with weights 20 and 30 are selected)
'''
def knapsack(weights, values, capacity, memo={}):
    if (capacity, len(weights)) in memo:
        return memo[(capacity, len(weights))]
    if capacity <= 0 or not weights:
        return 0
    if weights[-1] > capacity:
        result = knapsack(weights[:-1], values[:-1], capacity, memo)
    else:
        include = values[-1] + knapsack(weights[:-1], values[:-1], capacity - weights[-1], memo)
        exclude = knapsack(weights[:-1], values[:-1], capacity, memo)
        result = max(include, exclude)
    memo[(capacity, len(weights))] = result
    return result

#Longest Common Subsequence (LCS)
'''Given two strings, find the longest subsequence common to both strings. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
Example: str1 = "AGGTAB", str2 = "GXTXAYB"
Output: "GTAB" (length of LCS is 4)
'''
def longest_common_subsequence(str1, str2, memo={}):
    if (str1, str2) in memo:
        return memo[(str1, str2)]
    if not str1 or not str2:
        return ""
    if str1[-1] == str2[-1]:
        result = longest_common_subsequence(str1[:-1], str2[:-1], memo) + str1[-1]
    else:
        left = longest_common_subsequence(str1[:-1], str2, memo)
        right = longest_common_subsequence(str1, str2[:-1], memo)
        result = left if len(left) > len(right) else right
    memo[(str1, str2)] = result
    return result

# Edit Distance (Levenshtein Distance)
'''
Given two strings, determine the minimum number of operations required to transform one string into the other. The allowed operations are insert, delete, and replace.
Example: str1 = "kitten", str2 = "sitting"
Output: 3 (kitten -> sitten -> sittin -> sitting)
'''
def edit_distance(str1, str2, memo={}):
    if (str1, str2) in memo:
        return memo[(str1, str2)]
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)
    if str1[-1] == str2[-1]:
        result = edit_distance(str1[:-1], str2[:-1], memo)
    else:
        insert = 1 + edit_distance(str1, str2[:-1], memo)
        delete = 1 + edit_distance(str1[:-1], str2, memo)
        replace = 1 + edit_distance(str1[:-1], str2[:-1], memo)
        result = min(insert, delete, replace)
    memo[(str1, str2)] = result
    return result

# Coin Change Problem
'''
Given a list of coin denominations and a target amount, determine the number of ways to make the target amount using the given denominations. You can use each denomination an unlimited number of times.
Example: coins = [1, 2, 5], amount = 5
Output: 4 (ways to make 5: 1+1+1+1+1, 1+1+1+2, 1+2+2, 5)
'''
def coin_change(coins, amount, memo={}):
    if (amount, len(coins)) in memo:
        return memo[(amount, len(coins))]
    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0
    include = coin_change(coins, amount - coins[-1], memo)
    exclude = coin_change(coins[:-1], amount, memo)
    result = include + exclude
    memo[(amount, len(coins))] = result
    return result

# Assembler Problem
'''Given a positive integer n, determine the number of ways to assemble n using parts of size 1 to n. Each part can be used multiple times.
Example: n = 4
Output: 8 (ways to assemble 4: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1, 4)
'''
def assembler(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 1
    total = 0
    for i in range(1, n + 1):
        total += assembler(n - i, memo)
    memo[n] = total
    return total

# Example usage
if __name__ == "__main__":
    print("Fibonacci of 10:", fibonacci(10))
    print("Knapsack value:", knapsack([10, 20, 30], [60, 100, 120], 50))
    print("Longest Common Subsequence:", longest_common_subsequence("AGGTAB", "GXTXAYB"))
    print("Edit Distance:", edit_distance("kitten", "sitting"))
    print("Coin Change Ways:", coin_change([1, 2, 5], 5))
