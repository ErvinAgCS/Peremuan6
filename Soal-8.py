# * 
# * 
# * *
# * * * 
# * * * * *
# * * * * * * * * 
# * * * * * * * * * * * * *
#Palindrome


rows = 7

for i in range(1, rows + 1):
    for j in range( 1-i):
        if j % 2 == 0:
            print("* ", end='')
    print()
    