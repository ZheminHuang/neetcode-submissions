class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {"2": "abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}

        result = []
        path = []

        def dfs(index):
            if index == len(digits):
                result.append("".join(path))
                return 
            
            digit=digits[index]

            for char in phone[digit]:
                path.append(char)

                dfs(index+1)

                path.pop()
        
        dfs(0)

        return result