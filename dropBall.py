def main():


    height=float(input("Enter the height from which the ball is dropped in feet: \n"))

   
    BOUNCINESS=.6

   
    bounces=int(input("Enter the number of times the ball is allowed to continue bouncing: \n"))

   
    distance=0

    while bounces > 0:
        distance = distance + height 
        height = height * BOUNCINESS 
        distance = distance + height 

        
        bounces -= 1

        print("Total distance traveled is ", distance)

main()
