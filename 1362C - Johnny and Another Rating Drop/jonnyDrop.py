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
from functools import lru_cache


'''

################################################### '''

# @lru_cache(maxsize=None)
# def bitDif(n:int)-> int:
#     '''returns the nth value of 
#     https://oeis.org/A001511
#     ############################################### '''
#     if n == 0:
#         return 0
#     if n % 2 == 0:
#         return 1 + bitDif(n/2)
#     else:
#         return 1
    
@lru_cache(maxsize=None)
def solve(n:int)->int:
    '''returns https://oeis.org/A011371
    that has to be added n at the very end
    ############################################### '''
    if n == 0:
        return 0
    return solve(n//2) + n//2




def main():
    '''
    
    ############################################### '''
    # [print(solve(x) + x) for x in range(100)]
    T = int(input())
    for _ in range(T):
        n = int(input())
        resp = solve(n) + n
        print(resp)
    return


if __name__ == "__main__":
    main()
