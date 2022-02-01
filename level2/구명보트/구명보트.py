from collections import deque

def solution(people, limit):
    answer = 0
    d = deque()
    people.sort()
    d.extend(people)
    # print(d)
    i = 0
    while len(d) > 1:
        if d[i] + d.pop() <= limit:
            answer +=1
            d.popleft()
        else:
            answer +=1
    answer += len(d)
    return answer
