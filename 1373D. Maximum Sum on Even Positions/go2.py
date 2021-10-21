# -*- coding: utf-8 -*-
'''
Python 3.7.3
[MSC v.1916 64 bit (AMD64)]
24 / 09 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''
from functools import lru_cache

'''

################################################### '''

def solve(nums) -> int:
    '''
    ############################################### '''

    n = len(nums)

    @lru_cache(maxsize=None)
    def matrix(row: int, col: int) -> int:
        ''' Dynamic programming array where row [0, n). and col [0, 2] 
        0: is the best val with no reversing
        1: is the best val with reversing not finished
        2: is the best val with reversing finished
        ############################################### '''

        if row == 0:
            if col == 0:
                return nums[0]
            else:
                return 0

        if row == 1 and col > 0:
            return nums[1]

        if row % 2 == 0:
            # ---------on even possition that can be added if no reversed
            if col == 0:
                # element added
                return matrix(row - 1, col=0) + nums[row]
            elif col == 1:
                # is reversing and the current val is not possible to reverse!
                keepingLast = matrix(row - 1, col=1)

                firstInversion = matrix(row - 2, col=0) + nums[row - 1]
                # if row > 1:
                #     firstInversion = matrix(row - 2, col = 0) + nums[row - 1]
                # else:
                #     firstInversion = nums[1]

                return max(keepingLast, firstInversion)
            else:
                # add the value as has finished the reversing!
                # justFinishedInversion = matrix(row - 1, col = 1) + nums[row]
                justFinishedInversion = matrix(row, col=1)  # + nums[row]
                longAgoFinishedInversion = matrix(row - 1, col=2) + nums[row]

                return max(justFinishedInversion, longAgoFinishedInversion)

        else:
            # ------ odd possition, add in inversions
            if col == 0:
                # the odd element not need to add
                return matrix(row - 1, col=0)
            elif col == 1:
                # add the current to a previous
                firstInversion = matrix(row - 3, col=0) + nums[row]
                # if row > 2:
                #     firstInversion = matrix(row - 3, col = 0) + nums[row]
                # else:
                #     firstInversion = nums[1]

                continuingInversion = matrix(row - 1, col=1) + nums[row]
                # continuingInversion2 = matrix(row - 2, col=1) + nums[row]
                return max(firstInversion, continuingInversion)
            else:
                # finished the inversion!
                # finishingInversion = matrix(row - 2, col=1) + nums[row]
                finishingInversion = matrix(row, col=1)
                finishedInversion = matrix(row - 1, col=2)

                return max(finishingInversion, finishedInversion)

    for i in range(n):
        # bestNoInversion = matrix(i, 0)
        # bestInversing = matrix(i, 1)
        bestInversed = matrix(i, 2)

    bestNoInversion = matrix(n - 1, 0)
    bestInversing = matrix(n - 1, 1)


    # print('----------Matrix')
    # for r in range(n):
    #     print(matrix(r, 0), matrix(r, 1), matrix(r, 2))
    # print('Matrix')

    return max(bestInversed, bestInversing, bestNoInversion)


def main():
    '''
    
    ############################################### '''
    T = int(input())
    for _ in range(T):
        _ = input()

        nums = list(map(int, input().split()))

        resp = solve(nums)
        # print('--', resp)
        print(resp)
    return


if __name__ == "__main__":
    main()
