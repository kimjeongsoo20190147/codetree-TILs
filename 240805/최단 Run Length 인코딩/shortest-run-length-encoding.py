s = input().strip()

def run_length_encoding_length(s):
    if not s:
        return 0  # 빈 문자열이면 0을 반환
    
    encoded_length = 0  # 인코딩된 문자열의 길이를 저장할 변수
    count = 1  # 현재 문자의 반복 횟수를 저장할 변수
    current_char = s[0]  # 현재 문자를 초기화
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1  # 현재 문자가 이전 문자와 같으면 카운트를 증가
        else:
            encoded_length += 1 + len(str(count))  # 현재 문자와 반복 횟수의 길이를 더함
            current_char = s[i]  # 현재 문자를 업데이트
            count = 1  # 카운트를 1로 초기화
    
    encoded_length += 1 + len(str(count))  # 마지막 문자와 반복 횟수를 더함
    
    return encoded_length  # 최종 인코딩된 문자열의 길이를 반환

def min_run_length_encoding(s):
    n = len(s)  # 문자열의 길이
    min_length = float('inf')  # 최소 길이를 무한대로 초기화
    
    for shift in range(n):
        shifted_s = s[-shift:] + s[:-shift]  # 문자열을 오른쪽으로 shift
        encoded_length = run_length_encoding_length(shifted_s)  # shift된 문자열의 인코딩 길이를 계산
        min_length = min(min_length, encoded_length)  # 최소 인코딩 길이를 업데이트
    
    return min_length  # 최소 인코딩 길이를 반환

print(min_run_length_encoding(s))