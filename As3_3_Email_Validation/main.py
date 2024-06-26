def main():
    """
    This program evaluates a user inputted email address.
    The email length must be greater than 5 and less than 30, and include the '@' symbol.
    The email address must begin with an alphabet character, which can be upper or lower case.
    Email address must include at least one '.' after '@'.
    """

    # Difference between find() and index()
    #   index(): Raises a ValueError if the substring is not found.
    #   find(): Returns -1 if the substring is not found.
    # When to Use Which
    #   Use index() if you want the program to raise an error when the substring is not found.
    #   Use find() if you prefer to handle the absence of the substring more gracefully by checking if the returned index is -1.
    
    email = input('Enter your email: ')
    
    count_at_symbol = email.count('@')
    find_at_symbol_index = email.find('@')
    email_sliced_after_at = email[find_at_symbol_index + 1:]
    count_dot_symbol_after_at = email_sliced_after_at.count('.')

    if not(5 < len(email) < 30) or count_at_symbol != 1 or count_dot_symbol_after_at != 1 \
        or not email[0].isalpha:
        result = False
    else: 
        result = True
    
    print(f'Email address entered: {email}. Email address validity: {result}.')

    # or email[0] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    return result


if __name__ == '__main__':
    main()
