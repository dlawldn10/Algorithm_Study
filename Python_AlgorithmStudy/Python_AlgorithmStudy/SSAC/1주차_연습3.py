#1.
# ord함수는 문자를 아스키 코드로
# chr함수는 아스키 코드를 문자로 변환해준다.
# asc = input()
# print(ord(asc))


#2.
# N = int(input())
# print(sum(map(int, str(input()))))


#3.
# N = list(map(str, str(input())))

# alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o","p","q","r","s","t","u","v","w","x","y","z"]
# ans = [-1]*26
# for i in range(0, len(N)):
#     for j in range(0, len(alp)):
#         if (N[i] == alp[j]) and (ans[j] == -1):
#             ans[j] = i

# for i in range(0, len(ans)):
# 	print(ans[i], end=' ')


#4.
# import sys
# T = int(sys.stdin.readline())

# for j in range(0, T):
#     R, tmp = map(str, sys.stdin.readline().split())

#     for k in range(0, len(tmp)):
#         for i in range(0, int(R)):
#             print(tmp[k], end=' ')
#     print()


#다른사람 풀이
# n = int(input())

# for _ in range(n):
#     cnt, word = input().split()
#     for x in word:
#         print(x*int(cnt), end='')  # end='' 옆으로 붙임
#     print()  # 줄넘김



#5.
#다른 사람 풀이
#리스트에서 같은 요소 제거/세는 방법
# words = input().upper()
# unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

# cnt_list = []
# for x in unique_words :
#     cnt = words.count(x)
#     cnt_list.append(cnt)  # count 숫자를 리스트에 append

# if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
#     print('?')
# else :
#     max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
#     print(unique_words[max_index])


#6.
# words = list(map(str, input().split()))
# print(len(words))


#7.
#프린트에 if문 쓰기
# A, B = map(str, input().split())
# a = int(A[::-1])
# b = int(B[::-1])

# print(a if a>b else b)


#8.
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# alp = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
# ans = list()

# word = str(input())
# for i in range(0, len(word)):
#     for j in range(0, len(alp)):
#         for k in range(0, len(alp[j])):
#             if word[i] == alp[j][k]:
#                 ans.append(num[j])

# print(2*len(word) + sum(ans))


#9.
#문자열을 한글자씩 입력받는 방법
# words = list(input())

#다른 사람 풀이
#똑같은 요소가 있으면 대체한다.
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()

# for i in croatia :
#     word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
# print(len(word))



#10.
#다른 사람 풀이
#같은 요소가 있는 문자열 검사할때 참고할 것.
# N = int(input())
# result = N
# for i in range(0,N):
#     word=input()
#     for j in range(0,len(word)-1):
#         if word[j]==word[j+1]:
#             pass
#         elif word[j] in word[j+1:]:#이 뒤에 있는 문자들 중 일치하는 것이 있으면. 와 대박.
#             result-=1   #result에서 하나를 뺀다.
#             break
# print(result)



#11.
#내 풀이 -> 시간초과
# A, B, C = map(int, input().split())
# i = 1
# if B >= C:
#     print(-1)
# else:
#     while A + B*i >= C*i:
#         i+=1
#     print(i)

#다른 사람 풀이 -> 손익분기점 공식 이용.
# A, B, C = map(int, input().split())
# if B >= C:
#     print(-1)
# else:
#     print(int(A/(C-B) + 1))



#12.
#다른사람 풀이
#가장 적게 들 수 있는 방법 -> 5킬로 설탕을 최대한 많이 들기
#따라서 5의 배수가 될때까지 3킬로 설탕을 더해간다.
#그러다가 5의 배수가 되지 않아서 n값이 음수가 되면 -1을 출력한다. n값에 5와 3으로 딱 맞출 수 없다는 뜻이므로.
# n = int(input()) # 설탕

# result = 0 # 봉지 수

# while n >= 0:
#     if n % 5 == 0: # 5로 나눈 나머지가 0인 경우
#         result += n // 5 # 5로 나눈 몫 출력
#         print(result)
#         break
#     n -= 3 # 설탕이 5의 배수가 될때까지 반복
#     result += 1 # 봉지 추가
# else:
#     print(-1) # while문이 거짓이 되면 -1 출력


#13.
# N = int(input())
# a = 1
# count = 1
# while a<N:
#     a=a+6*count
#     count += 1
# print(count)


#14.
#내풀이
# N = int(input())
# sum = 0
# count = 0
# while sum < N:
#     count += 1
#     sum += count
# if count %2 == 0:   #count가 짝수인경우
#     print(str((count-(sum-N))) + "/" + str((1+(sum-N))))
# else:
#     print(str((1+(sum-N))) + "/" + str((count-(sum-N))))


#15.
#내풀이 -> 시간초과
# A, B, V = map(int, input().split())
# count = (V//A)
# height = count*A - count*B
# while height < V:
#     count += 1
#     height += A
#     if height >= V:
#         pass
#     else:
#         height -= B
    
# print(count)

#다른사람 풀이
#A-B = 하루동안 올라가는 거리임을 이용하여 직접 계산하기
#반올림 해주는 함수
# import math
# A, B, V = map(int, input().split())
# day = (V - B) / (A - B)
# print(math.ceil(day))



#16.
# T = int(input())

# for k in range(T):
#     H, W, N = map(int, input().split())
#     count = 0
#     for i in range(0, W):
#         for j in range(0, H):
#             count += 1
#             if count == N:
#                 print(100*(j+1) + (i+1))


#17.
# T = int(input())
# for i in range(T):
#     K = int(input())
#     N = int(input())

#     num = [[0]*N]
#     for i in range(0, N):
#         num[0][i] = i+1
#     num = num + [[1]*N for _ in range(1, K+1)]
#     for i in range(0, K):
#         for j in range(0, N-1):
#             num[i+1][j+1] = num[i][j+1] + num[i+1][j]
#     print(num[K][N-1])



#18.
#1011번. 모르겠음...
#다른 사람 풀이
# t = int(input())

# for _ in range(t):
#     x, y = map(int,input().split())
#     distance = y - x
#     count = 0  # 이동 횟수
#     move = 1  # count별 이동 가능한 거리
#     move_plus = 0  # 이동한 거리의 합
#     while move_plus < distance :
#         count += 1
#         move_plus += move  # count 수에 해당하는 move를 더함
#         if count % 2 == 0 :  # count가 2의 배수일 때, 
#             move += 1  
#     print(count)


#19.
#5분, 1분, 10초
#모르겠음 부분점수.
# T = int(input())
# times = list(150, 60, 10)
# A = 150
# B = 60
# C = 10

# a = T//A
# T = T%A
# b = T//B
# T = T%B
# c = T//C
# T = T%C
# if T > 0:
#     print(-1)
# else:
#     print(a, b, c)


#20.
# L = list(input())
# reverseCount = 0
# count = 0
# for i in range(0, len(L)):
#     if i+1 == len(L):
#         break
#     if L[i] != L[i+1]:
#         reverseCount += 1
    
# print(reverseCount//2 + reverseCount%2)