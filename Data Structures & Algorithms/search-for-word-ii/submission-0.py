class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. 建 Trie
        root = TrieNode()

        for word in words:
            cur = root

            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()

                cur = cur.children[ch]

            cur.word = word

        rows = len(board)
        cols = len(board[0])

        result = []

        def dfs(r, c, node):

            ch = board[r][c]

            # 当前字符不在 Trie 里
            if ch not in node.children:
                return

            next_node = node.children[ch]

            # 找到一个完整单词
            if next_node.word is not None:
                result.append(next_node.word)

                # 防止重复加入
                next_node.word = None

            # 标记当前格子已经使用
            board[r][c] = "#"

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] != "#"
                ):
                    dfs(nr, nc, next_node)

            # backtracking
            board[r][c] = ch

        # 2. 每个格子都作为起点
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result