#User function Template for python3

# euclidean algo remaining

class Solution:
    def lcmAndGcd(self, A , B):
        mini = min(A,B)
        gcd = 1
        for number in range(1,mini+1):
            if( A % number == 0 and B % number == 0):
                gcd = number
                
        lcm = (A*B)//gcd
        return [lcm,gcd]
        
        
            
        # code here 
