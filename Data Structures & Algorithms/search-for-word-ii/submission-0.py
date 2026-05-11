class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROW,COL = len(board),len(board[0])
        root = TrieNode()
        for w in words:
            self.addWord(root,w)

        res = []
        def dfs(r,c,node):
            char = board[r][c]
            if char not in node.children:
                return

            nxt_node = node.children[char]
            if nxt_node.word:
                res.append(nxt_node.word)
                nxt_node.word = None

            board[r][c] = '#'
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr,nc = r+dr,c+dc
                if 0<=nr<ROW and 0<=nc<COL and board[nr][nc]!='#':
                    dfs(nr,nc,nxt_node)
            board[r][c] = char

            if not nxt_node.children:
                del node.children[char]
        
        for r in range(ROW):
            for c in range(COL):
                dfs(r,c,root)
        return res


    def addWord(self,root,word):
        cur = root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word