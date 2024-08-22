#User function Template for python3

from typing import List

class Solution:
    def findOrder(self, alien_dict: List[str], N: int, K: int) -> str:
        # Your implementation here
        def dfs(ind,adj,vis,st):
            vis[ind]=1
            for i in adj[ind]:
                if vis[i]==0:
                    dfs(i,adj,vis,st)
            st.append(ind)
        adj=[[]for i in range(K)]
        for i in range(N-1):
            a=alien_dict[i]
            b=alien_dict[i+1]
            mini=min(len(a),len(b))
            for j in range(mini):
                if a[j]!=b[j]:
                    adj[ord(a[j])-ord('a')].append(ord(b[j])-ord('a'))
                    break
        vis=[0]*K
        st=[]
        for i in range(K):
            if vis[i]==0:
                dfs(i,adj,vis,st)
        ans=''
        while(len(st)):
            a=chr(st[-1]+ord('a'))
            ans+=a
            st.pop()
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3


class sort_by_order:

    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        s = ""
        for i in range(k):
            s += chr(97 + i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)

            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)

# } Driver Code Ends