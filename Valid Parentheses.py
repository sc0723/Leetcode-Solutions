class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        pairs = {')' : '(', '}' : '{', ']' : '['}

        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if stack:
                    top = stack.pop()
                    if top != pairs[c]:
                        return False
                else:
                    return False 
        
        if stack:
            return False
        return True