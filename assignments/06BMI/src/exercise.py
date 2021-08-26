def main(weight, height):
    return(weight/(height**2))

weight = float(input("Insert your weight (kg): "))

if (weight <= 0):
    print("Incorrect information. Please try again.")
    
height = float(input("Insert your height (m): "))
if (height <= 0):
    print("Incorrect information. Please try again.")

bmi = weight/(height**2)

if (bmi < 20):
    print("Underweight")
 
elif (bmi >= 20 and bmi < 25):
    print("Healthy")
 
elif (bmi >= 25 and bmi < 30):
    print("Overweight")
    
elif (bmi >= 30 and bmi < 40):
    print("Obesity")
 
elif (bmi >=40):
    print("Morbid Obesity")
