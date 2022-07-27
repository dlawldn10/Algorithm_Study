#https://programmers.co.kr/learn/courses/30/lessons/12950
#행렬의 덧셈

#내 답
def solution(arr1, arr2):
    answer = [[] for x in range(len(arr1))]
    for i in range(len(arr1)):
        for k in range(len(arr1[0])):
            answer[i].append(arr1[i][k] + arr2[i][k])
        
    return answer
    


#다른 사람 풀이1
#A에다가 B를 더해감
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A


#다른 사람 풀이2
#numpy 사용
import numpy as np
# -> 벡터/행렬 연산할때 사용
def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()


