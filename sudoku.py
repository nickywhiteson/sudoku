s = ""
row = 3
for i in sudoku:
    for j, k in enumerate(i):
        if row == 3:
            print((len(sudoku[0])+2) * "- ")
            row = 0
        s += str(k) if j % 3 or j == 0 else "|" + str(k)
    row += 1
    print(*s)
    s = ""
print((len(sudoku[0])+2) * "- ")