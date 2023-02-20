from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        res, trie, has = list(), dict(), set()

        for r in range(m):
            for c in range(n - 1):
                has.add(board[r][c] + board[r][c + 1])
        for r in range(m - 1):
            for c in range(n):
                has.add(board[r][c] + board[r + 1][c])

        for word in words:
            for i in range(len(word) - 1):
                a, b = word[i], word[i + 1]
                if a + b not in has and b + a not in has:
                    break
            else:
                cur = trie
                for c in word:
                    if c not in cur: cur[c] = {}
                    cur = cur[c]
                cur['*'] = word

        def dfs(r, c, node):
            node = node[board[r][c]]
            if '*' in node:
                res.append(node['*'])
                del node['*']
            rc = board[r][c]
            board[r][c] = '*'
            for i, j in (0, 1), (1, 0), (0, -1), (-1, 0):
                dr, dc = r + i, c + j
                if dr < 0 or dr >= m or dc < 0 or dc >= n \
                        or board[dr][dc] not in node:
                    continue
                dfs(dr, dc, node)
                if len(node[board[dr][dc]]) == 0:
                    del node[board[dr][dc]]
            board[r][c] = rc

        for r in range(m):
            for c in range(n):
                if board[r][c] in trie:
                    dfs(r, c, trie)

        return res