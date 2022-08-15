#취코테 0727

# #입출력
# name = input()
# n = int(input())
# a,b = map(int, input().split())
# print(name, n, a, b)

# #입출력 데이터가 만개 이상으로 많은 경우
# #빠른 입출력 사용
# import sys

# input = sys.stdin.readline
# for _ in range(100000):
#     n = input()


# #리스트 컴프리헨션
# a1 = [3]*8
# a2 = [3 for i in range(8)]
# print(a1)
# print(a2)

# b1 = [*range(8)]
# b2 = [i for i in range(8)]
# print(b1)
# print(b2)

# #삼항 연산자
# #한 줄로 간단하게 나타낼 수 있음.
# a = [2, 4, 7, 5, 1, 8, 6, 3]
# for i in a:
#     even_or_odd = '짝' if i % 2 == 0 else '홀'
#     print(i, even_or_odd)

# b = [1 if j % 2 else 0 for j in a]
# print(b)


# #11866
# N, K = map(int, input().split())
# sitting = [i for i in range(1, N+1)]

# index = 0
# answer = []

# for _ in range(N):
#     index = index + K - 1
#     index = index % len(sitting)
#     answer.append(sitting.pop(index))

# print(f"<{', '.join(map(str, answer))}>")


# #9012
# for _ in range(int(input())):
#     stk = []
#     answer = 'YES'
#     for c in input():
#         if c == '(':
#             stk.append('(')
#         else:
#             if len(stk) > 0:
#                 stk.pop()
#             else:
#                 answer = 'NO'

#     if len(stk) > 0:
#         answer = 'NO'

#     print(answer)


# #2164
# from collections import deque
# dq = deque()
# for i in range(1, int(input())+1):
#     dq.append(i)

# while len(dq) > 1:
#     dq.popleft()
#     dq.append(dq.popleft())

# print(dq.popleft())


# #11286
# import sys, heapq
# hq = []
# for _ in range(int(input())):
#     x = int(sys.stdin.readline())
#     if x == 0:
#         print(heapq.heappop(hq)[1] if len(hq) > 0 else 0)
#     else:
#         heapq.heappush(hq, (abs(x), x))


# #1302
# books = dict()
# for _ in range(int(input())):
#     name = input()
#     if name in books:
#         books[name] += 1
#     else:
#         books[name] = 1

# max_val = max(books.values())
# arr = []
# for k, v in books.items():
#     if v == max_val:
#         arr.append(k)
    
# arr.sort()
# print(arr[0])


#취코테 0728
# #7785

# # import sys
# # input = sys.stdin.readline
# s = set()

# for _ in range(int(input())):
#     name, el = input().split()
#     if el == 'enter':
#         s.add(name)
#     else:
#         if name in s:
#             s.remove(name)

# for name in sorted(s, reverse=True):
#     print(name)


# #5397

# #스택 사용
# for _ in range(int(input())):
#     keystr = list(map(str, input()))
#     stk1 = []
#     stk2 = []
#     for c in keystr:
#         if c == '<' and len(stk1) > 0:
#             stk2.append(stk1.pop())
#         elif c == '>' and len(stk2) > 0:
#             stk1.append(stk2.pop())
#         elif c == '-'and len(stk1) > 0:
#             stk1.pop()
#         elif c.isalpha() or c.isdigit():
#             stk1.append(c)

#     keystr.clear()
#     print(''.join(stk1) + ''.join(reversed(stk2)))

#


# #1935
# # -> 아스키 코드 사용부분, 소숫점 둘째자리 표현하는 프린트 부분
# N = int(input())
# postStr = input()
# stk = []
# val = []
# for _ in range(N):
#     val.append(int(input()))

# for c in postStr:
#     if c.isalpha():
#         c = val[ord(c) - ord('A')]
#         stk.append(c)
#     else:
#         a = stk.pop()
#         b = stk.pop()
#         if c == '+':
#             stk.append(b+a)
#         elif c == '-':
#             stk.append(b-a)
#         elif c == '/':
#             stk.append(b/a)
#         elif c == '*':
#             stk.append(b*a)
        
# print(f'{stk[0]:.2f}')


# #2075
# import heapq
# hq = []
# N = int(input())
# for _ in range(N):
#     for i in map(int, input().split()):
#         if len(hq) >= N:
#             heapq.heappushpop(hq, i)
#         else:
#             heapq.heappush(hq, i)

# print(heapq.heappop(hq))


