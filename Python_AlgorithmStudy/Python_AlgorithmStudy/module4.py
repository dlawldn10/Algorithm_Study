#https://programmers.co.kr/learn/courses/30/lessons/12948
#핸드폰 번호 가리기

#내 답
def solution(phone_number):
    answer = ''
    for i in range(len(phone_number) - 4):
        answer += '*'
    for i in range(len(phone_number) - 4, len(phone_number)):
        answer += phone_number[i]
        
    return answer



#다른 사람 풀이1
#문자열 곱셈!!
def hide_numbers(s):
  return '*' * (len(s) - 4) + s[-4:]
