class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackS,stackT = [],[]
        for s in S:
            if s == "#":
                if stackS:
                    stackS.pop()
            else:
                stackS.append(s)
        for t in T:
            if t == "#":
                if stackT:
                    stackT.pop()
            else:
                stackT.append(t)
        return stackT == stackS