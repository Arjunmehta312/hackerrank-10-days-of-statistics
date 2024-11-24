# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

# Read input values
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate mean
mean = sum(arr) / n
print(f"{mean:.1f}")

# Calculate median
arr.sort()
if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2
print(f"{median:.1f}")

# Calculate mode
frequency = {}
for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

max_freq = max(frequency.values())
mode = min(k for k, v in frequency.items() if v == max_freq)
print(mode)
