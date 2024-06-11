
from typing import List
from collections import defaultdict
'''
8
4
4
1 4 3 2 7 5 9 6
1 2 3 6 5 4 9 8

7
3
4
8 7 15 19 16 16 18
1 7 15 11 12 31 9

12
11
7
3 6 5 1 9 9 3 7 3 4 6 1
6 6 1 4 5 2 5 1 9 4 9 4
'''

class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        l=[[abs(arr[i]-brr[i]),arr[i],brr[i],i] for i in range(n)]
        l.sort(reverse=True,key=lambda x:x[0])
        a,b,t=0,0,0
        for dif,ta,tb,ind in l:
            if (ta>=tb and a<x) or b>=y:
                t+=ta
                a+=1
            else:
                t+=tb
                b+=1
        return t
        '''a=sorted(arr)
        b=sorted(brr)
        d1=defaultdict(list)
        d2=defaultdict(list)
        d3=defaultdict(list)
        d4=defaultdict(list)
        for i in range(n):
            d1[arr[i]].append(i)
            d2[brr[i]].append(i)
            d3[arr[i]].append(i)
            d4[brr[i]].append(i)
         
        #print(d1)
        c=x
        s1=s=0
        l1=[]
        p1=[]
        for i in range(n-1,-1,-1):
            if c<1:
                break
            ind=d1[a[i]][-1]
            
            if arr[ind]>=brr[ind]:
                s1+=a[i]
                c-=1
                l1.append(ind)
                d1[a[i]].pop()
            else:
                p1.append(i)
        if c>0:
            for i in p1:
                if c<1:
                    break
                ind=d1[a[i]][-1]
                d1[a[i]].pop()
                s1+=a[i]
                c-=1
                l1.append(ind)
            
        d=y
        for i in range(n-1,-1,-1):
            if d<1:
                break
            ind=d2[b[i]][-1]
            
            if ind in l1:
                continue
            else:
                s1+=b[i]
                d2[b[i]].pop()
                l1.append(ind)
                d-=1
        c=y
        s=0
        l=[]
        p=[]
       # print(d3,d4)
        for i in range(n-1,-1,-1):
            if c<1:
                break
            ind=d4[b[i]][-1]
            
            if brr[ind]>=arr[ind]:
                s+=b[i]
                c-=1
                l.append(ind)
                d4[b[i]].pop()
            else:
                p.append(i)
        if c>0:
            for i in p:
                if c<1:
                    break
                ind=d4[b[i]][-1]
                d4[b[i]].pop()
                s+=b[i]
                c-=1
                l.append(ind)
        d=x
        for i in range(n-1,-1,-1):
            if d<1:
                break
            ind=d3[a[i]][-1]
            
            if ind in l:
                continue
            else:
                s+=a[i]
                l.append(ind)
                d3[a[i]].pop()
                d-=1    
        return max(s,s1)'''
            
        



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

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends