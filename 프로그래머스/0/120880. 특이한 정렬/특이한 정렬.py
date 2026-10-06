def solution(numlist, n):
    # 큰 수를 맨 앞으로 정렬하자(reverse = True)
    numlist = sorted(numlist, reverse = True)
    answer = []
    # 범위 잘 확인하기range(10000)
    # d = distance 거리를 d로 둘 것.
    for d in range(10000) :
        for num in numlist :
    # 절댓값써보자 abs()        
            if abs(num - n) == d:
                answer.append(num)
    return answer