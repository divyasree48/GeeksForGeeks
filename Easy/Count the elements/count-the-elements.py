#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        b.sort()
        def upper_bound(x,b):
            i=0
            j=n-1
            while i<=j:
                m=(i+j)//2
                if b[m]<=x:
                    i=m+1
                else:
                    j=m-1
            return i
        ans=[]
        for i in query:
            x=a[i]
            c=upper_bound(x,b)
            ans.append(c)
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends