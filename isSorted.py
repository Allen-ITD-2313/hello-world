#define the isSorted function
def isSorted(myList):
    if len (myList) == 0 or len (myList) == 1:
        return True
    else:
        for index in range(len(myList) - 1):
            if myList[index] > myList[index +1]:
                return False
    return True

#define the main function

def main():
    myList = []
    print(isSorted(myList))
    myList = [1]
    print(isSorted(myList))
    myList = list(range(10))
    print(isSorted(myList))
    myList[9] = 3
    print(isSorted(myList))

if __name__ == "__main__":
    main()
