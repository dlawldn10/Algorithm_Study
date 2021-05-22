#https://programmers.co.kr/learn/courses/30/lessons/12969
#직사각형 별찍기

#내 답
a, b = map(int, input().strip().split(' '))
for i in range(1, b+1):
        for k in range(1, a+1):
            print("*", end = "")
        print(' ')
    


#다른 사람 풀이
#문자열 곱셈
a, b = map(int, input().strip().split(' '))
print(('*' * a + '\n') * b)
