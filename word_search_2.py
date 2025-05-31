class TrieNode:
    def __init__(self):
        self.children={}
        self.endofword=False
    
    def addWord(self,word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]       
        cur.endofword=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        cur=TrieNode()
        for word in words:
            cur.addWord(word)
        rows,cols=len(board),len(board[0])
        res,visited=set(),set()

        def dfs(r,c,node,word):
            if((r<0 or c<0) or 
            (r>=rows or c>=cols) or 
            ((r,c) in visited) or
            (board[r][c] not in node.children)):
                return
            visited.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.endofword:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visited.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,cur,"")

        return list(res) 
            
        