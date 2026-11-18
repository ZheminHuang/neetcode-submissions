class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {ch: set() for word in words for ch in word}

        indegree = {ch: 0 for ch in graph}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            
            for c1,c2 in zip(w1,w2):

                if c1!=c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2]+=1
                    break
        q = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)
        
        result = []

        while q:
            ch = q.popleft()

            result.append(ch)

            for neighbor in graph[ch]:
                indegree[neighbor] -=1

                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(result)!=len(indegree):
            return ""
        
        return "".join(result)