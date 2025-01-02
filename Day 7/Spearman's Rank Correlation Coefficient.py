n = int(input())
x_values = list(map(float, input().strip().split()))
y_values = list(map(float, input().strip().split()))

x_copy = x_values.copy()
y_copy = y_values.copy()

x_copy.sort()
xd = dict(zip(x_copy, range(1, n + 1)))

y_copy.sort()
yd = dict(zip(y_copy, range(1, n + 1)))

rx = [xd[i] for i in x_values]
ry = [yd[i] for i in y_values]

print(round(1 - (6 * sum([(rx - ry) ** 2 for rx, ry in zip(rx, ry)])) / ((n ** 3) - n), 3))
