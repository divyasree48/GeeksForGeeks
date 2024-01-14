#User function Template for python3
from collections import defaultdict
class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        ans=[]
        
        d={}
        k=-1
        for i in arr:
            s="".join(str(i))
            k+=1
            if s in d:
                d[s]+=1
                ans.append(k)
            else:
                d[s]=1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        arr = []
        for i in range(n):
            nums = list(map(int, input().strip().split()))
            arr.append(nums)
        ob = Solution()
        ans = ob.repeatedRows(arr, n, m)
        
        for x in ans:
            print(x, end=" ")
            
        print()
        tc -= 1

# } Driver Code Ends