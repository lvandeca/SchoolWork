def main():
    a = 12345678901234567890
    a1 = 12345678901234567890
    p = 10101010101010101073
    list_of_primes = [2,3,5,7,11,13]
    check = 1
    for prime in list_of_primes:
        assert (check * a) == a1
        while (a % prime) == 0:
            check = prime * check
            a = int(a/prime)
    return a


if __name__ == '__main__':
    main()