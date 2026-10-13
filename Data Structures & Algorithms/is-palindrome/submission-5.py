class Solution:
    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1
        s = s.lower()

        for i in range(len(s)):
            if not s[head].isalnum():
                head += 1
            elif not s[tail].isalnum():
                tail -= 1
            else:
                if s[head] != s[tail]:
                    return False
                head += 1
                tail -= 1
        
        return True