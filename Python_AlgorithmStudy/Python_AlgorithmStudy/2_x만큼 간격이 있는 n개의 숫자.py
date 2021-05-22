#https://programmers.co.kr/learn/courses/30/lessons/12954?language=python3
#x만큼 간격이 있는 n개의 숫자

#내 답
def solution(x, n):
    answer = []
    a=x
    for i in range(1,n+1):
        answer.append(x)
        x+=a
    return answer
    


#다른 사람 풀이
#문자열 곱셈
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]    #i가 n-1까지 라서 i * x + x 
print(number_generator(2, 5))


