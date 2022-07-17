def name_sorter(list_names):
    return {'female':sorted([name for name in list_names if name[-1] == 'a']),
            'male':sorted([name for name in list_names if name[-1] != 'a'])}

names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
print(name_sorter(names))

