# Adrian - A, B, C, A, B, C
# Bruno - B, A, B, C, B, A
# Goran - C, C, A, A, B, B

adrian_pattern = ["A", "B", "C"]
bruno_pattern = ["B", "A", "B", "C"]
goran_pattern = ["C", "C", "A", "A", "B", "B"]

totals = [0]*3
names =  ["Adrian", "Bruno", "Goran"]

input()
answer_key = input()
for index, answer in enumerate(answer_key):
    if answer == adrian_pattern[index % 3]:
        totals[0] += 1
    if answer == bruno_pattern[index % 4]:
        totals[1] += 1
    if answer == goran_pattern[index % 6]:
        totals[2] += 1
#    print(totals)

highest_score = max(totals)
print(highest_score)
for index, score in enumerate(totals):
    
    if score == highest_score:
        print(names[index])