# # 완전 탐색: 부르트포스. 모든 경우의 수를 탐색하는 방법.
# # 반복문, 재귀, 순열과 조합 사용.

# #순열: n개의 수 중에서 r개를 뽑아 줄을 세우는 경우의 수
# # = 한 리스트 안에서 r개를 뽑아 줄을 세우는 경우의 수. 순서도 고려.
# from itertools import permutations
# arr = [0,1,2,3]
# for i in permutations(arr, 4):
#     print(i)

# #조합: n개의 수 중에서 r개를 뽑는 경우의 수. 순서 상관x.
# # = 한 리스트 안에서 r개를 뽑는 경우의 수.
# from itertools import combinations
# arr = [0,1,2,3]
# for i in combinations(arr, 2):
#     print(i)

# #3040
# from itertools import combinations
# arr = [int(input()) for i in range(9)]

# for i in combinations(arr, 7):
#     if sum(i) == 100:
#         for j in i:
#             print(j)
#         break

# #10448
# def is_possible(T):
#     for j in range(0, i):
#         for k in range(j, i):
#             for l in range(k, i):
#                 if arr[j] + arr[k] + arr[l] == num:
#                     return 1
#     return 0
    
# T = int(input())
# for _ in range(T):
#     arr = []
#     num = int(input())
#     i = 0
#     while i*(i+1)//2 <= num:
#         i+=1
#         arr.append(i*(i+1)//2)
    
#     print(is_possible(T))


# #3085
# N = int(input())
# board = [list(input()) for _ in range(N)]
# ans = 1

# #연속된 노드 세는 부분
# def search():
#     global ans
#     for i in range(N):
#         cnt = 1
#         for j in range(1, N):
            
#             if board[i][j] == board[i][j-1]:
#                 cnt += 1
#                 ans = max(ans, cnt)
#             else:
#                 cnt = 1
        
#     for j in range(N):
#         cnt = 1
#         for i in range(1, N):
            
#             if board[i][j] == board[i-1][j]:
#                 cnt += 1
#                 ans = max(ans, cnt)
#             else:
#                 cnt = 1



# #두 노드 교환 부분
# #오른쪽 / 아래
# #인덱스 범위 주의
# for i in range(N):
#     for j in range(N):
#         if j+1 < N:
#             #두 노드 교환
#             board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

#             #연속된 노드 세주고
#             search()

#             #원상복귀
#             board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        
#         if i+1 < N:
#             #두 노드 교환
#             board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

#             #연속된 노드 세주고
#             search()

#             #원상복귀
#             board[i][j], board[i+1][j] = board[i+1][j], board[i][j]


# print(ans)


# #1931
# import sys

# input = sys.stdin.readline
# meetings = []
# for _ in range(int(input())):
#     start, end = map(int, input().split())
#     meetings.append((end, start))

# #종료시간 순으로 정렬
# meetings.sort()
# t = 0
# ans = 0
# for end, start in meetings:
#     if t <= start:
#         t = end
#         ans += 1

# print(ans)


# #1449
# N, L = map(int, input().split())
# ary = list(map(int, input().split()))
# ary.sort()
# inter = []
# for i in range(len(ary)-1):
#     inter.append(ary[i+1]-ary[i])

# cnt = 0
# ans = 0

# for v in inter:
#     if cnt + v <= L-1:
#         cnt += v
#     else:
#         cnt = 0
#         ans += 1


# print(ans+1)


# #11724
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# N, M = map(int, input().split())
# adj = [[False]*(N+1) for _ in range(N+1)]
# for _ in range(M):
#     u, v = map(int, input().split())
#     adj[u][v] = True
#     adj[v][u] = True

# print(adj)
# ans = 0
# chk = [False]*(N+1)

# def dfs(i):
#     for j in range(1, N+1):
#         if adj[i][j] == True and chk[j] == False:
#             chk[j] = True
#             dfs(j)

# for i in range(1, N+1):
#     if chk[i] == False:
#         ans += 1
#         chk[i] = True
#         dfs(i)


# print(ans)
# print(chk)


# #2178
# from collections import deque

# dy = (0, 1, 0, -1)
# dx = (1, 0, -1, 0)

# N, M = map(int, input().split())

# board = [input() for _ in range(N)]
# chk = [[False]*M for _ in range(N)]

# dq = deque()
# dq.append((0,0,1))
# chk[0][0] = True

