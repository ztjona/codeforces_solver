# -*- coding: utf-8 -*-
'''
Python 3.7.3
[MSC v.1916 64 bit (AMD64)]
15 / 10 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

'''
https://codeforces.com/contest/466/problem/C
################################################### '''


def solve(nums) -> int:
    '''Solves the problem first finding the sum, dividing by 3, and then from left to right.
    ############################################### '''
    n = len(nums)

    suma = 0
    for v in nums:
        suma += v
    
    target = suma//3
    # --- 
    if target == suma/3 and n > 2:
        # may be possible

        # ---------- from left
        left = -1 # min indx with the target value
        sumL = 0
        for idx, v in enumerate(nums):
            sumL += v
            if sumL == target:
                left = idx
                break
        
        if left == -1:
            # not reached the target, cannot complete not even this side
            return 0

        # else may possible

        # ---------- from right
        right = -1 # min indx with the target value
        sumR = 0
        for idx in range(n - 1, -1, -1):
            v = nums[idx]
            sumR += v
            if sumR == target:
                right = idx
                break
        
        if right == -1:
            # not reached the target, cannot complete on right side
            return 0

        # ---- both sides!
        if left + 1 < right:
            # a solution!
            # --------- lefts
            leftSols = [left, ]
            delta = 0
            for idxL in range(left + 1, right - 1):
                v = nums[idxL]
                delta += v
                if delta == 0:
                    leftSols.append(idxL)
            
            # --- rights!
            rightSols = [right, ]
            delta = 0
            for idxR in range(right - 1, left + 1, -1):
                v = nums[idxR]
                delta += v
                if delta == 0:
                    rightSols.append(idxR)

            
            def binSearch(lIdx: int):
                '''Returns the number of the right elements that full fills the condition.
                It is always possible at least 1 as the l and r top are possibles
                right elements are decreasing
                n, n-1, .... l
                lIdx > l
                T T T F F
                Returns idx of last true
                ############################################### '''
                
                l = 0
                r = len(rightSols)
                target = lIdx + 2 # from these value
                while l < r:
                    mid = (l + r)//2
                    if target > rightSols[mid]:
                        r = mid
                        mid = left
                    elif target < rightSols[mid]:
                        l = mid + 1
                        # mid = left
                    else:
                        break
                    
                return mid + 1
            
            
            # ------- counting!
            resp = 0
            for l in leftSols:
                resp += binSearch(l)

                # for r in rightSols:
                #     if l + 1 < r:
                #         # leaving a space for the mid array
                #         resp += 1
                #     else:
                #         break
                
            return resp
        else:
            # overlapping!
            return 0
    else:
        # impossible as there is no way to divide by 3
        return 0
    


def main():
    '''
    
    ############################################### '''
    _ = input()

    nums = list(map(int, input().split()))

    resp = solve(nums)
    print(resp)

    return


if __name__ == "__main__":
    main()
