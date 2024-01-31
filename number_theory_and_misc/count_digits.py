#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        count = 0
        c = N
        while(c!=0):
            digit = c%10
            if(digit == 0):
                c = c//10
                continue
            if(N%digit==0):
                count = count + 1
            c = c//10
        return count
            
