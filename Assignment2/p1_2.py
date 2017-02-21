'''while True:
    n_value = int(input("Please enter a value for n: "))
    pythagorean_triples = []

    for a in range(1, n_value, 1):
        aa = a * a
        b = a + 1
        c = b + 1
        while c <= n_value:
            cc = aa + b * b
            while c * c < cc:
                c += 1
            if c * c == cc and c <= n_value:
                triple = (a, b, c)
                pythagorean_triples.append(triple)
            b += 1
    for triples in pythagorean_triples:
        print(triples)
    print(len(pythagorean_triples)'''


def compute_pythagorean(upper_bound: int):
    pythagorean_triples = [(a, b, c) for a in range(1, upper_bound+1) for b in range(a, upper_bound+1)
                           for c in range(b, upper_bound+1) if a**2+b**2 == c**2]
    print(pythagorean_triples)
    print(len(pythagorean_triples))


n_value = int(input("Please enter an upper bound for the value n: "))
compute_pythagorean(n_value)
