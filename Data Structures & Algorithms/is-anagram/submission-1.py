class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sHash, tHash = {}, {}

        for i in range(len(s)):
            # dictionary.get(keyname, value)
            # keyname: Required. The keyname of the item you want to return the value from
            # value: Optional. A value to return if the specified key does not exist.
            sHash[s[i]] = 1 + sHash.get(s[i], 0)
            tHash[t[i]] = 1 + tHash.get(t[i], 0)
        
        if sHash == tHash:
            return True
        return False


        