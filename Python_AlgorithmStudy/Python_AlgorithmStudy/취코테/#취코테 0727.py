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


#