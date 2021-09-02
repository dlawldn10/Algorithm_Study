# from itertools import combinations


# #0802_1주차 라이브 코딩


# #input() -> 입력값 한줄을 받아올 수 있는 함수
# #combinations( , ) -> 가능한 조합을 모두 찾아줌
# #sorted() -> 오름차순?으로 정렬해줌

# #일곱난쟁이
# #1. combination 사용
# h = list(int(input()) for _ in range(9))
# for i in combinations(h,7):
#     if sum(i) == 100:
#         for j in sorted(i):
#             print(j)
            
#         break


# #3. 9명중 2명을 구해서 제외시키는 방법
# h = list(int(input()) for _ in range(9))
# tot = sum(j)
# for i in range(8):
#     for j in range(i+1):
#         if tot - h[i] - h[j] == 100:
#             for k in range(9):
#                 if k != i and k != j :
#                     print(h[k])

#             break



# #동전0
# N, K = map(int, input().split())
# coins = list(int(input()) for _ in range(N))
# coins.reverse()
# # print(coins)

# ans = 0
# for coin in coins:
#     ans += K // coin
#     K %= coin
#     # print(f'coin: {coin}, K: {K}, ans: {ans}')
# print(ans)




# #수리공 항승
# #1.
# N, L = map(int, input().split())
# coord = [False]*1001
# for i in map(int, input().split()):
#     coord[i]= True

# ans =0
# x=0
# while x< 1001:
#     if coord[x]:
#         ans += 1
#         x += L
#     else:
#         x += 1


# print(ans)

# #2. 
