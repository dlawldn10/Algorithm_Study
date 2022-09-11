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

# # 재귀함수 사용 -> 하향식 접근(Top-down): 직관적, 코드 가독성 높음 / 스택 메모리 부하 가능성, 느림.
# # 반복문 사용 -> 상향식 접근(Bottom-up): 빠름 / 부분 문제들의 풀이 순서 고려 필요.

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


# #11726
# # dp -> 가짓수를 나누고 점화식을 구한다.
# # 메모이제이션을 잊지 않는다.
# import sys
# sys.setrecursionlimit(10**6)

# N = int(input())
# cache = [0] * (N+1)

# def f(n):
#     if cache[n] != 0:
#         return cache[n]

#     if n <= 2:
#         cache[n] = n
#     else:
#         cache[n] = (f(n-1) + f(n-2))%10007

#     return cache[n]

# print(f(N))


# #9465
# for _ in range(int(input())):
#     n = int(input())
#     sticker = [list(map(int, input().split())) for _ in range(2)]
#     dp = [[0] * n for _ in range(2)]

#     for i in range(2):
#         dp[i][0] = sticker[i][0]
#         if n > 1:
#             dp[i][1] = sticker[i^1][0] + sticker[i][1]

#     for j in range(2, n):
#         for i in range(2):
#             dp[i][j] = max(dp[i^1][j-2], dp[i^1][j-1]) + sticker[i][j]

        
#     print(max(dp[0][n-1], dp[1][n-1]))


# #2343
# N, M = map(int, input().split())
# lessons = list(map(int, input().split()))
# l = max(lessons)
# r = sum(lessons)
# m = (l+r)//2
# ans = r

# def is_possible(sz):
#     cnt = 1
#     bluray = 0
#     for lesson in lessons:
#         if bluray + lesson <= sz:
#             bluray += lesson
#         else:
#             cnt += 1
#             bluray = lesson
    
#     return cnt <= M

# while l <= r:
#     if is_possible(m):
#         ans = m
#         r = m-1
#     else:
#         l = m+1

#     m = (l+r)//2

# print(ans)


# # 1699
# N = int(input())
# dp = [i for i in range(N+1)]
# for i in range(4, N+1):
#     for j in range(1, i):
#         if i < j*j:
#             break

#         if dp[i] > dp[i-j*j] + 1:
#             dp[i] = dp[i-j*j] + 1

# print(dp[N])


# #11055
# # 각 요소를 마지막 요소로 삼는 증가 부분 수열의 합을 f(x)로 삼고,
# # max(f(0), f(1), f(2), f(3)...f(n-1)) 을 구한다.

# N = int(input())
# A = list(map(int, input().split()))
# dp = [0]*N
# dp[0] = A[0]
# for i in range(1, N):
#     for j in range(i):
#         if A[j] < A[i]:
#             dp[i] = max(dp[i], dp[j])
    
#     dp[i] += A[i]

# print(max(dp))


# #1018
# # # 완전 탐색으로 푸는 방법
# # N, M = map(int, input().split())
# # board = [input() for _ in range(N)]
# # ans = N*M

# # def fill(y, x, bw):
# #     global ans
# #     cnt = 0
# #     for i in range(8):
# #         for j in range(8):
# #             if (i+j)%2:
# #                 if board[y+i][x+j] == bw:
# #                     cnt += 1
# #             else:
# #                 if board[y+i][x+j] != bw:
# #                     cnt += 1

# #     ans = min(ans, cnt)

# # for y in range(N-7):
# #     for x in range(M-7):
# #         fill(y, x, 'B')
# #         fill(y, x, 'W')

# # print(ans)


# # DP를 이용한 방법
# # 이해 부족.  다시 풀어보기.
# N, M = map(int, input().split())
# board = [input() for _ in range(N)]
# ans = N*M

# def make_acc(bw):
#     global ans
#     acc= [[0]*M for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             if i>0:
#                 acc[i][j] += acc[i-1][j]

#             if j>0:
#                 acc[i][j] += acc[i][j-1]

#             if i>0 and j>0:
#                 acc[i][j] -= acc[i-1][j-1]

#             if (i+j)%2 and board[i][j] == bw:
#                 acc[i][j] += 1

#             if (i+j)%2 == 0 and board[i][j] != bw:
#                 acc[i][j] += 1

#     for i in range(N-7):
#         for j in range(M-7):
#             cnt = acc[i+7][j+7]
#             if i > 0:
#                 cnt -= acc[i-1][j+7]

#             if j>0:
#                 cnt -= acc[i+7][j-1]

#             if i>0 and j>0:
#                 cnt += acc[i-1][j-1]

#             ans = min(ans, cnt)


# make_acc('B')
# make_acc('W')
# print(ans)


# # 2841
# import sys
# input = sys.stdin.readline

# N, P = map(int, input().split())
# ans = 0
# stk = [[] for _ in range(7)]

# for _ in range(N):
#     line, p = map(int, input().split())

#     while stk[line] and stk[line][-1] > p:
#         stk[line].pop()
#         ans += 1

#     if stk[line] and stk[line][-1] == p:
#         continue

