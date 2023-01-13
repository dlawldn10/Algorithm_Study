# #11653
# N = int(input())

# for i in range(2, N+1):
#     while N % i == 0:
#         N = N // i
#         print(i)


# #11720
# N = int(input())
# numstr = input()
# sum = 0
# for n in numstr:
#     sum += int(n)
# print(sum)


# #11816
# X = input()

# if X[1] == 'x':
#     # 16진수
#     print(int(X, 16))
# elif X[0] == '0':
#     # 8진수
#     print(int(X, 8))
# else :
#     # 10진수
#     print(X)


#8595
#7:20
# --

# # 시간초과 풀이
# import sys
# input = sys.stdin.readline
# n = int(input())
# hiddenStr = input()
# tmpStr = ""
# for i in hiddenStr:
#     if i.isdigit():
#         tmpStr += i
#     else:
#         tmpStr += ' '
# print(sum(list(map(int, tmpStr.split()))))

# # 내 풀이
# n = int(input())
# hiddenStr = input()
# tmpStr = ""
# result = 0
# for i in hiddenStr:
#     if i.isdigit():
#         tmpStr += i
#     else:
#         if len(tmpStr) > 0:
#             result += int(tmpStr)
#             tmpStr = ""

# if tmpStr != '':
#     result += int(tmpStr)
# print(result)


# # 정답 코드
# n = int(input())
# arr = input()
# num = ''
# val = 0

# for i in arr:
#   if '0' <= i and i <= '9':
#     num += i
#   elif num != '':
#     val += int(num)
#     num = ''
    
# if num != '':
#   val += int(num)
  
# print(val)


#1269
#11:10
#11:28
# # 시간초과 풀이
# a, b = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# commons = []
# cnt = 0
# for num in A:
#   if num in B:
#     commons.append(num)
#   else:
#     cnt+=1

# for num in B:
#   if num not in commons:
#     cnt+=1

# print(cnt)

# # 대칭 차집합 구하는 방법 사용 풀이
# a, b = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# result = list(set(A) ^ set(B))
# print(len(result))

### 공부
## 합집합
# union = list(set(A) | set(B))

## 교집합
# intersection = list(set(A) & set(B))

## 차집합
# complement = list(set(A) - set(B))
# complement = list(set(B) - set(A))

## 대칭차집합
# sym_diff = list(set(A) ^ set(B))



#11728
#11:28
#11:39
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# print(" ".join(map(str, sorted(A+B))))


#1406
# #11:40
# #12:00
# import sys
# init = list(input())
# N = int(input())
# stk = []
# for _ in range(0, N):
#   cmd = sys.stdin.readline()
#   if cmd[0] == 'P':
#     init.append(cmd[2])
#   elif cmd[0] == 'L' and len(init)>0:
#     stk.append(init.pop())
#   elif cmd[0] == 'D' and len(stk)>0:
#     init.append(stk.pop())
#   elif cmd[0] == 'B'and len(init)>0:
#     init.pop()

# print("".join(init + list(reversed(stk))))


#9935
#11:27
#--

# # 정답코드
# import sys
# input = sys.stdin.readline
# word = list(input().rstrip())
# x = list(input().rstrip())
# stack = []
# for i in word:

#     #스택에 문자를 일단 넣는다.
#     stack.append(i)

#     # 폭발문자열의 마지막과 Word의 문자열 비교한다.
#     if stack[-1] == x[-1] and len(stack) >= len(x):

#         #스택의 뒤에서부터 폭발문자열의 길이까지의 문자열이 폭발 문자열과 같으면,
#         if stack[-len(x):] == x:
#             #폭발 문자열의 길이 만큼 스택에서 pop하여 해당 문자열들을 빼낸다.
#             for i in range(len(x)): stack.pop()
            
# if stack:
#     print("".join(stack))
# else:
#     print("FRULA")


#2231
#11:03
#11:23
# N = int(input())
# ans = 0
# for i in range(1, N):
#     res = 0
#     res += i
#     spl = list(str(i))
#     for j in spl:
#         res += int(j)
#     if res == N:
#         ans = i
#         break
# print(ans)


#2789
#11:23
#11:30
# from itertools import combinations
# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# sumBig = 0
# for i in combinations(cards, 3):
#     if sumBig <= sum(i) and sum(i) <= M:
#         sumBig = sum(i)
# print(sumBig)


#10974
#11:30
#11:37
# from itertools import permutations
# N = int(input())
# lst = [i for i in range(1, N+1)]
# for j in permutations(lst):
#     print(' '.join(map(str, list(j))))


#6603
#11:37
#11:50
# from itertools import combinations
# while True:
#     numStr = list(map(int, input().split()))
#     K = numStr[0]
#     if K == 0:
#         break
#     numList = []
#     for i in range(1, K+1):
#         numList.append(numStr[i])
#     for j in combinations(numList, 6):
#         print(' '.join(map(str, list(j))))
#     print()


#10815
#11:01
#11:19
# N = int(input())
# cards = list(map(int, input().split()))
# M = int(input())
# ans = [0 for _ in range(0, M)]
# lst = list(map(int, input().split()))
# cards.sort()

# for i in range(0, len(lst)):
#     left = 0
#     right = len(cards)-1
#     mid = (left + right) // 2

#     while left <= right:
#         if cards[mid] == lst[i]:
#             ans[i] = 1
#             break
#         elif cards[mid] > lst[i]:
#             right = mid - 1
#         else:
#             left = mid + 1

#         mid = (left + right) // 2

# print(' '.join(map(str, ans)))


#2343
#11:25
# --
#정답코드
# #가능한 블루레이의 크기를 이분탐색
# N, M = map(int, input().split())
# lessons = list(map(int, input().split()))
# l = max(lessons)
# r = sum(lessons)
# m = (l + r) // 2
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
#         r = m - 1
#     else:
#         l = m + 1

#     m = (l + r) // 2

# print(ans)


#1654
#11:13
K, N = map(int, input().split())
lines = []
for _ in range(0, K):
    lines.append(int(input()))

l = 1
r = max(lines)
mid = (l+r)//2

# 해당 길이의 랜선이 몇개가 될 수 있는지
def is_possible(sz):
    cnt = 0
    for line in lines:
        cnt += line // sz
    return cnt >= N

ans = 0
while l <= r:
    # 조건을 만족하여 더 커질 수 있다.
    if is_possible(mid):
        ans = mid
        l = mid + 1
    else:
        # 너무 커서 조건에 부합하지 않는다.
        r = mid - 1

    mid = (l+r)//2

print(ans)














