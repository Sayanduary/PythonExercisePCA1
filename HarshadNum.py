def checkHarshad(n):

    digit_sum = 0

    temp = n

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    if n % digit_sum == 0:
        print(f"{n} is a Harshad number.")
    else:
        print(f"{n} is not a Harshad number.")


checkHarshad(21)
