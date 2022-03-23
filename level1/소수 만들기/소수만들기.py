from itertools import combinations
def find_primeNum(num):
    for j in range(2,num//2):
        if num % j == 0: #소수가 
            return False
    return True

    
def solution(nums):
    answer = 0
    lst = list(combinations(nums,3)) #3개 가능한 조합 리스트
    for i in lst:
        num = sum(i)
        if find_primeNum(num):
            answer += 1

    return answer
