class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        currentWindow = set()

        i = 0

        for j in range(len(s)):
            while s[j] in currentWindow:
                currentWindow.remove(s[i])
                i += 1
            
            currentWindow.add(s[j])
            maxLength = max(maxLength, j - i + 1)
        
        return maxLength