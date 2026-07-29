class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        need = Counter(t)
        window = defaultdict(int)

        required = len(need)

        formed = 0
        left = 0

        best_start = 0
        best_length = float("inf")

        for right,char in enumerate(s):
            window[char] +=1

            if char in need and window[char] == need[char]:
                formed +=1

                while formed == required:
                    current_length = right - left + 1

                    if current_length < best_length:
                        best_start = left
                        best_length = current_length

                    left_char = s[left]
                    window[left_char] -= 1
                    left += 1

                    if(left_char in need and window[left_char]<need[left_char]):
                        formed-=1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]    
        