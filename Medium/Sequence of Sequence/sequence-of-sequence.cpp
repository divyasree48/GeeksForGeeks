//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    void fun(int i,int m,int n,vector<int>&l,int &c)
    {
        if(l.size()==n)
        {
            c+=1;
            return;
        }
        for(int j=2*i;j<=m;j++)
        {
            l.push_back(j);
            fun(j,m,n,l,c);
            l.pop_back();
        }
    }
    int numberSequence(int m, int n){
        // code here
        int c=0;
        for(int i=1;i<=(m/n);i++)
        {
            vector<int>l;
            l.push_back(i);
            fun(i,m,n,l,c);
        }
        return c;
    }
};

//{ Driver Code Starts.
int main(){
    int t;
    cin>>t;
    while(t--){
        int m, n;
        cin>>m>>n;
        
        Solution ob;
        cout<<ob.numberSequence(m, n)<<endl;
    }
    return 0;
}
// } Driver Code Ends