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
  






