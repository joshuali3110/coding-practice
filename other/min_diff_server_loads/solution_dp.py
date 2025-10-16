from typing import List

def min_diff(loads: List[int]) -> int:
    total = sum(loads)
    dp = [False] * (total // 2 + 1)
    dp[0] = True

    for load in loads:
        for curr in range(total // 2, load, -1):
            dp[curr] = dp[curr] or dp[curr - load]

    for i in range(total // 2, -1, -1):
        if dp[i]:
            print(i)
            return abs(i - abs(total - i))
    
    return total
    

if __name__ == '__main__':
    assert min_diff([1, 2, 3, 4, 5]) == 1
    assert min_diff([5, 8, 1, 4, 6, 10, 3]) == 1