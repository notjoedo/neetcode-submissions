class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(n) implementation
        newstr = []

        for i in range(len(s)):
            if (s[i].isalnum()):
                newstr.append(s[i].lower())
        
        head = 0
        tail = len(newstr) - 1

        while head < tail:
            if (newstr[head] != newstr[tail]):
                return False
            head += 1
            tail -= 1
        
        return True
        