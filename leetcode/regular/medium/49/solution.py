# https://leetcode.com/problems/group-anagrams/description/

# my initial solution, O(N * k) but highly unoptimized, ends up very slow due to multiple Python-level loops

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            counts = Counter(s)
            key = []
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch in counts:
                    key.append(ch + str(counts[ch]))
            key = ''.join(key)

            groups[key].append(s)
        
        return [group for group in groups.values()]