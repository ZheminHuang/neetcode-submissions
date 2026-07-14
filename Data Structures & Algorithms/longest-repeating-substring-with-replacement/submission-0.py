class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26

        left = 0
        longest = 0

        for right in range(len(s)):
            right_index = ord(s[right])-ord('A')
            count[right_index]+=1

            while (right-left+1)-max(count)>k:
                left_index = ord(s[left])-ord('A')
                count[left_index]-=1
                left+=1

            current_length = right - left +1
            longest=max(longest,current_length)
        return longest