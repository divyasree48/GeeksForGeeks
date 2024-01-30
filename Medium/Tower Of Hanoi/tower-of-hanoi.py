# User function Template for python3

class Solution:
    def toh(self, n, fromm, to, aux):
        # Your code here
        def fun(n,a,b,c,cnt):
            if n>0:
                fun(n-1,a,c,b,cnt)
                print("move disk "+str(n)+" from rod "+str(a)+" to rod "+str(c))
                cnt[0]+=1
                fun(n-1,b,a,c,cnt)
        a=fromm
        b=aux
        c=to
        cnt=[0]
        fun(n,a,b,c,cnt)
        return cnt[0]


#{ 
 # Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends