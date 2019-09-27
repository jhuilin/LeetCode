# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self,root: TreeNode) -> List[float]:
        if root == None:
            return []
        queue = collections.deque()
        result = []
        queue.append(root)
        while queue:
            sum = 0
            num_nodes = len(queue)
            for _ in range(num_nodes):
                current = queue.popleft()
                sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            if num_nodes != 0:
                result.append(sum/num_nodes)
        return result