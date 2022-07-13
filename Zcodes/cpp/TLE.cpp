#include <bits/stdc++.h>
using namespace std ;
int main(){
    int n ;
    while (1);
    cin>>n ;
    vector <int> a(n);
    int mx =0 ;
    for (int i =0;i< n ;i++){
        cin>>a[i];
        if (mx < a[i])mx = a[i];
    }
    std::cout << mx;
    return 0;
}