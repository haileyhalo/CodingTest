def solution(s):
    answer = ''
    for ele in sorted(s) :
        if s.count(ele) == 1:
            answer += ele
    return answer