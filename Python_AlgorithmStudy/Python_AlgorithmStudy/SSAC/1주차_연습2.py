# #1.
# N = int(input())

# for i in range(1, N+1):
# 	print(i)


# #2.
# N = int(input())

# for i in range(0, N):
# 	print(N-i)


# #3.
# import sys
# T = int(sys.stdin.readline())

# for i in range(0, T):
# 	a, b = map(int, sys.stdin.readline().split())
# 	print("Case #{0}: ".format(i+1) + str(a+b))


# #4.
# import sys
# T = int(sys.stdin.readline())

# for i in range(0, T):
# 	a, b = map(int, sys.stdin.readline().split())
# 	print("Case #{0}: {1} + {2} = {3}".format(i+1, a, b, a+b))


# #5.
# import sys
# T = int(sys.stdin.readline())

# for i in range(0, T):
# 	print("*"*(i+1))


# #6.
# import sys
# T = int(sys.stdin.readline())

# for i in range(0, T):
# 	print(" "*(T-i-1) + "*"*(i+1))


# #7.
# import sys
# N,X = map(int,sys.stdin.readline().split())
# num = list(map(int,sys.stdin.readline().split()))
# for i in range(0, N):
# 	if X > num[i] :
# 		print(num[i], end=' ')


# #8.
# #파일이 끝날때까지 읽어오는 방법
# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except EOFError:
#         break


# #9.
# N = int(input())
# newNum = N
# count = 0

# while True:
# 	a = newNum//10
# 	b = newNum%10
# 	c = (a + b)%10

# 	newNum = b*10 + c
# 	count += 1
# 	if(newNum == N):
# 		print(count)
# 		break



# #10.
# import sys
# N = int(sys.stdin.readline())
# num = list(map(int, sys.stdin.readline().split()))
# num.sort()
# print(num[0], num[N-1])


# #11.
# import sys
# A = list()
# B = list()
# for i in range(0,9):
# 	tmp = int(sys.stdin.readline())
# 	A.append(tmp)
# 	B.append(tmp)
# A.sort()
# for i in range(0, 9):
# 	if(B[i] == A[-1]):
# 		print(A[-1])
# 		print(i+1)
# 		break


# #12.
# import sys
# a=int(sys.stdin.readline())
# b=int(sys.stdin.readline())
# c=int(sys.stdin.readline())

# idx = list()
# for i in range(0,10):
# 	idx.append(0)
# res = str(a*b*c)
# for i in range(0, len(res)):
# 	idx[int(res[i])] += 1
# for i in range(0, len(idx)):
# 	print(idx[i])


# #13.
# import sys
# n = set()
# count = 0
# for i in range(0, 10):
# 	n.add(int(sys.stdin.readline())%42)
# print(len(n))


# #14.
# import sys
# N = int(sys.stdin.readline())
# P = list(map(int, sys.stdin.readline().split()))

# P.sort()
# M = P[-1]

# for i in range(0, N):
# 	P[i] = P[i]/M*100

# print(sum(P)/N)



# #16.
# #다른사람 풀이
# n = int(input())

# for _ in range(n):
#     ox_list = list(input())
#     score = 0  
#     sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
#     for ox in ox_list:
#         if ox == 'O':
#             score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
#             sum_score += score  # sum_score = sum_score + score
#         else:
#             score = 0
#     print(sum_score)


# #17.
# #소숫점 세번째 자릿수 까지 표기하기
# n = int(input())
# count = 0
# for i in range(0, n):
# 	Pointlist = list(map(int, input().split()))
# 	ave = (sum(Pointlist) - Pointlist[0])/Pointlist[0]
	
# 	for j in range(1, Pointlist[0]+1):
# 		if Pointlist[j] > ave:
# 			count += 1

# 	res = count/Pointlist[0]*100
# 	print(str("{:.3f}%".format(res)))
# 	count = 0


# #18.
# def solve(a):
#     ans = sum(a)

#     return ans


# #19.
# #다른 사람 풀이
# #각 자릿수의 합을 구하는 방법 sum(map(int,str(n)))
# a = list()
# for n in range(1,10001):
# 	n=n+sum(map(int,str(n)))
# 	a.append(n)

# for j in range(1, 10001):
# 	if j not in a:
# 		print(j)




# #20.
# #다른 사람 풀이
# num = int(input())
# hansu = 0

# for n in range(1, num+1) :
#     if n <= 99 : # 1부터 99까지는 모두 한수
#         hansu += 1 
    
#     else :     
#         nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
#         if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
#             hansu+=1

# print(hansu)