//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
    public:
        int fun(int n)
        {
            if(n<2)return n;
            int maxi=max(n,(fun(n/2)+fun(n/3)+fun(n/4)));
            return maxi;
        }
        int maxSum(int n)
        {
            //code here.
            return fun(n);
        }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        Solution ob;
        cout<<ob.maxSum(n)<<"\n";
    }
    return 0;
}
// } Driver Code Ends