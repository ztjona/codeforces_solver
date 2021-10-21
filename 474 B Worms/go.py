# -*- coding: utf-8 -*-
'''
Python 3.7.3
[MSC v.1916 64 bit (AMD64)]
29 / 09 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

'''
https://codeforces.com/problemset/problem/474/B
################################################### '''

def solve(piles, queries):
# def solve(piles: list[int], queries:list[int]) -> list[int]:
    '''
    
    ############################################### '''
    n = len(piles)
    cumsum = [piles[0], ]

    for x in piles[1:]:
        cumsum.append(cumsum[-1] + x)
    # print(cumsum)

    def binarySearch(val:int)->int:
        '''
        ############################################### '''
        left = 0
        right = n# - 1
        
        while right > left:
            mid = (left + right)//2
            # print(val, ':', left, mid, right)
            if cumsum[mid] > val:
                right = mid
            elif cumsum[mid] < val:
                left = mid + 1
                mid = left
            else:
                break
        

        return mid

    resp = []
    for q in queries:
        resp.append(binarySearch(q) + 1)

    return resp


def main():
    '''
    
    ############################################### '''
    _ = int(input()) # number of piles
    piles = list(map(int, input().split()))

    _ = int(input()) # number of queries
    queries = list(map(int, input().split()))

    resp = solve(piles, queries)
    print(*resp, sep='\n')
    return


if __name__ == "__main__":
    main()