# def is_valid_coord(y, x):
#     return 0<=y<N and 0<=x<M

# while len(dq)>0:
#     y, x, d = dq.popleft()
#     if y == N-1 and x == M-1:
#         print(d)
#         break

#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         nd = d + 1

#         if is_valid_coord(ny,nx) and not chk[ny][nx] and board[ny][nx] == '1':
#             chk[ny][nx] = True
#             dq.append([ny, nx, nd])


# #1987
# from collections import deque

# dy = (0, 1, 0, -1)
# dx = (1, 0, -1, 0)

# R, C = map(int,input().split())
# board = [input() for _ in range(R)]

# #백트래킹을 위한 chk.
# #set을 C*R개 만든다.
# chk = [[set() for _ in range(C)] for _ in range(R)]
# # print(chk)

# dq = deque()
# dq.append((0,0, board[0][0]))
# chk[0][0].add(board[0][0])
# ans = 0

# def is_valid_coord(y, x):
#     return 0<=y<R and 0<=x<C

# while dq:
#     y, x, s = dq.popleft()
#     ans = max(ans, len(s))

#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if is_valid_coord(ny, nx) and board[ny][nx] not in s:
#             ns = s + board[ny][nx]
#             #경로에 있는 알파벳이 같은 경우를 제외시킨다.
#             if ns not in chk[ny][nx]:
#                 chk[ny][nx].add(ns)
#                 dq.append((ny, nx, ns))

# print(ans)


# #1743
# from collections import deque
# import sys

# input = sys.stdin.readline

# dy = (0, 1, 0, -1)
# dx = (1, 0, -1, 0)

# N, M, K = map(int, input().split())
# board = [['.']*M for _ in range(N)]
# chk = [[False]*M for _ in range(N)]
# for _ in range(K):
#     y, x = map(int, input().split())
#     board[y-1][x-1] = '#'

# ans = 0


# def is_valid_coord(y, x):
#     return 0<=y<N and 0<=x<M

# def bfs(y, x):
#     dq = deque()
#     dq.append((y,x))
#     chk[y][x] = True
#     sz = 1

#     while dq:
#         y, x = dq.popleft()
#         # print(ans)

#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]

#             if is_valid_coord(ny, nx):

#                 if board[ny][nx] == '#' and not chk[ny][nx]:
#                     sz = sz + 1
#                     dq.append((ny, nx))
#                     chk[ny][nx] = True
                
        
#     return (1 if sz == 0 else sz)

        
# for i in range(N):
#     for j in range(M):
#         if board[i][j] == '#' and not chk[i][j]:
#             ans = max(ans, bfs(i, j))

# print(ans)


# #7562
# from collections import deque

# dy = (2,1,2,1,-2,-1,-2,-1)
# dx = (1,2,-1,-2,-1,-2,1,2)

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     board = [[0]*N for _ in range(N)]

#     start_y, start_x = map(int, input().split())
#     board[start_y][start_x] = 1
#     end_y, end_x = map(int, input().split())

#     dq = deque()
#     dq.append((start_y, start_x, 0))

#     def is_valid_coord(y, x):
#         return 0<=y<N and 0<=x<N

#     while dq:
#         y, x, d = dq.popleft()
        

#         if y == end_y and x == end_x:
#             print(d)
#             break

#         for i in range(8):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             nd = d + 1
#             if is_valid_coord(ny, nx) and board[ny][nx] == 0:
#                 board[ny][nx] = 1
#                 dq.append((ny, nx, nd))


#9663
# 다시 풀어보기


# # 이분탐색
# # 3 위치 찾기
# a = [2,3,6,6,8,12]
# left = 0
# right = len(a)-1
# mid = (left + right) // 2

# while left <= right:
#     if a[mid] == 3:
#         print(f'a[{mid}] = 3')
#         break
#     elif a[mid] > 3:
#         right = mid - 1
#     else:
#         left = mid + 1

#     mid = (left + right) // 2


# # 이분탐색 관련 라이브러리
# from bisect import bisect_left, bisect_right

# a = [2,3,6,6,6,10,12,15]
# l = bisect_left(a, 6) # -> 가장 왼쪽 6의 인덱스를 반환, 2
# r = bisect_right(a, 6) # -> 가장 오른쪽 6의 그 다음 인덱스를 반환, 5
# print(l)
# print(r)
# print(r-l)
# print("-----")
# l = bisect_left(a, 10) # -> 가장 왼쪽 10의 인덱스를 반환, 5
# r = bisect_right(a, 10) # -> 가장 오른쪽 10의 그 다음 인덱스를 반환, 6
# print(l)
# print(r)
# print(r-l)