#     stk[line].append(p)
#     ans += 1

# print(ans)


# # 4796
# n = 0
# while True:
#     n += 1
#     L, P, V = map(int, input().split())
#     if L == 0 and P == 0 and V == 0:
#         break

#     a = V // P
#     b = V % P
#     if b >= L:
#         print(f"Case {n}: {V//P*L + L}")
#     else:
#         print(f"Case {n}: {V//P*L + V%P}")


# #15686
# from itertools import combinations

# N, M = map(int, input().split())
# r = 0
# c = 0
# house = []
# chicken = []
# for _ in range(N):
#     r += 1
#     ary = list(map(int, input().split()))
#     # print(ary)
    

#     for a in ary:
#         c += 1
#         if a == 1:
#             house.append((r, c))
#         elif a == 2:
#             chicken.append((r, c))
#     c = 0  

# def get_dist(coord1, coord2):
#     r1, c1 = coord1
#     r2, c2 = coord2
#     return abs(r1 - r2) +  abs(c1 - c2)


# ans = 2 * N * len(house)
# for comb in combinations(chicken, M):
#     tot = 0
#     for h in house:
#         tot += min(get_dist(h, ch) for ch in comb)
    
#     ans = min(ans, tot)


# print(ans)


# # 1389
# from collections import deque

# N, M = map(int, input().split())
# gr = [[False] * N for _ in range(N)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     gr[a-1][b-1] = gr[b-1][a-1] = True

# ans = -1
# ans_tot = 987654321
# dist = [[0] * N for _ in range(N)]

# def bfs(start, goal):
#     chk = [False]*N
#     dq = deque()
#     chk[start] = True
#     dq.append((start, 0))
#     while dq:
#         now, d = dq.popleft()
#         if now == goal:
#             return d

#         for nxt in range(N):
#             if gr[now][nxt] and not chk[nxt]:
#                 chk[nxt] = True
#                 dq.append((nxt, d+1))


# for i in range(N):
#     tot = 0
#     for j in range(N):
#         if i != j:
#             if dist[i][j] == 0:
#                 dist[i][j] = dist[j][i] = bfs(i, j)

#             tot += dist[i][j]

#     if ans_tot > tot:
#         ans = i
#         ans_tot = tot

# print(ans+1)


# # 1915
# n, m = map(int,input().split())
# arr = [ list(map(int,input())) for _ in range(n)]
# ans = max(arr[0])

# for i in range(1, n):
#     for j in range(1, m):
#         if arr[i][j] == 1:
#             arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1]) + 1

#     ans = max(ans, max(arr[i]))

# print(ans**2)


# # 2696
# # 다시 해보기
# for _ in range(int(input())):
#     M = int(input())
#     ipt = []
#     for _ in range(M//10+1 if M%10 else M//10):
#         ipt += map(int, input().split())

#     arr = []
#     ans = []
#     for i, v in enumerate(ipt):
#         arr.append(v)
#         if (i&1) == 0:
#             arr.sort()
#             ans.append(arr[i//2])
        
#     print(len(ans))
#     for i in range(len(ans) // 10+1 if len(ans) % 10 else len(ans)//10):
#         print(*ans[i*10:(i+1)*10])


# # 1213
# from collections import Counter

# alphabet_cnt = Counter(input())
# if sum(cnt%2 for cnt in alphabet_cnt.values()) > 1:
#     print("I'm Sorry Hansoo")
# else:
#     half = ''
#     for ch, cnt in sorted(alphabet_cnt.items()):
#         half += ch * (cnt // 2)

#     ans = half
#     for ch, cnt in alphabet_cnt.items():
#         if cnt % 2:
#             ans += ch
#             break

#     ans += ''.join(reversed(half))
#     print(ans)


# # 17298
# N = int(input())
# arr = list(map(int, input().split()))
# stk = []
# ans = [-1 for _ in range(N)]
# for i in range(N):
#     while stk and arr[stk[-1]] < arr[i]:
#         ans[stk[-1]] = arr[i]
#         stk.pop(-1)

#     stk.append(i)

# print(' '.join(map(str, ans)))


# #1015
# N = int(input())
# A = list(map(int, input().split()))
# B = sorted(A)

# chk = [False]*N
# P = []
# for i in A:
#     for j in range(B.index(i), N):
#         if i == B[j] and not chk[j]:
#             chk[j] = True
#             P.append(j)
#             break


# print(" ".join(map(str, P)))


# #10819
# from itertools import permutations

# N = int(input())
# A = list(map(int, input().split()))
# ans = -1
# for arr in set(permutations(A, N)):
#     ans = max(ans, sum(abs(arr[i-1] - arr[i]) for i in range(1, N)))

# print(ans)


# # 1026
# N = int(input())
# A = sorted(map(int, input().split()))
# B = sorted(map(int, input().split()), reverse=True)
# print(sum(A[i]*B[i] for i in range(N)))


#3986
ans = 0
for _ in range(int(input())):
    stk = []
    for ch in input():
        if not stk or stk[-1] != ch:
            stk.append(ch)
        else:
            stk.pop()

    ans += len(stk) == 0

print(ans)