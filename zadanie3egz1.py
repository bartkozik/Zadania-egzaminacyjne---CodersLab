def check_palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


print(check_palindrome('Kobyła ma mały bok'))