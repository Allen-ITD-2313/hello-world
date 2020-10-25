def main():
    iteration = int(input("Please enter a value for iterations:"))
    total=0
    for i in range(1,iteration):
        total += (-1)**(i+1)*((1.0/(i+i+1)))

    pi = 4*(1-total)
    print(pi)

main()
