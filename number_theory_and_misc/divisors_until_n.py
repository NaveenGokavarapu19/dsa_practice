class Solution:
    def print_divisors(self, N):
        for index in range(1,N+1):
            if(N%index == 0):
                print(index,end=" ")