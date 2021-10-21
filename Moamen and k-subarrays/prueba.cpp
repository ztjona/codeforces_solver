/*
01 / 08 / 2021
@author: z_tjona
*/

#include <bits/stdc++.h>
#include <numeric>

using namespace std;
typedef unsigned long long ll;

/// \brief returns the first idx of the given x in the array. Assumes it is sorted
size_t findIdx(vector<int>* vals, int x) {
	int n = vals->size();

	int low = 0;
	int high = n - 1;

	int m = 0;
	size_t idx = 0;
	while (high - low > 0)
	{
		int m = low + (high - low) / 2;
		if (x <= vals->at(m))
		{
			high = m;

			if (x == vals->at(m))
				idx = m;
		}
		else
		{
			low = m + 1;
		}
	}
	return idx;
}

bool solve(vector<int>* nums, int k) {
	
	int n = nums->size();

	if (n < k)
		return false;

	vector<int> numsOrderered(*nums);

	sort(numsOrderered.begin(), numsOrderered.end());

	vector<bool> filled; // in the ordered vector
	filled.reserve(n);
	for (int i = 0; i < n; i++)
		filled.push_back(false);
	

	int kGroups = 0;

	int valsPlaced = 0;

	bool isNewGroup = true;

	vector<size_t> groupSizes;
	
	int lastIdx = -2; // needs to be lower than -1

	for (int x : *nums)
	{// loop by element in nums, ie subarray

		// finding the first possible location of the x val in the sorted array
		size_t idx = findIdx(&numsOrderered, x);

		for (idx; idx < n; idx++)
		{// reaching the first not used
			if (!filled[idx])
				break;
		}

		if (idx != lastIdx + 1)
			isNewGroup = true;

		if (isNewGroup)
		{		
			kGroups++;
			groupSizes.push_back(1);
		}
		else
		{
			groupSizes.back()++;
		}
		
		filled[idx] = true;
		lastIdx = idx;
		
		if (kGroups > k)
			return false;
	}

	return kGroups < k;
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
		int n, k;
		cin >> n >> k;
		vector<int> nums;
		nums.reserve(n);
		for (int j = 0; j < n; j++)
		{
			int v;
			cin >> v;
			nums.push_back(v);
		}
		bool isPossible = solve(&nums, k);

		if (isPossible)
			cout << "Yes" << endl;
		else
			cout << "No" << endl;
	}
}