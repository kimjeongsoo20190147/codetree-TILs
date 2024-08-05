def max_histogram_area(histogram):
    max_area = 0

    for i in range(n):
        if histogram[i] == 0:
            continue
        
        # 왼쪽으로 확장
        left = i
        while left > 0 and histogram[left - 1] >= histogram[i]:
            left -= 1
        
        # 오른쪽으로 확장
        right = i
        while right < n - 1 and histogram[right + 1] >= histogram[i]:
            right += 1
        
        # 현재 높이를 기준으로 면적 계산
        width = right - left + 1
        area = width * histogram[i]
        max_area = max(max_area, area)
    
    return max_area

def max_rectangle_area(matrix):
    if not matrix or not matrix[0]:
        return -1
    
    n = len(matrix)
    m = len(matrix[0])
    
    # 초기 히스토그램 초기화
    histogram = [0] * m
    max_area = 0
    
    for row in matrix:
        for i in range(m):
            if row[i] > 0:
                histogram[i] += 1
            else:
                histogram[i] = 0
        max_area = max(max_area, max_histogram_area(histogram))
    
    return max_area if max_area > 0 else -1

# 입력 처리
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(max_rectangle_area(matrix))