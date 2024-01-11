#User function Template for python3

class Solution:

    def removeKdigits(self, s,k):
        # code here
        l=[]
        for i in range(len(s)):
            if k<=0:
                l.append(s[i])
                continue
            if len(l)==0:
                l.append(s[i])
            else:
                if int(s[i])<int(l[-1]):
                    while(len(l)>0 and k>0):
                        if int(s[i])>=int(l[-1]):
                            break
                        k-=1
                        l.pop()
                    l.append(s[i])
                else:
                    l.append(s[i])
        while(k):
            l.pop()
            k-=1
        if len(l)==0:
            return '0'
        ans=''
        
        for i in l:
            if len(ans)==0 and i=='0':
                continue
            ans+=i
        if len(ans)==0:
            return '0'
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends