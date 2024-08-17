#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        ans=[]
        k=0
        p=1
        for i in nums:
            if i==0:
                k+=1
            else:
                p*=i
        for i in nums:
            if k==0:
                ans.append(p//i)
            else:
                if k==1:
                    if i!=0:
                        ans.append(0)
                    else:
                        ans.append(p)
                else:
                    ans.append(0)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends