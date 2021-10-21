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

'''
https://codeforces.com/problemset/problem/279/B
################################################### '''

from functools import lru_cache
def solve(nums, t:int)->int:
    '''
    ############################################### '''
    n = len(nums)

    maxTam = 0
    
    resp = []
    lastI = -1

    for idx, val in enumerate(nums):
        # loop by initial idx
        if idx == 0:
            suma = 0
        else:
            suma -= nums[idx - 1]

        suma2 = suma
        for idxLast in range(lastI + 1, n):
            # loop by final idx
            suma2 += nums[idxLast]
            if suma2 <= t:
                suma = suma2
                lastI = idxLast
            else:
                break
        tam = lastI - idx + 1
        # resp.append(tam)
        if maxTam < tam:
            maxTam = tam
    return maxTam


def main():
    '''
    
    ############################################### '''
    n, t = list(map(int, input().split()))

    tiempos = list(map(int, input().split()))

    resp = solve(tiempos, t)
    print(resp)
    return


if __name__ == "__main__":
    main()
