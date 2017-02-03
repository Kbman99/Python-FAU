while True:
    # Initialize the variables to zero at the beginning of each loop
    amount = float(input("Enter amount: "))
    original_amount = amount

    if amount < 0:
        print("Please enter a non-negative and non-zero value...")
    elif amount >= 0:
        # use round when doing floating point arithmetic/algebra to make up for limitations
        if amount >= 0.25:
            quarter_count = int(amount / 0.25)
            amount = round(amount % 0.25, 2)
            # amount = round(amount - quarter_count * 0.25, 2)
        if amount >= 0.10:
            dime_count = int(amount / 0.10)
            amount = round(amount % 0.10, 2)
        if amount >= 0.01:
            penny_count = int(amount / 0.01)
            amount = round(amount % 0.01, 2)

        coin_count = quarter_count + dime_count + penny_count
    if original_amount >= 0:
        # format string to print in specific order and to display proper decimal places
        print("${:.2f} makes {} quarters, {} dimes, and {} pennies ({} coins total), \
total amount in coins: ${:.2f}.".format(original_amount, quarter_count, dime_count,
                                        penny_count, coin_count, original_amount))
