# https://leetcode.com/problems/text-justification/description/

class Line:
    def __init__(self, maxWidth):
        self.words = []
        self.num_chars = 0
        self.maxWidth = maxWidth
        self.isLast = False
    
    def add_word(self, word):
        if self.num_chars + len(word) + len(self.words) > self.maxWidth:
            return False
        
        self.words.append(word)
        self.num_chars += len(word)
        return True

    def format(self):
        if self.isLast:
            return " ".join(self.words) + " " * (self.maxWidth - self.num_chars - len(self.words) + 1)
        
        if len(self.words) == 1:
            return self.words[0] + " " * (self.maxWidth - self.num_chars)
        
        formatted = []
        total_spaces = self.maxWidth - self.num_chars
        spaces_per = total_spaces // (len(self.words) - 1)
        extras = total_spaces - (spaces_per * (len(self.words) - 1))

        for i in range(len(self.words) - 1):
            formatted.append(self.words[i])
            formatted.append((" " if extras > 0 else "") + " " * spaces_per)
            extras -= 1
        
        formatted.append(self.words[-1])
        return ''.join(formatted)
        


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = [Line(maxWidth)]

        for w in words:
            if not lines[-1].add_word(w):
                lines.append(Line(maxWidth))
                lines[-1].add_word(w)
        
        lines[-1].isLast = True

        res = []

        for l in lines:
            res.append(l.format())

        return res

        
 