# -*- coding: utf-8 -*-
'''
Python 3.7.3
[MSC v.1916 64 bit (AMD64)]
09 / 10 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from collections import Counter


'''
https://codeforces.com/problemset/problem/1335/C
################################################### '''

def solve(nums)->int:
    '''
    
    ############################################### '''
    counter = Counter(nums)
    n = len(nums)

    mostCommon = counter.most_common()
    diffs = len(mostCommon)
    for idx, times in mostCommon:
        if diffs - 1 >= times:
            # enough to complete
            return times
        if diffs >= times - 1:
            # needs to pass 1 to the otherside
            return times - 1
        
        elif times > diffs:
            # all the diffs and 1 from the otherside
            return diffs
    return 0


def main():
    '''
    
    ############################################### '''
    T = int(input())

    for _ in range(T):
        _ = input()
        nums = list(map(int, input().split()))
        resp = solve(nums)
        print(resp)
    return


if __name__ == "__main__":
    main()
