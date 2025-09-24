class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filtered= "".join(ch for ch in s if ch.isalnum() )
        print(filtered)
        return filtered == filtered[::-1]