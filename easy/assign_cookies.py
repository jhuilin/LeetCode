class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(s) - 1
        m = len(g) - 1
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i<=m and j<=n:
            if g[i] > s[j]:
                j +=1
            else:
                i += 1
                j += 1
        return i