import math

sample = 100
mean = 500
sd = 80
z = 1.96
rng = 0.95

print(round(-z * (sd / math.sqrt(sample)) + mean, 2))
print(round(z * (sd / math.sqrt(sample)) + mean, 2))