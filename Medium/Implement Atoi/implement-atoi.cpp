//{ Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function template for C++

class Solution{
  public:
    /*You are required to complete this method */
    int atoi(string s) {
        //Your code here
        int c=0,j=1;
        for(int i=s.size()-1;i>=0;i--)
        {
            
            if(i==0 and s[i]=='-')
            {
                c*=-1;
                break;
            }
            if(s[i]>=48 and s[i]<=57)
            {
                c+=((s[i]-'0')*j);
                j*=10;
            }
            else
            {
                c=-1;
                break;
            }
        }
        return c;
    }
};

//{ Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		string s;
		cin>>s;
		Solution ob;
		cout<<ob.atoi(s)<<endl;
	}
}
// } Driver Code Ends