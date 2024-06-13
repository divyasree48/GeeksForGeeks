#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        # code here 
        if n<3:
            return 1
        a=b=c=1
        for i in range(n-2):
            d=(a+b)%1000000007
            a=b
            b=c
            c=d
        return d%1000000007
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends