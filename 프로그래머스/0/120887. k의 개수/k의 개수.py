def solution(i, j, k):
    answer = 0
    
    # i부터 j까지 하나씩 돌기
    for num in range(i, j+1):   
    # k등장해야하고, count()는 문자를 셀 수 있으니 k를 str()로 감싸기
        answer += str(num).count(str(k))
    return answer