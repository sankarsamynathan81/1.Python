class multipleFunctionsTest():
    def OddEven():
        nameData=int(input("Enter a number"))
        if (nameData % 2 != 0):
            print(nameData,"is Odd number")
            message="Odd number"
        else:
            print(nameData,"is Even number")
            message="even number"
        return message
        
    def bmiCalculation():
        thisBMI=int(input("Enter the BMI Index"))
        if thisBMI < 18.5: 
            print ("Underweight")
            message="Underweight"
        elif  18.5 <= thisBMI <= 24.99:
            print ("Normal, keep it up!")
            message="Normal, keep it up!"
        elif  25 <= thisBMI <= 29.99:
            print ("Overweight, exercise more!")
            message="Overweight, exercise more!!"
        elif 30 <= thisBMI <=  39.99:
            print ("Very Overweight")
            message="Very Overweight"
        elif thisBMI >=40:
            print ("Morbidly Obese - take action!")
            message="Morbidly Obese - take action!"
        else:  
            print("Please check your input values, BMI cannot be calculated.")
            message ="Test Morbidly Obese - take action!"
        return message
    def percentage():
        subject1 = 98
        subject2 = 87
        subject3 = 95
        subject4 = 95
        subject5 = 93
        nums = [subject1,subject2,subject3, subject4,subject5]
        total = sum(nums)
        avg = sum(nums) / len(nums)
        print("Total=",total)
        print("Average=",avg)
        return avg
        
    def triangle():
        height=32
        breath=34
        print("Area formula : (Height*Breath)/2")
        triangle=0.5*height*breath
        print("Area of Triangle :",triangle)
        height1=2
        height2=4
        breathval=4
        print("Height1 :",height1)
        print("Height2 :",height2)
        print("Breath :",breathval)
        perimeter = height1+height2+breathval
        print("Perimeter formula = Height1+Height2+Breath")
        print("Perimeter of Triangle = ",perimeter)
