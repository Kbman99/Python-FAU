while True:
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
    print(len(pythagorean_triples))