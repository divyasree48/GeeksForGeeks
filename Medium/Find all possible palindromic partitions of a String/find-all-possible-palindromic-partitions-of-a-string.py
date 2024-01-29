#User function Template for python3

class Solution:
    def allPalindromicPerms(self, s):
        # code here
        def palin(st):
            num=0
            for i in st:
                x=ord(i)-97
                num=num^(1<<x)
            if bin(num)[2::].count('1')<2:
                return 1
            return 0
        k=[]
        def fun(s,i,n,lis):
            if i==n:
                ans=lis.copy()
                k.append(ans)
                return
            for j in range(i,n):
                a=s[i:j+1:]
                if a==a[::-1]:
                    lis.append(a)
                    fun(s,j+1,n,lis)
                    lis.pop()
            return
            
        n=len(s)
        lis=[]
        fun(s,0,n,lis)
        return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        allPart = ob.allPalindromicPerms(S)
        for i in range(len(allPart)): 
            for j in range(len(allPart[i])): 
                print(allPart[i][j], end = " ") 
            print() 
# } Driver Code Ends