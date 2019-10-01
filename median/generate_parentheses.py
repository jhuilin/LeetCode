class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        result = []
        self.helper(n,n,"",result)
        return result
        
    def helper(self,left, right, item, result):
        if right < left:
            return
        if right == 0 and left == 0:
            result.append(item)
        if left > 0:
            self.helper(left-1,right,item+"(",result)
        if right > 0:
            self.helper(left,right-1,item+")",result)