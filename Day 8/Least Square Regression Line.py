def calculate_mean(values):
    '''To calculate the mean'''
    return sum(values) / len(values)

def least_square_regression(x_values, y_values):
    '''To calculate the Least Square Regression'''
    b = sum([(x_values[i] - calculate_mean(x_values)) * (y_values[i] - calculate_mean(y_values))
             for i in range(len(x_values))]) / sum([(j - calculate_mean(x_values)) ** 2 for j in x_values])
    a = calculate_mean(y_values) - (b * calculate_mean(x_values))
    return a + (b * 80)

x_values = []
y_values = []

for _ in range(5):
    a, b = list(map(int, input().split()))
    x_values.append(a)
    y_values.append(b)

print(round(least_square_regression(x_values, y_values), 3))