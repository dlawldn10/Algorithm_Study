

# #0809_2주차 라이브 코딩


#9012번 괄호()
#이런 괄호의 쌍을 맺어주는 문제 -> 대표적 스택 문제
# ( 가 들어오면 push 하고, ) 가 들어오면 pop을 한다.
#마지막에 스택이 비어야 vps.
#종류가 맞지 않거나 스택이 비어있는 경우 invalid 처리를 해준다.
# for i in range(int(input())):
#     stk = []
#     is_vps = True
#     for ch in input():
#         if ch == '(':
#             stk.append(ch)
#         else:
#             if stk:
#                 stk.pop()
#             else:
#                 is_vps=False
#                 break
#     if stk:
#         is_vps = False

#     print('YES' if is_vps else 'NO')



#1935번 후위표기식 큐
#후위표기식이란? : 연산자의 위치를 기준으로 전위, 중위, 후위로 나눈다.
#1 + 2 -> 중위 표기식
#+ 1 2 -> 전위 표기식
#1 2 + -> 후위 표기식
#1+2-3 -> 1 2 + 3 -
#ABC*+DE/- -> A + B * C - D / E
#숫자를 만나면 스택에 넣고
#연산자를 만나면 숫자 두개 빼서 연산하기
#결과를 다시 스택에 넣기
#마지막에 스택에 남은 숫자가 정답.
# N = int(input())
# s = input()
# arr = [int(input()) for _ in range(N)]
# stk = []
# for ch in s:
#     if ch.isalpha(): #피연산자이면
#         stk.append(arr[ord(ch) - ord('A')])
#         continue

#     b = stk.pop()
#     a = stk.pop()
#     if ch == '+':
#         stk.append(a+b)
#     elif ch == '-':
#         stk.append(a-b)
#     elif ch == '*':
#         stk.append(a*b)
#     elif ch == '/': #나눗셈의 경우 연산 순서 중요하므로 주의할 것!
#         stk.append(a/b)

# print(f"{stk[0]:.2f}")
# print(f'{stk[0]}, {2+5}, {s}')



#*항상 극단값과 테스트값 넣어보기.
#큐에다가 숫자를 모두 넣고
#pop을 하고, 그 수를 뒤에다 넣는다.
# from collections import deque
# from os import name, spawnl

# dq = deque()
# for i in range(1, int(input())+1):
#     dq.append(i)

# #1개가 되면 탈출
# while len(dq) > 1:
#     dq.popleft()
#     dq.append(dq.popleft())

# print(dq.popleft())



#절댓값 힙
#튜플이나 리스트를 정렬할 경우, 인덱스 0번째 위치한 숫자들을 비교해서 정렬한다.
#만약 0번째가 같으면 다음 인덱스로 넘어간다.
#커스텀 정렬을 하고 싶으면 람다를 사용해서도 정렬 가능.
# a=[(9, 2), (3,5), (5,7), (3,0), (3,9)]
# a.sort()
# a.sort(key = lambda x: x[0] > A[0] and x[1] > A[1], P) # -> 아 다 못 썼다...
# print(a)

# 방법1
# 튜플로 묶어서 저장하기
# (abs(x), x)
# import sys
# import heapq

# numbers = int(input())
# heap = []

# for _ in range(numbers):
#     num = int(sys.stdin.readline())
#     if num != 0:
#         heapq.heappush(heap, (abs(num), num))
#     else:
#         try:
#             print(heapq.heappop(heap)[1])
#         except:
#             print(0)

#방법2
#우선순위 큐를 두개 이용해서 푸는 방법
#이 방법은 분기가 많아서 복잡함. 리스트가 두개라서 서로 비교해야됨.
# import heapq, sys

# input = sys.stdin.readline
# min_heap = []   #양수 저장
# max_heap = []   #음수 저장
# for _ in range(int(input())):
#     x = int(input())

    


#회사에 있는 사람
#집합 사용
# import sys

# input = sys.stdin.readline()
# s =set()

# for _ in range(int(input)):
#     name, el = input().split()
#     if el == "enter":
#         s.add(name)
#     elif name in s: 
#         s.remove(name)
            
# for name in sorted(s, reverse=True):
#     print(name)


#다른 사람 풀이
# import sys

# pe = {}

# for _ in range(int(sys.stdin.readline())):
#   p, c = sys.stdin.readline().rstrip().split()

#   if c == 'enter':
#     pe[p] = 'enter'
#   else:
#     if pe[p]:
#       del pe[p]

# for people in sorted(pe, reverse=True):
#   print(people)

#베스트 셀러
#같은 값이 몇개인지 셀때 유용
#딕셔너리 사용.
# +) collections.Counter 사용하면 특정 문자열에 들어있는 문자들의 갯수를 딕셔너리로 나타낼 수 있음.
#매우 편리하므로 잘 써보기...

# import sys
# input() = sys.stdin.readline
# d = dict()
# for _ in range(int(input())):
#     book = input().rstrip()     #rstrip -> 뒤에 줄바꿈(\n) 빼줌.
#     if book in d:
#         d[book] += 1
#     else:
#         d[book] = 1

# #각각 모아서 반환해주는 기능이 있음.
# # print(d.keys())
# # print(d.values())
# # print(d.items())

# m = max(d.values())
# ans = ''
# for k, v in d.items():
#     if v == m and (ans == ' ' or ans > k):
#         ans = k

# print(ans)


#이번주 메인 과제는 -> 구글 설문조사. 
#  자료구조 문제들 풀이법 및 pseudo code(의사코드)제출.
#  문제 해결 능력을 좀 더 키우기 위해서.
# - 실 구현은 할 필요 없음
# - 어떤 자료구조를 사용해서 어떻게 풀면 되는지.
# - ex) 리스트는 이러이러해서 시간 때문에 안될것 같다. 
#       대신에 이러한 이유때문에 이러한 것을 써야할 것 같다. 