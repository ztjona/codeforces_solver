# -*- coding: utf-8 -*-
'''
Python 3.7.3
[MSC v.1916 64 bit (AMD64)]
13 / 09 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''


'''https://codeforces.com/problemset/problem/1373/D
################################################### '''

def solve(nums: list[int])->int:
    '''
    
    ############################################### '''
    n = len(nums)
    
    baseVal = sum(nums[::2]) # result if no inversion. This can increase if gain is possitive

    def findMidInversion(l:int, mid: int, r:int)-> (int, int, int):
        '''Returns the indexes and the max gain from inverting the current array in the middle.
        That includes the middle
        ############################################### '''

        assert (l < mid < r)

        if mid % 2 == 0:
            gain = nums[mid - 1] - nums[mid]
        else:
            gain = nums[mid] - nums[mid - 1]
        
        lInv = mid - 1
        rInv = mid + 1

        if r <= l + 3: # 2 or 3 elements, l and mid inverted
            # base case, swap [l, mid]
            return lInv, rInv, gain
        
        if not (r >= l + 3): # too small
            assert(False)
            return l, l + 1, 0

        
        tempGain = gain
        for i in range(rInv + 1, r, 2):
            if i % 2 == 0:
                miniGain = nums[i - 1] - nums[i]
            else:
                miniGain = nums[mid] - nums[mid - 1]
            
            tempGain += miniGain

        
            if tempGain > gain:
                gain = tempGain
                idxR = i
        
        idxL = l
        tempSum = sumaInverted
        for i in range(l, mid):
            if i% 2 == 1:
                # 
                tempSum += nums[i]
                if tempSum > sumaInverted:
                    sumaInverted = tempSum
                    idxL = i
        
        baseSum = sum(nums[l:r])

        gain = baseSum - sumaInverted

        return idxL, idxR, gain
    
    
    def maxInversion(l, r):
        '''recursively returns indexes and max gain from inverting a portion of the array[l, r)
        ############################################### '''
        if l + 1 == r:
            return l, r, 0
        
        if l + 2 == r:
            if l % 2 == 0:
                idxInverted = l + 1
                idxNoInv = l
            else:
                idxInverted = l
                idxNoInv = l + 1
            gain = nums[idxInverted] - nums[idxNoInv]
            return l, r, gain
        
        # is on the right??, on the left, on the middle?
        mid = l + (r - l) // 2
        
        rI, rJ, rGain = maxInversion(l, mid)
        lI, lJ, lGain = maxInversion(mid, r)
        mI, mJ, mGain = findMidInversion(l, mid, r)

        if rGain >= lGain and rGain >= mGain:
            return rI, rJ, rGain
        elif lGain >= rGain and lGain >= mGain:
            return lI, lJ, lGain
        else:
            return mI, mJ, mGain

    # ----------------- solve func
    i, j, gain = maxInversion(0, n)

    if gain > 0:
        baseVal += gain
        i = 0
        j = n
    return i, j, baseVal


def main():
    '''
    ############################################### '''
    T = int(input())

    for _ in range(T):
        _ = input()
        nums = list(map(int, input().split()))
        resp = solve(nums)
        print('resp: ', resp[2])
    return


if __name__ == "__main__":
    main()
 