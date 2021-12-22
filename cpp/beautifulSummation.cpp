#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std;

typedef long long ll; 

ll power(int a, int b)
{
  ll pow = 1;
  while ( b ) 
  {
         if ( b & 1 ) 
         {
           pow = pow * a;
           --b;
         }
         a = a*a;
         b = b/2;
  }
  return pow;
}

int mod(int a, int m)
{
    return (a%m + m) % m;
}

int main() {
    int P,Q,N,M;
    cin >> P;
    cin >> Q;
    cin >> N;
    cin >> M; 
    
    ll sum = 0;
    ll p_k = 1;
    ll k_q = 1;

    for(ll k=1 ;k<N+1;k++)
        k_q*=power(k,Q);

    for(ll k=1 ;k<N+1;k++){
         p_k = P*p_k;
         sum += p_k ;
    }
    sum*=k_q;
    cout << mod(sum,M) << endl;
    return 0;
}