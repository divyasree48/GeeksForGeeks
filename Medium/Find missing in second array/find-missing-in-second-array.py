#User function Template for python3


class Solution:
    def findMissing(self,a,b,n,m):
        
        b.sort()
        def find(x):
            i=0
            j=m-1
            while i<=j:
                mid=(i+j)//2
                if b[mid]==x:
                    return 1
                elif b[mid]>x:
                    j=mid-1
                else:
                    i=mid+1
            return 0
        ans=[]
        for i in a:
            if find(i)==0:
                ans.append(i)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
   # n=int(input())
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ob=Solution()
    ans=ob.findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()
# } Driver Code Ends