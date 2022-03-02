# Coin Change - Dynamic Programming -> https://leetcode.com/problems/coin-change/
def coinChange(coins, amount):
    A = [amount+1] * (amount + 1)
    for i in range(len(A)):
        if i == 0:
            A[i] = 0
            continue
        for y in coins:
            if i - y < 0:
                continue
            A[i] = min(A[i], A[i - y] + 1)
    return A[-1] if A[-1] <= amount else -1


# Maximum Product Subarray - Dynamic Programming -> https://leetcode.com/problems/maximum-product-subarray/
def maxProduct(nums) -> int:
    pre_data = (None, None)
    res = None
    for i, v in enumerate(nums):
        if i == 0:
            pre_data = (v, v)
            res = v
            continue
        x = v * pre_data[0]
        y = v * pre_data[1]
        pre_data = (max(x, y, v), min(x, y, v))
        res = max(pre_data[0], pre_data[1], res)
    return res
        

if __name__ == '__main__':
    print(coinChange([1, 2, 5], 11))
    print(maxProduct([-2,0,-1]))
