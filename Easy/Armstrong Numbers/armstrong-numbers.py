#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        a=n
        s=0
        while(n):
            r=n%10
            s+=r*r*r
            n=n//10
        if s==a:
            return 'Yes'
        return 'No'


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends