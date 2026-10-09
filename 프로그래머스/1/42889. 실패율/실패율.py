def solution(N, stages):
    # 1. 처음 도달한 사람 = 전체인원
    people = len(stages)
    # 실패율 기록
    fail = {} # 리스트 []는 빈칸이 없어서 못쓰니까 {}
    
    # 2. 스테이지 1부터 N까지 돌기(for반복문)
    for stage in range(1, N+1) :
    # 근데 스테이지마다 막힌 사람이 있으니 count
        n_people = stages.count(stage)
    
    # 3. 실패율 계산(근데 도달한 사람 0명이면 실패율 0)
        if people == 0 :
            fail[stage] = 0
        else :
    # 위 경우가 아니면 실패율 = 막힌 사람 / 도달사람    
            fail[stage] = n_people / people
    # 다음 스테이지 가기 전에 막힌 사람 빼기
        people = people - n_people
    # 정렬하자! lamda stage : fail[stage] 쓸 것임! 
    answer = sorted(range(1, N+1), key = lambda stage: fail[stage], reverse = True)  
    return answer