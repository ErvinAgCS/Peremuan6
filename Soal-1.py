# 9 
# 8 7
# 7 6 5 
# 6 5 4 3
# 5 4 3 2 1

rows = 5
col = 9

for i in range(rows):
    for j in range(i+1):
        print(col, end=' ')
        col -= 1
    print()
    col += i