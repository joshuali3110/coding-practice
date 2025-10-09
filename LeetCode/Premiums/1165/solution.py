class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mp = {}

        for i in range(26):
            mp[keyboard[i]] = i
        
        pos = 0
        time = 0

        for ch in word:
            next_pos = mp[ch]
            time += abs(next_pos - pos)
            pos = next_pos
        
        return time

if __name__ == '__main__':
    sol = Solution()

    assert sol.calculateTime("abcdefghijklmnopqrstuvwxyz", "cba") == 4
    assert sol.calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode") == 73