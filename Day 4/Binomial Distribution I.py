from math import factorial, pow

def binomial(n, x, p):
    if p < 0 or p > 1 or n < 0 or x < 0 or x > n:
        return None
    return combinations(n, x) * pow(p, x) * pow(1 - p, n - x)

def combinations(n, x):
    if n < 0 or x < 0 or x > n:
        return None
    return factorial(n) // (factorial(x) * factorial(n - x))

def main():
    ratio = 1.09
    p = ratio / (1 + ratio)
    n = 6

    result = 0
    for x in range(3, n + 1):
        result += binomial(n, x, p)

    print(f"{result:.3f}")

if __name__ == "__main__":
    main()