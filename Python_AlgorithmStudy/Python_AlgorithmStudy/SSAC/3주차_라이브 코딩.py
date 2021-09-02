

#0816_3주차 라이브 코딩

#둘 모두 완전탐색 알고리즘.
#최악의 경우 모두 탐색하게됨.
#차이점 -> 자료구조의 차이, 탐색 순서, 최단거리 탐색 시 보통 BFS쓴다.


#깊이 우선 탐색 DFS
#스택/재귀를 사용해서 구현한다.
#구현이 BFS보다 좀더 단순한 편.
#단 파이썬으로 구현하면 BFS보다 좀 느림. (재귀함수가 좀 느림.)
#최단거리 탐색에 비효율적 
#  -> 중간에 탈출할 수 없음. + (사이클이 있을 수 있고, 자꾸 재방문을 할 수도 있기때문에)방문체크 해야함.
#

#넓이 우선 탐색 BFS
#큐를 사용해서 구현한다.
#중간에 탈출할 수 있음.
#최단거리 탐색
#얘도 방문체크는 해줘야됨.

#인접행렬로 DFS/BFS 구현했을 때 시간 복잡도: O(V2)
#인접리스트로 DFS/BFS 구현했을 때 시간 복잡도: O(V+E)



#11724 연결요소의 개수
#무방향 그래프
# from typing_extensions import IntVar
# import sys

# sys.setrecursionlimit(10*6) #이부분 수정하기
# N, M = map(int, input().split())
# adj = [[False]*(N+1) for _ in range(N+1)]

# for _ in range(M):
#     a,b = map(int, input().split())
#     adj[a][b] = adj[b][a] = True


# def dfs(now):
#     # print(f'{now}', end=' ')
#     for nxt in range(1, N+1):
#         if now != nxt and adj[now][nxt] and not chk[nxt]:
#             chk[nxt] = True
#             dfs(nxt)


# ans = 0
# chk = [False] *(N+1)
# for i in range(1, N+1):
#     if not chk[i]:
#         chk[i] = True
#         ans+=1
#         # print(f'\nstart: {i}')
#         dfs(i)

# print(ans)

# for i in range(N+1):
#     for j in range(N+1):
#         print(1 if adj[i][j] else 0, end=' ')

#     print()


#2278
#최단거리를 구하는 문제라서 BFS가 아닐까.
# from collections import deque

# dy =(0,1,0,-1)
# dx =(1,0,-1,0)

# N, M = map(int, input().split())
# board = [input() for _ in range(N)]

# def is_valid_coord(y, x):
#     return 0 <= y < N and 0<= x <M

# def bfs(sy, sx):
#     chk = [[False]*M for _ in range(N)]
#     chk[sy][sx] = True

#     dq = deque()
#     dq.append((sy, sx, 1))
#     while dq:
#         y,x,d = dq.popleft()
#         if y == N-1 and x == M-1:
#             return d

#         for k in range(4):
#             ny = y + dy[k]
#             nx = x + dx[k]
#             nd = d + 1
#             if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
#                 chk[ny][nx] = True
#                 dq.append((ny, nx, nd))

# print(bfs(0,0))
