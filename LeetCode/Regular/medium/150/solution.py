# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                st.append(int(token))
            else:
                op2 = st.pop()
                op1 = st.pop()
                if token == '+':
                    st.append(op1 + op2)
                elif token == '-':
                    st.append(op1 - op2)
                elif token == '*':
                    st.append(op1 * op2)
                else:
                    st.append(int(op1 / op2))
        
        return st.pop()
                    