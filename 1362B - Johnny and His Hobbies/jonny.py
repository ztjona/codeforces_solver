# -*- coding: utf-8 -*-
'''
Python 3.7.3
[MSC v.1916 64 bit (AMD64)]
20 / 10 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from datetime import datetime


'''
https://codeforces.com/problemset/problem/1362/B
################################################### '''

def solve(nums)->int:
    '''Returns the resp, -1 when no solution
    ############################################### '''
    n = len(nums)

    resp = set()
    for idx, x in enumerate(nums):
        minSet = set()
        for idx2, y in enumerate(nums):
            if idx == idx2:
                continue
            
            z = x ^ y
            minSet.update([z, ])
        if idx == 0:
            resp = minSet
        else:
            resp.intersection_update(minSet)
        if not resp:
            return -1
    
    return min(resp)


def main():
    '''
    
    ############################################### '''
    T = int(input())
    for _ in range(T):
        _ = input()
        nums = list(map(int, input().split()))
        resp = solve(nums)
        # print('^*\t\t\t\t', resp)
        print(resp)
    return


if __name__ == "__main__":
    main()
