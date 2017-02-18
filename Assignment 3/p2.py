def compute_pythagorean(upper_bound: int):
    try:
        pythagorean_triples = [(a, b, c) for a in range(1, upper_bound) for b in range(a, upper_bound)
                               for c in range(b, upper_bound+1) if a**2+b**2 == c**2]
    except ValueError:
        print("Oops! You entered a value that is not allowed!")
        return []
    return pythagorean_triples


while True:
    try:
        n_value = int(input("Please enter an upper bound for the value n: "))
        triples = compute_pythagorean(n_value)
        print(triples)

    except ValueError:
        print("Oops! You entered a value that is not allowed! Please ensure you entered an integer and not a float")
