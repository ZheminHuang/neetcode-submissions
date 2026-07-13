class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        left=0
        right = 0

        longest = 0

        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left+=1
            char.add(s[right])

            cur_length=right-left+1
            longest=max(longest,cur_length)
        return longest