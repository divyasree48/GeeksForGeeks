
from typing import List


class Solution:
    
    def getPrimes(self, n : int) -> List[int]:
        # code here
        def sieve(l,n):
            if l[4]==0:
                #print(1)
                return
            l[0]=l[1]=0
            for i in range(2,n):
                if l[i]:
                    j=i*i
                    while(j<n):
                        l[j]=0
                        j+=i
        if n<4:
            return [-1,-1]
        l=[1]*(n+1)
        sieve(l,n+1)
        for i in range(2,n+1):
            a=i
            b=n-i
            if l[a] and l[b]:
                return [a,b]
        return [-1,-1]
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends