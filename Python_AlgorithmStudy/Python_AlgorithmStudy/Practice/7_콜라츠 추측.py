#https://programmers.co.kr/learn/courses/30/lessons/12943
#콜라츠 추측

#내 답
def solution(num):
    answer = 0
    while(num!=1 and answer < 500):
        if(num%2 == 0):
            num/=2
        else:
            num = num*3 +1
        answer+=1

    if(answer >= 500):
        answer = -1
        
    return answer



#다른 사람 풀이
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1
