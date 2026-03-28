class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            node=trie
            for ch in word:
                if ch not in node:
                    node[ch]={}
                node=node[ch]
            node['@']=word
        rows,cols=len(board),len(board[0])
        res=[]
        def dfs(r,c,node):
            ch=board[r][c]
            if ch not in node:
                return
            nextn=node[ch]
            if '@' in nextn:
                res.append(nextn["@"])
                del nextn['@']
            board[r][c]='#'
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols:
                    dfs(nr,nc,nextn)
            board[r][c]=ch
            if not nextn:
                del node[ch]
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,trie)
        return res
        
