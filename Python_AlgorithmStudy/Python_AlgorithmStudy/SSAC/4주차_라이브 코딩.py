

#0823_4주차 라이브 코딩
# 콤비네이션 두번 사용해서
# 49Ck, kC6
# 가능한 경우의 수를 출력하기

# from itertools import combinations

# tc = 0
# while True:
#     #맨 앞 숫자와 나머지를 리스트로 받는 방법
#     k, *S = list(map(int, input().split()))
#     #이렇게도 가능
#     # k, *S, a  = list(map(int, input().split()))
#     # print(k, S)

#     if k== 0:
#         break

#     if tc:
#         print()


#     for combi in combinations(S, 6):
#         print(*combi)
    
#     tc += 1



#dfs로 2번까지만 찾으면되지않을까 x 불가능.
# 아 오키
# depth가 정해져있고 경로에 따라 같은 값의 depth가 달라지는 경우 bfs로만 풀수있다.

# from collections import deque
# import sys
# input = sys.stdin.readline
# n = int(input())
# m = int(input())


# #인접리스트
# adj = [[]for _ in range(n+1)]

# for _ in range(m):
#     a,b = map(int, input().split())
#     adj[a].append(b)
#     adj[b].append(a)

# chk = [False] *(n+1)
# chk[1] = True
# dq = deque()
# dq.append((1,0))
# while dq:
#     now, d = dq.popleft()
#     if d < 2:
#         for nxt in adj[now]:
#             if not chk[nxt]:
#                 chk[nxt] = True
#                 dq.append((nxt, d+1))

# print(chk.count(True) - 1)



#개념은 '그리디'이나, 시뮬레이션으로 풀면 시간초과 발생함.
#공식 이용해서 푸는 것이 좋겠음.
# tc = 0
# while True:
#     L, P, V = map(int, input().split())
#     if L == 0 and P == 0 and V == 0:
#         break

#     tc += 1
#     a = V // P
#     b = V % P
#     if b >= L:
#         print("Case {0}: {1}".format(tc, (L*a + L)))
#     else:
#         print("Case {0}: {1}".format(tc, (L*a + b)))

#     # print(f'Case {0}: {1}'.format(tc, min...))





#맨 앞 탑은 0이 될 수밖에 없음.
# from itertools import product
# from sys import stdin


# N = int(input())
# stk = []
# ans = []
# h = list(map(int, input().split()))

# #인덱스와 벌류를 동시에 보여주는 아이 enumerate
# for i, v in enumerate(h):

#     while stk and stk[-1][1] < v:
#         stk.pop

#     ans.append(stk[-1][0] if stk else 0)
#     stk.append((i+1,v))


# print(*ans)
    


# #각각의 집에서 모든 치킨집에 대하여 거리를 구한 후 그 거리들을 저장한다.
# #그 후 조합 사용해서 합이 최소가 되는 조합을 찾는다.
# #완탐/조합!
# from itertools import combinations

# N, M = map(int, input().split())

# houses = []
# chickens = []
# for i in range(N):
#     for j,v in enumerate(map(int, input().split())):
#         if v == 1:
#             houses.append((i,j))
#         elif v == 2:
#             chickens.append((i,j))


# def get_dist(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])

# #상한 생각하기
# ans = len(houses) * 2 * N
# for combi in combinations(chickens, M):
#     tot = 0
#     for house in houses:
#         tot += min(get_dist(house, chicken) for chicken in combi)

#     if ans > tot:
#         ans = tot

# print(ans)




# #최소한의 동작으로 도착지점까지 가야되므로 bfs
# #최소한의 동작으로 가려면 말의 움직임을 최대한 사용해서 가면 됨.

# #말의 움직임을 최대한 사용해서 bfs를 이용해서 풀면 될것 같음.
# #말의 움직임을 사용할 순서는? -> 3차원으로 만들어서 능력을 사용한 횟수를 저장한다.

# from collections import deque

# dy = (0,1,0,-1, -2,-1,1,2,2,1,-1,-2)
# dx = (1,0,-1,0, 1)

# K = int(input())
# W, H = map(int, input().split())

# board = [input().split() for _ in range(H)]

# def is_valid_coord(a, b):


# def bfs():
#     chk =[[[False]*(K+1) for _ in range(W)] for _ in range(H)]
#     chk[0][0][0] = True
#     dq = deque()
#     dq.append((0,0,0,0))
#     while dq:
#         y, x, k, d = dq.popleft()
#         if y==H-1 and x == W-1:
#             return d

#         nd = d +1
#         nk = k
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if is_valid_coord(ny, nx) and board[ny][nx] == '0' and not chk[ny][nx][nk]:
#                 chk[ny][nx][nk] = True
#                 dq.append((ny,nx,nk,nd))


#             if k < K:
#                 nk = k + 1
#                 for i in range(4, 12):
#                     ny = y + dy[i]
#                     nx = x + dx[i]
#                     if is_valid_coord(ny, nx) and board[ny][nx] == '0' and not chk[ny][nx][nk]:
#                         chk[ny][nx][nk] = True
#                         dq.append((ny,nx,nk,nd))

#     return -1


# print(bfs())




#기업 코테 대비하기->
#나동빈 코딩테스트
#https://book.naver.com/bookdb/book_detail.nhn?bid=16439154


