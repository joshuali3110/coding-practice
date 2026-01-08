# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# slightly better/more optimized (i think) solution

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []

        for token in tokens:
            if token == '+':
                operands.append(operands.pop() + operands.pop())
            elif token == '-':
                op2 = operands.pop()
                operands.append(operands.pop() - op2)
            elif token == '*':
                operands.append(operands.pop() * operands.pop())
            elif token == '/':
                op2 = operands.pop()
                operands.append(int(operands.pop() / op2))
            else:
                operands.append(int(token))
        
        return operands[0]