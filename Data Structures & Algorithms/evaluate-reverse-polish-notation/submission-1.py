class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator={"+","-","*","/"}

        for token in tokens:
            if token not in operator:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == "*":
                    result = left * right
                else:
                    result = int(float((left))/(right))

                    # if (left<0)!=(right<0):
                    #     result = -result
                stack.append(result)
        return stack[-1]