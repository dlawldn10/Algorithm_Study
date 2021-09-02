#1.
#동전0과 똑같.
# K = int(input())
# coins = [500, 100, 50, 10, 5, 1]
# K = 1000 - K
# ans = 0
# for coin in coins:
#     ans += K // coin
#     K %= coin
# print(ans)


#2.
#풀이는 맞췄지만 구현을 못했음...
#다른 사람 풀이
# s = int(input())
# n = 1
# while n * (n + 1) / 2 <= s:
#     n += 1
# print(n - 1)


#3.
#내풀이 -> 틀림 -> 수정 -> 맞음
# count = 0
# while True:
#     L, P, V = map(int, input().split())
#     if L == 0 and P == 0 and V == 0:
#         break

#     count += 1
#     a = V // P
#     b = V % P
#     if b >= L:
#         print("Case {0}: {1}".format(count, (L*a + L)))
#     else:
#         print("Case {0}: {1}".format(count, (L*a + b)))


#4.
# x, y, w, h = map(int, input().split())

# #위
# up = h-y

# #아래
# down = y

# #오른
# right = w-x

# #왼
# left = x

# dist = [up, down, right, left]

# dist.sort()
# print(dist[0])


#5.
# x = list()
# y = list()

# for i in range(0, 3):
#     tmp1, tmp2 = map(int, input().split())
#     x.append(tmp1)
#     y.append(tmp2)

# for i in range(3):
#     if x.count(x[i]) == 1:
#         a = x[i]
#     if y.count(y[i]) == 1:
#         b = y[i]
# print(a, b)


#6.
# while True:
#     l =list(map(int, input().split()))
#     if l[0] == 0 and l[1] == 0 and l[2] == 0:
#         break
#     l.sort()
#     if l[-1]**2 == l[0]**2 + l[1]**2:
#         print("right")
#     else:
#         print("wrong")


#7.
#유클리드 기하학 원, 택시 기하학 원 알고 풀면 쉬워짐.
#다른 사람 풀이
# import math
# r = int(input())
# print(r*r*math.pi)
# print(r*r*2)


#8.
#네가지 경우의 수가 있음.
#1. 두 원이 일치하는 경우
#2. 두 원이 한점에서 만나는 경우 -> 외접, 내접
#3. 두 원이 만나지 않는 경우
#4. 두 원이 두 점에서 만나는 경우

#다른 사람 풀이
# n= int(input())

# for i in range(n):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     r = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
#     R = [r1,r2,r]
#     m=max(R)
#     R.remove(m)
#     print(-1 if (r==0 and r1==r2) 
#     else 1 if (r == r1 +r2 or m== sum(R)) 
#     else 0 if(m>sum(R)) 
#     else 2)


#9.
# n = int(input())
# ans = 1
# for i in range(1, n+1):
#     ans = ans * i
# print(ans)


#10.
#풀이는 맞췄는데 구현 못함...
#다른 사람 풀이
# import sys
# n = int(sys.stdin.readline())
# countList = [0]*10001

# for i in range(n):
#     countList[int(sys.stdin.readline())] += 1

# for i in range(10001):
#     if countList[i] != 0:
#         for j in range(countList[i]):
#             print(i)


#11.
#C++로 함
#include <iostream>
#define MAX 100
# using namespace std;

# int main() {
#    int num, target, sum = 0;
#    int maxNum = 0;
#    int arr[MAX] = { 0, };
#    cin >> num >> target;
#    for (int i = 0; i < num; i++)
#        cin >> arr[i];

#    for (int i = 0; i < num - 2; i++) {
#        for (int j = i + 1; j < num - 1; j++) {
#            for (int k = j + 1; k < num; k++)
#            {
#                sum = arr[i] + arr[j] + arr[k];
#                if (sum > maxNum && target >= sum) {
#                    maxNum = sum;
#                }
#            }
#        }
#    }
       
           
#    cout << maxNum;
# }


#12. 이건 왜 틀림..? -> 아 0인 경우 추가 안해서...
# N = int(input())
# ans = 0
# for i in range(1, N+1):
#     if N == i + sum(list(map(int,str(i)))):
#         ans = i
#         break
# print(ans)


