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

'''
https://codeforces.com/problemset/problem/1514/B
################################################### '''


def powMod(base: int, exponent: int, m: int)->int:
    '''returns base ^e % m
    
    ############################################### '''
    
    resp = 1
    while exponent > 0:
        if exponent %2 == 1:
            # odd
            exponent -= 1
            resp *= base
            resp %= m
        else:
            # even
            base *= base
            base %= m
            exponent //= 2
    
    # resp *= base
    
    return resp % m


m = 1_000_000_000 + 7
def solve(n: int, k: int)->int:
    '''Returns the number of ways an array with k-bits n elements can be formed 
    that the bitwise AND is always zero with max sum.
    ############################################### '''

    return powMod(n, k, m)


def main():
    '''
    
    ############################################### '''
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        resp = solve(n, k)
        print(resp)
    return


if __name__ == "__main__":
    main()
