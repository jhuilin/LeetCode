class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if len(arr) <= 0:
            return
        arr = sorted(arr)
        result = []
        current = 0
        min_value = float('inf')
        
        for index in range(len(arr)-1):
            if arr[index+1] - arr[index] < min_value:
                if result:
                    result.clear()
                min_value = arr[index+1] - arr[index]
                result.append([arr[index],arr[index+1]])
            elif arr[index+1] - arr[index] == min_value:
                result.append([arr[index],arr[index+1]])
        return result