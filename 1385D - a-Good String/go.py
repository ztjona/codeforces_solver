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

'''

################################################### '''



letters = 'abcdefghijklmnopqrstuvwxyz'

def solve(S: str):
    n = len(S)

    
    def count(l, r, c):
        ''' returns count elements with value lettres[c] in S
        ############################################### '''
        resp = 0
        for s in S[l:r]:
            if s == letters[c]:
                resp += 1
        return resp
    
    
    def calc(l: int, r: int, c: int = 0):
        ''' recursive S[l, r) with letters[c]
        ############################################### '''

        if l + 1 == r:
            return int(S[l] != letters[c])
        
        mid = (l + r) // 2
        
        halfElements = (r - l) // 2

        # recursive on the side
        rL = calc(l, mid, c + 1) + halfElements - count(mid, r, c)
        rR = calc(mid, r, c + 1) + halfElements - count(l, mid, c)
        
        return min(rL, rR)

    return calc(0, n)


def main():
    '''
    
    ############################################### '''
    T = int(input())

    for _ in range(T):
        _ = input()
        S = input()

        print(solve(S))

    return


if __name__ == "__main__":
    main()
