n = int(input())
arr = list(map(int, input().split()))

is_ascending = all(arr[i] <= arr[i + 1] for i in range(n - 1))
is_descending = all(arr[i] >= arr[i + 1] for i in range(n - 1))

if is_ascending or is_descending:
    print(0)
else:
    sorted_arr = sorted(arr)
    count = sum(a != b for a, b in zip(arr, sorted_arr))
    print(count // 2)
