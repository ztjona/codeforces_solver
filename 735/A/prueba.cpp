/*
"I find that I don't understand things unless I try to program them.",
"-Donald E. Knuth",

@author: z_tjona
*/

#include <bits/stdc++.h>
#include <numeric> // gcd

using namespace std;
typedef unsigned long long ull;
using vI = vector<int>;

/// \brief solves the problem
int solve(vI *nums)
{

	return 0;
}

/*===========================================================
MAIN
===========================================================*/
int main()
{
	// added the two lines below
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	// loop by case
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int n;
		vI nums;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			int x;
			cin >> x;
			nums.push_back(x);
		}
		cout << solve(&nums) << endl;
	}
}