# n 값을 입력받습니다.
n = int(input())

# 첫 번째 줄부터 n번째 줄까지 출력
for i in range(1, n + 1):
    print(" " * (2 * (n - i)) + "@ " * i)

# n-1번째 줄부터 마지막 줄까지 출력
for i in range(n - 1, 0, -1):
    print("@ " * i + " " * (2 * (n - i)))