# #2805
# N, M = map(int, input().split())
# tree = list(map(int, input().split()))

# low = 0
# high = max(tree)
# mid = (low + high) // 2

# def get_total_tree(h):
#     ret = 0
#     for t in tree:
#         if t > h:
#             ret += t - h
#     return ret

# ans = 0
# while low <= high:
#     if get_total_tree(mid) >= M:
#         ans = mid
#         low = mid + 1
#     else:
#         high = mid - 1

#     mid = (low + high) // 2

# print(ans)


# # 10816
# # # 1. 라이브러리 이용하는 방법
# # from bisect import bisect_left, bisect_right

# # N = int(input())
# # cards = sorted(list(map(int, input().split())))
# # M = int(input())
# # ans = []
# # for i in map(int,input().split()):
# #     ans.append(bisect_right(cards, i) - bisect_left(cards, i))

# # print(' '.join(map(str, ans)))

# # # 2. 자료구조(딕셔너리) 이용하는 방법
# # N = int(input())
# # cards = {}
# # for num in map(int,input().split()):
# #     if num in cards:
# #         cards[num] += 1
# #     else:
# #         cards[num] = 1

# # M = int(input())
# # ans = []
# # for i in map(int, input().split()):
# #     if i in cards:
# #         ans.append(cards[i])
# #     else:
# #         ans.append(0)

# # print(' '.join(map(str, ans)))



# # 동적계획법(Dynamic Programming)
# # 피보나치 수열 구현하기

# # 1. 재귀함수만 사용하는 방법
# def f(n):
#     if n < 2:
#         return n

#     return f(n-1)+f(n-2)


# # 2. 메모이제이션(Memoization) 사용하는 방법; 
# # 한번 구한 문제의 답을 따로 저장해두고, 같은 함수가 호출되면 연산 없이 그 값을 이용하는 것. 
# cache = [-1] * 37
# def f(n):
#     if cache[n] != -1:
#         return cache[n]

#     cache[n] = n if n < 2 else f(n-1)+f(n-2)
#     return cache[n]
# print(f(36))


# # 3. 타뷸레이션(Tabulation) 사용하는 방법; 연산을 전부 먼저 시행하여 결과값들을 저장해두고 필요한 결과를 가져가기.
# fibo = [-1] * 37
# def f(n):
#     for i in range(n):
#         fibo[i] = i if i < 2 else fibo[i-1]+fibo[i-2]
# print(f(36))


# #1463
# # import sys
# # sys.setrecursionlimit(10**6)

# # N = int(input())
# # INF = 987654321
# # cache = [INF] * (N+1)
# # cache[1] = 0

# # def dp(x):
# #     if cache[x] != INF:
# #         return cache[x]

# #     if x % 6 == 0:
# #         cache[x] = min(dp(x//3), dp(x//2)) + 1
# #     elif x % 3 == 0:
# #         cache[x] = min(dp(x//3), dp(x-1)) + 1
# #     elif x % 2 == 0:
# #         cache[x] = min(dp(x//2), dp(x-1)) + 1
# #     else:
# #         cache[x] = dp(x-1) + 1 

# #     return cache[x]

# # print(dp(N))

# # BFS로 풀어보기
# from collections import deque

# N = int(input())
# chk = [False] * (N+1)
# chk[N] = True
# dq = deque()
# dq.append((N, 0))

# while dq:
#     x, d = dq.popleft()
#     if x == 1:
#         print(d)
#         break

#     if x % 3 == 0 and not chk[x//3]:
#         dq.append((x//3, d+1))
#         chk[x//3] = True

#     if x % 2 == 0 and not chk[x//2]:
#         dq.append((x//2, d+1))
#         chk[x//2] = True

#     if not chk[x-1]:
#         dq.append((x-1, d+1))
#         chk[x-1] = True


#11726
# dp -> 가짓수를 나누고 점화식을 구한다.
# 메모이제이션을 잊지 않는다.
import sys
sys.setrecursionlimit(10**6)

N = int(input())
cache = [0] * (N+1)

def f(n):
    if cache[n] != 0:
        return cache[n]

    if n <= 2:
        cache[n] = n
    else:
        cache[n] = (f(n-1) + f(n-2))%10007

    return cache[n]

print(f(N))
