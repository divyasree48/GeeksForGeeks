#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here 
        a=bin(x)[2::]
        while len(a)<32:
            a='0'+a
        a=a[::-1]
        return int(a,2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends