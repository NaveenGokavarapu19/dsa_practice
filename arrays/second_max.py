#User function Template for python3

from sys import maxsize
class Solution:

    def print2largest(self,arr, n):
        s_maxi = -maxsize
        maxi = -maxsize
        for element in arr:
            if(element > maxi):
                s_maxi = maxi
                maxi = element
            elif (element > s_maxi and element < maxi):
                s_maxi = element
        if (s_maxi == -maxsize):
            return -1
        return s_maxi
            
            





#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends