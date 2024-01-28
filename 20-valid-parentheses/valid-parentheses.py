class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return 0
        
        stack = []

        for c in s:
            if c in '({[':
                stack.append(c)
            
            else:
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        
        return not stack
        
        