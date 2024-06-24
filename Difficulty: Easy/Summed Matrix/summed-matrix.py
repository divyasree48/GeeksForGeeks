#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
        if q>2*n:
            return 0
        return n-abs((n+1)-q)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends