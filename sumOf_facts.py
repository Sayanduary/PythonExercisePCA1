def factorial(N):
    if N == 1:
        return 1
    return N * factorial(N - 1)


def SeriesOfSum(N):
    sum = 0
    for i in range(1, N + 1):
        fact = factorial(i)

        sign = fact

        if i % 2 == 0:
            sign = sign * -1
        sum += sign

    return sum


N = 6
print(SeriesOfSum(N))
