def printAll(seq, margin):
    blanks = " " * margin
    print(blanks, seq)
    if seq:
        print(blanks, seq[0])
        printAll(seq[1:])
