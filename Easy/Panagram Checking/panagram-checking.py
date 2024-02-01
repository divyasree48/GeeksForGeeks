#User function Template for python3

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        c=0
        for i in s:
            
            if ord(i)>=65 and ord(i)<=90:
                x=ord(i)-64
                c=c|(1<<x)
            if ord(i)>=97 and ord(i)<=122:
                x=ord(i)-96
            
                c=c|(1<<x)
        
        if bin(c)[2::].count('1')==26:
            return 1
        return 0
            


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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends