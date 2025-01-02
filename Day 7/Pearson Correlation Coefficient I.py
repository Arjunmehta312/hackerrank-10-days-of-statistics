def standard_deviation(values):
    return (sum([(i - (sum(values)) / len(values)) ** 2 for i in values]) / len(values)) ** 0.5

n = int(input())
x_values = list(map(float, input().split()))
y_values = list(map(float, input().split()))

x_mean = sum(x_values) / len(x_values)
y_mean = sum(y_values) / len(y_values)

x_std = standard_deviation(x_values)
y_std = standard_deviation(y_values)

print(round(sum([(i - x_mean) * (j - y_mean) for i, j in zip(x_values, y_values)]) / (n * x_std * y_std), 3))