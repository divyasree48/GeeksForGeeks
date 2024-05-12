#User function Template for python3

class Solution:
    def minSteps(self, d):
        s=0
        c=0
        while(s<d or (s-d)&1):
            c+=1
            s=s+c
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d = int(input())

        ob = Solution()
        print(ob.minSteps(d))

# } Driver Code Ends