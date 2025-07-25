class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right] 
        
        longest = ""
        for i in range(len(s)):
            even = expand_from_center(i, i+1)
            odd = expand_from_center(i, i)

            if len(even) > len(longest):
                longest = even
            elif len(odd) > len(longest):
                longest = odd
        
        return longest
