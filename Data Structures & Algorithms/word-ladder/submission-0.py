class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        beginSet, endSet = set(),set()
        beginSet.add(beginWord)
        endSet.add(endWord)

        length = 1

        #bidirectional bfs
        while beginSet and endSet:
            if len(beginSet)>len(endSet):
                beginSet,endSet = endSet,beginSet

            nxt_set = set()
            for word in beginSet:
                wordLi = list(word)
                for i in range(len(word)):
                    orig = wordLi[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        wordLi[i] = c
                        newWord = ''.join(wordLi)
                        if newWord in endSet:
                            return length+1
                        if newWord in wordSet:
                            nxt_set.add(newWord)
                            wordSet.remove(newWord) #alt way of mark as visited
                    wordLi[i] = orig
            beginSet = nxt_set
            length+=1
        return 0