n,s = map(int, input().split())

numbers = list(map(int, input().split()))



def find_closest_sum(n,s,numbers):
    total_sum = sum(numbers)
    closest_diff = float('inf')

    for i in range(n):
        for j in range(i+1,n):
            current_sum = total_sum - (numbers[i] + numbers[j])
            current_diff = abs(current_sum - s)

            if current_diff < closest_diff:
                closest_diff = current_diff

    return closest_diff


result = find_closest_sum(n,s,numbers)
print(result)