class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                newNode = TrieNode()
                cur.children[c] = newNode
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(i,root):
            cur = root

            for j in range(i,len(word)):
                c = word[j]
                if c=='.':
                    for node in cur.children.values():
                        if dfs(j+1,node):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end
        return dfs(0,self.root)

                

