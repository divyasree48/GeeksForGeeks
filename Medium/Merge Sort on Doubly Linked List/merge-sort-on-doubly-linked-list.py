#User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''

class Solution():
#Function to sort the given doubly linked list using Merge Sort.
    def sortDoubly(self,head):
        a=[]
        n=0
        while(head!=None):
            a.append(head.data)
            n+=1
            head=head.next
        
        def merge(l,r):
            res=[]
            i=j=0
            while(i<len(l) and j<len(r)):
                if l[i]<=r[j]:
                    res.append(l[i])
                    i+=1
                else:
                    res.append(r[j])
                    j+=1
            while(i<len(l)):
                res.append(l[i])
                i+=1
            while(j<len(r)):
                res.append(r[j])
                j+=1
            return res
        
        def mergesort(a):
            if len(a)<2:
                return a
            mid=len(a)//2
            l=mergesort(a[:mid])
            r=mergesort(a[mid:])
            return merge(l,r)
            
        a=mergesort(a)
        #print(a)
        hea=Node(a[0])
        temp=hea
        for i in range(1,len(a)):
            x=Node(a[i])
            temp.next=x
            x.prev=temp
            temp=x
            #print(temp.data)
        
        t=hea
        c=0
        '''while(t!=None):
            print(t.data)
            t=t.next
            if c==8:
                break
            c+=1'''
        return hea
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while (node is not None):
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while (temp):
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        ob = Solution()
        llist.head = ob.sortDoubly(llist.head)
        printList(llist.head)
        print()

# } Driver Code Ends