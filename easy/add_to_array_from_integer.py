class Solution:
    def addToArrayForm(self, A: List[int], k: int) -> List[int]:
        carry = 0
        n = len(A) - 1
        for i in range(n,-1,-1):
            reminder = k%10
            k //= 10
            A[i] = A[i] + reminder + carry
            if A[i] >= 10:
                A[i] = A[i] - 10
                carry = 1
            else:
                carry = 0
        if carry and k == 0:
            A.insert(0,1)
        elif k > 0:
            k = k + carry
            while k > 0:
                reminder = k % 10
                k //= 10
                A.insert(0,reminder)
        return A
        