# #다른 사람 풀이 -> 왜 이건 시간초과 안남?
# N = int(input())
# print_num = 0
# for i in range(1, N+1):
#     div_num = list(map(int, str(i)))
#     sum_num = i + sum(div_num)
#     if(sum_num == N):
#         print_num = i
#         break
# print(print_num)


#13.
#2차원 배열 일때 filter 사용하면 편리함.
#다른 사람 풀이
# N = int(input())
# P = [list(map(int, input().split())) for _ in range(N)]
# ans = []

# for A in P:
#   f = list(filter(lambda x: x[0] > A[0] and x[1] > A[1], P))
#   ans.append(len(f) + 1)

# print(' '.join(list(map(str, ans))))


#14.
#다시 풀기
#다른 사람 풀이
# N, M = map(int, input().split())
# original = []
# count = []

# for _ in range(N):
#     original.append(input())

# for a in range(N-7):
#     for b in range(M-7):
#         index1 = 0
#         index2 = 0
#         for i in range(a, a+8):
#             for j in range(b, b+8):
#                 if (i+j) % 2 == 0:
#                     if original[i][j] != 'W':
#                         index1 += 1
#                     if original[i][j] != 'B':
#                         index2 += 1
#                 else:
#                     if original[i][j] != 'B':
#                         index1 += 1
#                     if original[i][j] != 'W':
#                         index2 += 1
#         count.append(min(index1, index2))

# print(min(count))



#15.
# six_n을 1씩 더해가는 while문을 만들어 666이 안에 들어있다면 cnt를 1 증가시키고, cnt가 n과 같다면 six_n을 출력해준다.
# n = int(input())
# cnt = 0
# six_n = 666
# while True:
#     if '666' in str(six_n):
#         cnt += 1
#     if cnt == n:
#         print(six_n)
#         break
#     six_n += 1


#16.
# N = int(input())
# P = list()
# for i in range(N):
#     P.append(int(input()))

# P.sort()
# for i in range(N):
#     print(P[i])




#17.
#다른 사람 풀이
#개천재다 ㄹㅇ
#오름차순 정렬
# import sys
# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(sys.stdin.readline()))
# for i in sorted(l):
#     sys.stdout.write(str(i)+'\n')


#18.
#다시 풀기
#다른 사람 풀이
# from itertools import permutations #순열 함수

# N = int(input())
# N_list = [i for i in range(1, N+1)]

# for numbers in list(permutations(N_list)):
#     for num in numbers:
#         print(num, end=' ')
#     print()


#19.
#순열 이용
#다시 풀기
#다른 사람 풀이
# import sys
# from itertools import permutations

# n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# num = list(permutations(n, 3))	# 순열로 3개씩 뽑음

# t = int(sys.stdin.readline())
# for _ in range(t):
#     test, s, b = map(int, sys.stdin.readline().split())
#     test = list(str(test))
#     removed_cnt = 0     # 배열에서 제거된 튜플 개수

#     # num : 3개 리스트
#     leng = len(num)
#     for i in range(leng):
#         s_cnt = b_cnt = 0   # 스트 개수, 볼 개수 0 초기화
#         i -= removed_cnt

#         for j in range(3):
#             test[j] = int(test[j])
#             if test[j] in num[i]:
#                 if j == num[i].index(test[j]):
#                     s_cnt += 1
#                 else:
#                     b_cnt += 1

#         if s_cnt != s or b_cnt != b:
#             num.remove(num[i])      # 스트 개수, 볼 개수 다르면 배열에서 제거
#             removed_cnt += 1

# print(len(num))



#20.
#다시 풀기
#다른 사람 풀이
# import sys
# input = sys.stdin.readline
# def dfs(idx, sum):
#     global cnt
#     if idx >= n:
#         return
#     sum += s_[idx]
#     if sum == s:
#         cnt += 1
#     dfs(idx + 1, sum - s_[idx])
#     dfs(idx + 1, sum)
# n, s = map(int, input().split())
# s_ = list(map(int, input().split()))
# cnt = 0
# dfs(0, 0)
# print(cnt)