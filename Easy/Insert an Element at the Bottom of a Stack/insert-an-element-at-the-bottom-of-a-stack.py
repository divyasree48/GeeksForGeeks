#User function Template for python3
class Solution:
    def insertAtBottom(self,st,x):
        # code here
        s=[]
        while(len(st)):
            a=st[-1]
            st.pop()
            s.append(a)
        st.append(x)
        while(len(s)):
            a=s[-1]
            s.pop()
            st.append(a)
        return st


#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        n,x = map(int,input().split())
        stack = list(map(int,input().split()))
        obj = Solution()
        ans = obj.insertAtBottom(stack,x)
        for e in ans:
            print(e,end=" ")
        print()
        
        
        
# } Driver Code Ends