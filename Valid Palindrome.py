class Solution:
    def isPalindrome(self, s: str) -> bool:
        # process string
        processed_string = ""
        for char in s:
            if char.isalnum():
                processed_string += char.lower()
        
        i, j = 0, len(processed_string) - 1
        
        while i < j:
            if processed_string[i] != processed_string[j]:
                return False
            i += 1
            j -= 1

        return True