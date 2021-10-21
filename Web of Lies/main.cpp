/*
01 / 08 / 2021
@author: z_tjona
*/

#include <bits/stdc++.h>
#include <numeric>

typedef unsigned long long ll;
using namespace std;

double solve(vector<int>* nums) {
	sort(nums->begin(), nums->end(), greater<int>()); // descending order

	double sum1 = (double)nums->at(0);
	double sum2 = (double)nums->at(1);
	double mean1 = (double)nums->at(0);
	double mean2 = (double)nums->at(1);

	double solution = 0;

	int size1 = 1;
	int size2 = 1;

	for (int i = 2; i < nums->size(); i++)
	{
		double v = (double)nums->at(i);

		// in the first group
		double tempSum1 = sum1 + v;
		double tempMean1 = tempSum1 / (size1 + 1);
		double tempSol1 = tempMean1 + mean2;

		double tempSum2 = sum2 + v;
		double tempMean2 = tempSum2 / (size2 + 1);
		double tempSol2 = tempMean2 + mean1;

		if (tempSol1 > tempSol2)
		{
			mean1 = tempMean1;
			size1++;
			sum1 = tempSum1;
			solution = tempSol1;
		}
		else
		{
			mean2 = tempMean2;
			size2++;
			sum2 = tempSum2;
			solution = tempSol2;
		}
	}

	return solution;
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
	{//test case
		int n;
		cin >> n;
		vector<int> nums;
		for (int j = 0; j < n; j++)
		{
			int v;
			cin >> v;
			nums.push_back(v);
		}

		double resp = solve(&nums);

		printf("%.9f\n", resp);
	}

}