while True:
    n_value = int(input("Please enter a value for n: "))
    c_max = n_value
    pythagorean_triples = []

    for c in range(c_max, int(c_max/2) - 1, -1):
        c_value = c
        cc = c_value**2
        for a in range(c_max - 1, int((c_max - 1)/2) - 1, -1):
            a_value = a
            for b in range(a_value - 1, 0, -1):
                b_value = b
                if a_value**2 + b_value**2 == cc:
                    triple = (a_value, b_value, c_value)
                    pythagorean_triples.append(triple)

    for triples in pythagorean_triples:
        print(triples)
    print(pythagorean_triples.count())
