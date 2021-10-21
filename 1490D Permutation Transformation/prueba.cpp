/*
"I find that I don't understand things unless I try to program them.",
"-Donald E. Knuth",

@author: z_tjona
*/

#include <bits/stdc++.h>
#include <numeric> // gcd

using namespace std;
typedef unsigned long long ull;

using vect = vector<int>;

/// \brief solves the problem for array between i, j inclusive
void solve(const vect* vals, vect* depth, int i, int j, int initialDepth = 0)
{
	if (i < 0 || j < 0)
		return;
	if (i > j )
		return;
	if (j >= vals->size())
		return;

	// find max
	auto aux = max_element(vals->begin() + i, vals->begin() + j + 1);
	int x = *aux;
	int idx = distance(vals->begin(), aux);

	depth->at(idx) = initialDepth;
	initialDepth++;
	if (idx == i)
	// only right
		solve(vals, depth, i + 1, j, initialDepth);
		
	
	else if (idx == j)
			//only left
		solve(vals, depth, i, j - 1, initialDepth);
	else
	{
		// left
		solve(vals, depth, i, idx - 1, initialDepth);
		//right
		solve(vals, depth, idx + 1, j, initialDepth);
	}

	return;
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
		cin >> n;
		vect vals;
		vals.reserve(n);

		for (int j = 0; j < n; j++)
		{
			int x;
			cin >> x;
			vals.push_back(x);
		}

		vect depth(n, -1);

		solve(&vals, &depth, 0, n - 1);
		//cout << "resp: ";
		for (int x : depth)
			cout << x << " ";
		cout << endl;
	}
}