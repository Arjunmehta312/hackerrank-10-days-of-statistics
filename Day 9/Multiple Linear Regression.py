from sklearn import linear_model

m, n = list(map(int, input().strip().split()))
x_values = [0] * n
y_values = [0] * n

for i in range(n):
    inp = list(map(float, input().strip().split()))
    x_values[i] = inp[:-1]
    y_values[i] = inp[-1]

lm = linear_model.LinearRegression()
lm.fit(x_values, y_values)
intercept = lm.intercept_
coefficients = lm.coef_

q = int(input())

for i in range(q):
    features = list(map(float, input().strip().split()))
    y_pred = intercept + sum([coefficients[j] * features[j] for j in range(m)])
    print(round(y_pred, 2))