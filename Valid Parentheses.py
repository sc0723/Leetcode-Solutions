class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        pairs = {'}' : '{', ')' : '(', ']': '['}

        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if stack:
                    recent_value = stack.pop()
                    if pairs[c] != recent_value:
                        return False
                else:
                    return False
        
        if stack:
            return False
        
        return True