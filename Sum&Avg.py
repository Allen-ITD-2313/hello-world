def main():

    count = 0
    sum = 0.0
    product = 1.0
    data = input("Enter a number or press Enter to quit: ")

    while True: 
        data = input("Enter a number or press Enter to quit: ")
            
        if data == "":
            break

        number = float(data)
        
        sum += number
        product *= number
        average = sum / number

    
    print("The sum is", sum)
    print("The average is", average)
main()

