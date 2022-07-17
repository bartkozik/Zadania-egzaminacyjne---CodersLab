def shortend(word):
    shorten = word.split()
    new =''
    for i in range(len(shorten)):
        new += shorten[i][0]
    return new.upper()

d = shortend('jak sie poscielisz tak sie wyspisz')
print(d)
