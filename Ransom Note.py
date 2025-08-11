from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = Counter(magazine)

        for char in ransomNote:
            if char in freq:
                freq[char] -= 1
                if freq[char] < 0:
                    return False
            else:
                return False
        
        return True