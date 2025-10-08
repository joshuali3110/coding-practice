from typing import List

def min_diff(loads: List[int]) -> int:
    total = sum(loads)
    res = float('inf')

    def backtrack(curr, idx):
        nonlocal res
        res = min(res, abs(curr - abs(total - curr)))

        if curr >= total // 2:
            return
        
        for i in range(idx, len(loads)):
            backtrack(curr + loads[i], i + 1)
    
    backtrack(0, 0)
    
    return res

if __name__ == '__main__':
    assert min_diff([1, 2, 3, 4, 5]) == 1
    assert min_diff([5, 8, 1, 4, 6, 10, 3]) == 1