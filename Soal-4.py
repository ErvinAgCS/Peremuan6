# 1 3 5 6 7
# 2 5 8 11 14
# 3 7 11 15 19
# 4 9 13 17 21
# 5 11 15 19 23

rows = 5
start_col = 1
increment_main = 2
increment_row = 1

for i in range(rows):
    col = start_col
    for j in range(rows):
        print(col, end=' ')
        col += increment_row
    start_col += increment_main
    increment_row += 2
    print()
    
    
# Masih Salah