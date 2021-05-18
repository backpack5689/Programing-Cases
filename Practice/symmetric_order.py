number_entries = int(input())
total_sets = 1
while number_entries != 0:
    print("SET", total_sets)
    total_sets += 1 
    names = []
    for i in range(number_entries):
        # If it's an even entry, put it in the middle
        if i % 2 == 0:
            names.insert(int(i/2), input())
        else:
            names.insert(len(names)-int((i/2)), input())
    for item in names:
        print(item)
    number_entries = int(input())
