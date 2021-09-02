#1.
#print("Hello World!")


#2.
# for i in range(0,2):
# print("강한친구 대한육군")

#3.
# print("\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \(__)|")


#4.
# print("|\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\\\__|")


#5.
# A, B = map(int, input().split())
# print(A+B)


#6.
# A, B = map(int, input().split())
# print(A-B)


#7.
# A, B = map(int, input().split())
# print(A*B)


#8.
# A, B = map(int, input().split())
# print(A/B)

#9.
#/ -> 나눗셈 소숫점 버리지 않음.
#// -> 나눗셈 소숫점 버림. 결과 정수.
# A, B = map(int, input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)

#10.
# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)


#11.
#472
#385
#내 풀이
# A = input()
# B = input()

# a = list()
# b = list()
# for i in range(0, 3):
#     a.append(int(A[i]))
#     b.append(int(B[i]))

# f = ""
# n = 0
# for j in range(0, 3):
#     for k in range(0, 3):
#        f += str((a[2-k]*b[2-j])%10 + n)
#        n = (a[2-k]*b[2-j])//10
#        if(k == 2):
#            f += str(n)
#            n=0
        
# f = f[::-1]
# print(f[8:12])
# print(f[4:8])
# print(f[:4])
# print(int(A)*int(B))

#다른 사람 풀이
# A = int(input())  # 첫번째 입력받은 문자 : 숫자로 변환
# B = input()       # 두번째 입력받은 문자 : 문자열 그대로 둠

# # 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
# AxB2 = A * int(B[2])
# AxB1 = A * int(B[1])
# AxB0 = A * int(B[0])
# AxB = A * int(B)

# print(AxB2, AxB1, AxB0, AxB, sep='\n')
# # sep='\n'로 줄바꿈


#12.
# A, B = map(int, input().split())
# if(A > B):
#     print(">")
# if (A < B):
#     print("<")
# if(A == B):
#     print("==")


#13.
# A = int(input())
# if(90 <= A & A <= 100):
#     print("A")
# elif(80 <= A & A < 90):
#     print("B")
# elif(70 <= A & A < 80):
#     print("C")
# elif(60 <= A & A < 70):
#     print("D")
# else:
#     print("F")


#14.
# A = int(input())
# if((A%4 == 0 and A%100 != 0) or A%400 == 0):
#     print("1")
# else:
#     print("0")


#15.
# X = int(input())
# Y = int(input())

# if(X > 0 and Y > 0):
#     print(1)
# elif(X < 0 and Y > 0):
#     print(2)
# elif(X < 0 and Y < 0):
#     print(3)
# elif(X > 0 and Y < 0):
#     print(4)


#16.
# h, m = map(int, input().split())
# if(m-45 < 0):
#     m = 60 + (m-45)
#     if(h-1 == -1):
#         h=23
#     else:
#         h -= 1
# else:
#     m -= 45
# print(h, m)


#17.
# N = int(input())
# for i in range(1, 10):
#     print("%d * %d = %d" % (N, i, N*i))



#18.
# N = int(input())
# ans = list()
# for i in range(0, N):
#     a, b = map(int, input().split())
#     ans.append(a+b)
# for j in range(0, N):
#     print(ans[j])



#19.
# N = int(input())
# ans = ((N+1)*N)//2
# print(ans)


#20.
#한개의 정수를 입력받을 때
# a = int(sys.stdin.readline())

#정해진 갯수의 정수를 한줄에 입력받을 때
# a,b,c = map(int,sys.stdin.readline().split())

#임의의 갯수의 정수를 한줄에 입력받을 때
# data = list(map(int,sys.stdin.readline().split()))

#임의의 갯수의 정수를 n줄 입력받아 2차원 리스트에 저장할때
# import sys
# data = []
# n = int(sys.stdin.readline())
# for i in range(n):
#     data.append(list(map(int,sys.stdin.readline().split())))

#문자열 n줄을 입력받아 리스트에 저장할때
# import sys
# n = int(sys.stdin.readline())
# data = [sys.stdin.readline().strip() for i in range(n)]

#내풀이
# import sys
# T = int(sys.stdin.readline())

# for i in range(0, T):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)

 