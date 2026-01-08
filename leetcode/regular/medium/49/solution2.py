# https://leetcode.com/problems/group-anagrams/description/

# key generation via sorted, O(N * KlogK), but ends up being faster for small K (as in this problem) due to sorted being run in highly optimized C code

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        
        return [group for group in groups.values()]