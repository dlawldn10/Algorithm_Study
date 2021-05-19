#https://programmers.co.kr/learn/courses/30/lessons/12947
#하샤드 수

#내 답
def solution(x):
    sum=0
    answer = True
    x_save = x
    while x>0:
        sum+=x%10
        x=x//10
    if(x_save%sum == 0):
        answer = True
    else:
        answer = False

    return answer



#다른 사람 풀이1
#str(n) -> 숫자n을 문자열로 변환시키는 함수
#int() -> int형으로 변환하는 함수
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0      

#n을 string으로 만들고 sttring 요소 하나하나를 int로 변환한다. 그후 총합을 구하고 n으로 나눠 떨어지는지 확인 후 true/false 리턴


