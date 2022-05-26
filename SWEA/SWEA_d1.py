# #1545
# n = int(input())
# array = []

# for i in range(n+1):
#     array.append(str(n-i))

# print(' '.join(array))

# #2019
# n = int(input())
# result = 1
# for i in range(n):
#     print(result, end = ' ')
#     result *= 2

# print(result)

# #1936
# a, b = map(int, input().split())

# if abs(a-b) == 1:
#     win = "A" if a > b else "B"
# elif abs(a-b) == 2:
#     win = "A" if a < b else "B"

# print(win)

# #1933
# n = int(input())
# print(1, end=' ')
# array = []
# for i in range(2, n+1):
#     if n % i == 0:
#         array.append(i)
#         print(array[-1], end=' ')

# #1938
# a, b = map(int, input().split())

# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)

# #2025
# n = int(input())
# result = 0
# for i in range(1, n+1):
#     result += i
# print(result)

# #2027
# idx = 0
# for _ in range(5):
#     for i in range(5):
#         if idx == i:
#             print('#', end='')
#         else:
#             print('+', end='')
#     idx += 1
#     print()


# #2029
# T = int(input())
# for i in range(1, T+1):
#     a, b = map(int, input().split())
#     print('#' + str(i) + ' ' + str(a//b) + ' ' + str(a%b))

# #2043
# p, k = map(int, input().split())
# count = 0
# while p != k:
#     k += 1
#     count += 1
    
# print(count+1)

# #2046
# n = int(input())

# for _ in range(n):
#     print('#', end='')

# #2047
# l = input()
# print(l.upper())

# #2050
# from operator import indexOf
# l = input()
# array = [chr((ord('A') +i)) for i in range(26)]
# for i in range(0, len(l)):
#     for alphabet in array:
#         if l[i] == alphabet:
#             print(indexOf(array, alphabet)+1, end=' ')

# #2056
# T = int(input())
# thirty_m = [4, 6, 9, 11]

# for t in range(1, T+1):
#     l = input()
#     m = l[4:6]
#     if 1 <= int(m) <= 12:
#         d = l[6:]
#         if 1 <= int(d) <= 31:
#             if (int(m) in thirty_m) and int(d) > 30:
#                 print('#' + str(t) + ' -1')
#             elif (int(m) == 2) and int(d) > 28:
#                 print('#' + str(t) + ' -1')
#             else:
#                 y = l[0:4]
#                 print('#' + str(t) + ' ' + y + '/' + m + '/' + d)
#         else:
#             print('#' + str(t) + ' -1')
#     else:
#         print('#' + str(t) + ' -1')

# #2058
# l = input()

# result = 0

# for i in range(0, len(l)):
#     result += int(l[i])

# print(result)

# #2063
# n = int(input())
# array = list(map(int, input().split()))

# array.sort()
# print(array[len(array)//2])

# #2068
# T = int(input())
# for i in range(1, T+1):
#     array = list(map(int,input().split()))
#     num = array[0]
#     for j in range(1, 10):
#         if array[j] > num:
#             num = array[j]

#     print('#' + str(i) + ' ' + str(num))

# #2070
# T = int(input())
# for i in range(1, T+1):
#     a, b = map(int, input().split())
#     if a < b:
#         print('#' + str(i) + ' <')
#     elif a == b:
#         print('#' + str(i) + ' =')
#     elif a > b:
#         print('#' + str(i) + ' >')


#2071

# T = int(input())

# for i in range(1, T+1):
#     array = list(map(int, input().split()))
#     print('#' + str(i) + ' ' + str(int(round(sum(array)/10, 0))))

# #2072
# T = int(input())

# for i in range(1, T+1):
#     array = list(map(int, input().split()))
#     result = 0
#     for j in range(0, 10):
#         if array[j] % 2 != 0:
#             result += array[j]

#     print('#' + str(i) + ' ' + str(result))
