def lcm(first_number, second_number):
    return (first_number * second_number) / gcd(first_number, second_number)


def gcd(first_number, second_number):
    if second_number == 0:
        return first_number
    else:
        return gcd(second_number, first_number % second_number)
    