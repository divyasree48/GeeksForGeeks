#User function Template for python3

class Solution:
    
    def CombinationSum2(self, arr, n, k):
        # code here
        arr.sort()
        ans=set()
        def fun(arr,n,k,i,s,cur):
            if s==k:
                ans.add(tuple(cur))
                return
            if i>=n or s>k:
                return
            
            for j in range(i,n):
                if s+arr[j]>k:
                    break
                fun(arr,n,k,j+1,s+arr[j],cur+[arr[j]])
        fun(arr,n,k,0,0,[])
        return sorted(ans)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ob = Solution()
    result = ob.CombinationSum2(arr, n, k)
    for row in result:
        print(*row)
    if not result:
        print()

# } Driver Code Ends