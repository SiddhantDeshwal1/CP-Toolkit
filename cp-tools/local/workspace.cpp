/****************************************************
*                                                  *
        author :  siddhantDeshwal                 
        date   : 25th March 2025, 10:47           
*                                                  *
****************************************************/

#include <algorithm>
#include <chrono>
#include <climits>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;
using ll = signed long long int;

// ;(
struct custom_hash {
  static uint64_t splitmix64(uint64_t x) {
    x += 0x9e3779b97f4a7c15;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
    x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
    return x ^ (x >> 31);
  }

  size_t operator()(uint64_t x) const {
    static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
    return splitmix64(x + FIXED_RANDOM);
  }
};

ll isqrt(ll x) {
  ll val = sqrtl(x) + 5;
  while (val * val > x) val--;
  return val;
};

const ll M = 1e9 + 7;

#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define fl(i, n) for (int i = 0; i < n; i++)
#define in(v) fl(i, v.size()) cin >> v[i];
#define py cout << "YES\n";
#define pm cout << "-1\n";
#define pn cout << "NO\n";
#define pimp cout << "IMPOSSIBLE\n";
#define vr(v) v.begin(), v.end()
#define rv(v) v.end(), v.begin()
#define csort(nums) sort(nums.begin(), nums.end());
#define sum(v) accumulate(v.begin(), v.end(), 0LL);
#define int long long
#define print(x) cout << x << endl ;

typedef vector<ll> vll;
typedef unordered_map<ll, ll, custom_hash> safehash;
typedef vector<vector<int>> mat;

template <typename T>
void printvec(vector<T> v) {
  ll n = v.size();
  fl(i, n) cout << v[i] << " ";
  cout << "\n";
}
template <typename T>
ll sumvec(vector<T> v) {
  ll n = v.size();
  ll s = 0;
  fl(i, n) s += v[i];
  return s;
}

ll gcd(ll a, ll b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
ll lcm(ll a, ll b) {
  return (a / gcd(a, b) * b);
}
ll moduloMultiplication(ll a, ll b, ll mod) {
  ll res = 0;
  a %= mod;
  while (b) {
    if (b & 1) res = (res + a) % mod;
    a = (2 * a) % mod;
    b >>= 1;
  }
  return res;
}
ll powermod(ll x, ll y, ll p) {
  ll res = 1;
  x = x % p;
  if (x == 0) return 0;
  while (y > 0) {
    if (y & 1) res = (res * x) % p;
    y = y >> 1;
    x = (x * x) % p;
  }
  return res;
}
bool isPrime(ll n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;
  for (int i = 5; i * i <= n; i += 6)
    if (n % i == 0 || n % (i + 2) == 0) return false;
  return true;
}

void solve() {
    string s ;
    cin >> s ;

    int ans = s[0] - '0' ;

    for (int i = 1 ; i <= 3 ; i++)
    {
        if (s[i] == '0' || s[i-1] == '0') 
        {
            ans += min(9LL,10LL - (s[i-1] - '0')) + 1 ;
        }
        else ans += abs(s[i-1] - s[i]) + 1 ;
    }
    cout << ans << endl ;
}

int32_t main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int t = 1;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}

