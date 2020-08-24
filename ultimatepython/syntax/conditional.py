def main():
    x = 1
    x_add_two = x + 2

    # This condition is obviously true
    if x_add_two == 3:
        print("Math wins")  # run

    # A negated condition can also be true
    if not x_add_two == 1:
        print("Math wins here too")  # run

    # There are `else` statements as well, which run if the initial condition
    # fails. Notice that one line gets skipped, and that this conditional
    # does not help one make a conclusion on the variable's true value
    if x_add_two == 1:
        print("Math lost here...")  # skip
    else:
        print("Math wins otherwise")  # run

    # The `else` statement also run once every other `if` and `elif` condition
    # fails. Notice that multiple lines get skipped, and that all of the
    # conditions could have been compressed to `x_add_two != 3`
    # for simplicity. In this case, less is more
    if x_add_two == 1:
        print("Nope not this one...")  # skip
    elif x_add_two == 2:
        print("Nope not this one either...")  # skip
    elif x_add_two < 3 or x_add_two > 3:
        print("Nope not quite...")  # skip
    else:
        print("Math wins finally")  # run


if __name__ == "__main__":
    main()
