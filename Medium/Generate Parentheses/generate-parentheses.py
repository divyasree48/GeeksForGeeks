#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        #code here
        ans=[]
        def fun(openn,close,v,n):
            if openn==n and close==n:
                a=v.copy()
                ans.append("".join(a))
                return
            if openn<n:
                v.append('(')
                fun(openn+1,close,v,n)
                v.pop()
            if close<openn:
                v.append(')')
                fun(openn,close+1,v,n)
                v.pop()
        v=[]   
        fun(0,0,v,n)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends