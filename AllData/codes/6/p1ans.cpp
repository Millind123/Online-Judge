#include <bits/stdc++.h>
using namespace std ;
int main(){
    int n ;
    cin>>n ;
    vector <int> a(n);
    int mx =1e9;
    for (int i =0;i< n ;i++){
        cin>>a[i];
        if (mx > a[i] && a[i]%2==1) mx = a[i];
    }
    cout << mx<<"\n";
    return 0;
}




