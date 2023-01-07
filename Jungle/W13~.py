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


# 정답 코드
n = int(input())
arr = input()
num = ''
val = 0

for i in arr:
  if '0' <= i and i <= '9':
    num += i
  elif num != '':
    val += int(num)
    num = ''
    
if num != '':
  val += int(num)
  
print(val)






