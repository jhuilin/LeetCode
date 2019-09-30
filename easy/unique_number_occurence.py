class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result = []
        check = []
        for index in arr:
            if index not in check:
                check.append(index)
                c = arr.count(index)
                if c not in result:
                    result.append(c)
                else:
                    return False
        return True