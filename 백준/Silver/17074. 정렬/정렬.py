def solve():
    # 입력 처리
    N = int(input())  # 수열의 길이
    vec = [0] * (N + 2)
    vec[0] = -1000000000
    vec[N + 1] = 1000000000
    
    # 수열 전체 입력을 한 번에 처리
    arr = list(map(int, input().split()))
    for i in range(1, N + 1):
        vec[i] = arr[i - 1]  # 배열에 수열 저장
    
    cnt = 0
    before_dec = 0
    after_dec = 0
    
    # 오름차순 위반 확인
    for i in range(1, N + 1):
        if vec[i] < vec[i - 1]:
            cnt += 1
            before_dec = i - 1
            after_dec = before_dec + 1
    
    if cnt == 0:
        ans = N
    elif cnt > 1:
        ans = 0
    else:
        ans = 0
        if vec[before_dec - 1] <= vec[after_dec]:
            ans += 1
        if vec[before_dec] <= vec[after_dec + 1]:
            ans += 1
    
    # 결과 출력
    print(ans)

# 함수 호출
solve()
