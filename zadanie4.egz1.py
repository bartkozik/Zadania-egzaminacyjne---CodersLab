def div(start, stop):
    return [num for num in range(start, stop+1) if num % 2 == 0 and num % 3 != 0]

result = div(0, 20)
print(result)

