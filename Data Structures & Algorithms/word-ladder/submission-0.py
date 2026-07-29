class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 1
        wordList.append(beginWord)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adj[pattern].append(word)
        
        q = deque([beginWord])
        visit = {beginWord}
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord: return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res += 1
        return 0