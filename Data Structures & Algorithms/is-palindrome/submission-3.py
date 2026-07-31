class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        # turning into only alphanumeric characters
        for i in range (len(s)):
            if s[i].isalnum():
                newstr += s[i].lower()

        head = 0
        tail = len(newstr) - 1

        while head < tail:
            if (newstr[head] != newstr[tail]):
                return False
            head = head + 1
            tail = tail - 1

        return True