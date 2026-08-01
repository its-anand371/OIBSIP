def get_positive_value_weight():
    valid=False
    while not valid:
        weight=input("The weight of the person is : ")
        try:
            number=float(weight)
            if(number<=0):
                print("The Entered Weight is Incorrect, Please try again and enter a positive number ")
                continue
            else:
                valid=True 
                return number 
        except ValueError :
            print(f"The value you have entered is invalid, Please try again ")    
def get_positive_value_height():
    valid=False 
    while not valid:
        height=input("Enter the value of height in meters : ")
        try:
            number=float(height)
            if(number<=0):
                print("The value of height entered is invalid , Please try again.")
                continue
            else:
                valid=True
                return number
        except ValueError:
            print("The value Entered is invalid, Please try again.")
def calculate_bmi(weight,height):
    return weight/(height*height)
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
def main():
    print("--BMI CALCULATOR--")
    weight=get_positive_value_weight()
    height=get_positive_value_height()

    bmi=calculate_bmi(weight,height)
    category=classify_bmi(bmi)

    print(f"Your BMI is : {bmi:.2f}")
    print(f"Acc to the your weight and height by bmi farmula you are classified as : {category}")
if __name__ == "__main__":
    main()