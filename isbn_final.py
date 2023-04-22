def check_isbn(isbn_num):
    # Remove whitespaces
    isbn_num = isbn_num.strip()

    # Remove dashes commonly seen in ISBN's
    isbn_num = isbn_num.replace("-", "")

    # Disregard inputs with too many or too little digits
    if len(isbn_num) != 10 and len(isbn_num) != 13:
        print("Invalid")

    # Check if isbn_num is a valid ISBN-13
    elif len(isbn_num) == 13 and isbn_num.isdigit():
        # create a list of all the separate digits in isbn_num
        digits = [int(d) for d in str(isbn_num)]
        # create an alternating pattern of 1 and 3 for the multipliers
        multipliers = [1 if i % 2 == 0 else 3 for i in range(len(digits))]
        # calulate the total
        prod_sum = sum(d * m for d, m in zip(digits, multipliers))

        # Determine validity
        if prod_sum % 10 == 0:
            print("Valid")
        else:
            print("Invalid")

    # check if isbn_num is a valid ISBN-10
    elif len(isbn_num) == 10 and isbn_num[:-1].isdigit() and (isbn_num[-1].isdigit() or isbn_num[-1] == 'X'):
        # replace X with 10 & separate digits accordingly
        if isbn_num[-1] == 'X':
            digits = [int(d) for d in str(isbn_num[:-1])] + [10]
        # No X, just create a list of all the separate digits in isbn_num
        else:
            digits = [int(d) for d in str(isbn_num)]
        # create a list of the numbers 10 to 1 in reverse order
        multipliers = list(range(10, 0, -1))
        # calculate the total
        prod_sum = sum(d * m for d, m in zip(digits, multipliers))

        # Determine validity
        if prod_sum % 11 == 0:
            # convert to ISBN-13 format
            isbn13_num = "978" + isbn_num[:-1]

            # check if isbn13_num is a valid ISBN-13
            # create a list of all the separate digits in isbn13_num
            digits = [int(d) for d in str(isbn13_num)]
            # create an alternating pattern of 1 and 3 for the multipliers
            multipliers = [1 if i % 2 == 0 else 3 for i in range(len(digits))]
            # calulate the total
            prod_sum = sum(d * m for d, m in zip(digits, multipliers))
            # calculate check digit
            check_digit = (10 - (prod_sum % 10)) % 10
            # concatenate to produce the ISBN-13
            isbn13_num += str(check_digit)
            print("Valid")
            print(f"The ISBN-13 version is: {isbn13_num}")
        else:
            print("Invalid")

    else:
        print("Invalid")

while True:
    # Receive input ISBN for the user
    isbn_num = input("Please provide the ISBN number of your book (or enter 'exit' to quit): ")

    if isbn_num.strip().lower() == 'exit':
        print("Goodbye!")
        break
        
    check_isbn(isbn_num)