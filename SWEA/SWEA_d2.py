# #1204
# from itertools import count

# T = int(input())
# for _ in range(1, T+1):
#     i = int(input())
#     done = []
#     max_cnt = 0
#     array = list(map(int, input().split()))
#     max_value = []
#     for j in range(0, len(array)):
#         if array[j] in done:
#             pass
#         elif array.count(array[j]) >= max_cnt:
#             max_cnt = array.count(array[j])
#             done.append(array[j])
#             max_value.append([max_cnt, array[j]])
#         else:
#             done.append(array[j])

#     print('#' + str(i) + ' ' + str(max(max_value)[1]))

# #최빈값 문제 -> 위처럼 말고 아래처럼 풀기
# import collections
# T = int(input())
# for _ in range(1, T+1):
#     i = int(input())
#     a = list(map(int, input().split()))

#     print('#' + str(i) + ' ' + str(collections.Counter(a).most_common(1)[0][0]))


# #1284
# T = int(input())
# for i in range(1, T+1):
#     p, q, r, s, w = map(int, input().split())
#     if w < r:
#         result = w*p if w*p < q else q
#         print('#' + str(i) + ' ' + str(result))
#     else:
#         result = w*p if w*p < q+((w-r)*s) else q+((w-r)*s)
#         print('#' + str(i) + ' ' + str(result))
 

# #1285
# T = int(input())
# for i in range(1, T+1):
#     n = int(input())
#     ary = list(map(int, input()))
#     for j in range(len(ary)):
#         ary[j] = abs(ary[j])
#     ary.sort()
#     print('#' + str(i) + ' ' + str(ary[0]) + ' ' + str(ary.count(ary[0])))

# #1288
# T = int(input())

# for i in range(1, T+1):
#     n = int(input())
#     num = set()
#     count = 0
#     while len(num) != 10:
#         count += 1
#         tmp_string = str(n*count)
#         for k in range(len(tmp_string)):
#             num.add(tmp_string[k])
            
        
#     print('#' + str(i) + ' ' + tmp_string)

# #1940
# T = int(input())
# for i in range(1, T+1):
#     n = int(input())
#     l = 0
#     s = 0
#     for j in range(n):
#         ary = list(map(int, input().split()))
#         if ary[0] == 1:
#             s += ary[1]
#         elif ary[0] == 2:
#             s = 0 if s-ary[1] < 0 else s-ary[1]
#         l += s

#     print('#' + str(i) + ' ' + str(l))

# #1945
# T = int(input())
# num_ary = [2, 3, 5, 7, 11]
# for i in range(1, T+1):
#     n = int(input())
#     ary = []
#     for d in num_ary:
#             count = 0
#             while n%d == 0:
#                 n = n//d
#                 count += 1
#             ary.append(str(count))
#     print('#' + str(i) + ' ' + ' '.join(ary))


#