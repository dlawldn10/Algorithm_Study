# # #14178
# t = int(input())

# for tc in range(1, t + 1) :
#     n, d = map(int, input().split())
#     d = d * 2 + 1
#     result = n // d
#     if n % d != 0 :
#         result += 1

#     print('#%d %d' % (tc, result))

#13732
import collections

T = int(input())
for i in range(1, T+1):
    n = int(input())
    arr = []
    #입력받음
    for j in range(n):
        arr.append(input())

    point = []
    # '#'있는 곳 검사
    for k in range(n):
        for l in range(n):
            if arr[k][l] == '#':
                point[k].append([k, l])

    print(point)

    if len(point) < 4:
        print('#' + str(i) + ' no')
    else:
        for o in range(len(point)):
            for p in range(len(point[o])):
                if ((abs(point[o][p][1] - point[o][p+1][1]) ==
                    abs(point[o+1][p][0] - point[o+1][p+1][0])) and
                    (abs(point[o][p][1] - point[o][p+1][1]) ==
                    abs(point[o][p+1][0] - point[o+1][p+1][0]))):
                    print('#' + str(i) + ' yes')
                else:
                    pass

        

    
    