#User function Template for python3

class Solution:
    def search(self, pattern, text):
        # code here
        k=len(pattern)
        l=[]
        for i in range(len(text)):
            if text[i]==pattern[0]:
                x=text[i:i+k:]
                if x==pattern:
                    l.append(i+1)
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends