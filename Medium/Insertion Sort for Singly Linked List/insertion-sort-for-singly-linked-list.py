#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def insertionSort(self, head):
        #code here
        if head==None or head.next==None:
            return head
        i=head
        ans=head
        j=head.next
        while(j!=None):
            
            if j.data<i.data:
                
                temp1=ans
                temp=ans
                while(temp.data<j.data):
                    temp1=temp
                    temp=temp.next
                if temp==ans:
                    x=j.next
                    
                    i.next=x
                    
                    j.next=temp
                    ans=j
                    j=i.next
                    
                else:
                    x=j.next
                    i.next=x
                    temp1.next=j
                    j.next=temp
                    j=i.next
            else:
                i=i.next
                j=j.next
        return ans
    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
INF = float("inf")
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = Node(INF)
        nodes = list(map(int, input().strip().split()))
        ptr = a
        for x in nodes:
            ptr.next = Node(INF)
            ptr = ptr.next
            ptr.data = x
        a = a.next
        ob=Solution()
        head = ob.insertionSort(a)
        printList(head)
# } Driver Code Ends