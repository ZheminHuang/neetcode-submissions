class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []

        def dfs(open_count,close_count):
            if open_count ==n and close_count ==n:
                result.append("".join(current))
                return 
            
            if open_count<n:
                current.append("(")
                dfs(open_count+1,close_count)
                current.pop()

            if close_count<open_count:
                current.append(")")
                dfs(open_count,close_count+1)
                current.pop()
        
        dfs(0,0)
        return result