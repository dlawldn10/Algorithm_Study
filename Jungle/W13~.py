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


#11816
X = input()

if X[1] == 'x':
    # 16진수
    print(int(X, 16))
elif X[0] == '0':
    # 8진수
    print(int(X, 8))
else :
    # 10진수
    print(X)




