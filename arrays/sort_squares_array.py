from math import pow

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        for index,element in enumerate(A):
            square = int(pow(element,2))
            A[index] = square
        A.sort()
        return A
            
            
