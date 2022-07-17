def str_counter(str_sth):
    letters = {}
    if str_sth == str(str_sth):
        for letter in str_sth.replace(' ', ''):
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1
        return letters
    else:
        raise Exception


d = str_counter("ala ma kota")
print(d)