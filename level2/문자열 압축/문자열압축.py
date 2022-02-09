def solution(s):
    answer = 1
    pre = ''
    now = ''
    lst = []
    for j in range(1,len(s)//2+1):
        t = 0
        total = 0
        k = 0
        tmp = [s[i:i+j] for i in range(0, len(s), j)]
        cnt = [1]*len(tmp)
        result = ''
        while k < len(tmp):
            
            now = tmp[k]
            if pre != now:
                pre = now
                k += 1
                t += 1
            else:
                cnt[t] += 1
                del tmp[k]
        for h in range(len(cnt)):
            if cnt[h] != 1:
                result += str(cnt[h])
        result += (''.join(tmp))
        lst.append(len(result))
                
        print(tmp)
        print(cnt)
        print(result)
    if len(lst) > 1:
        answer = min(lst)

            
    return answer
