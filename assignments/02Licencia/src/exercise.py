def main():
    return()

age = int(input("Insert your age: "))

if age >= 18:
   
   legal_license = input("Do you have a license? (Y/N): ")
   
   if legal_license == "Y":
    print("You're eligible for a license")
   elif legal_license == "N":
    print("You're not eligible for a license")
   else:
    print("Incorrect information. Please try again.")

elif age < 18:
   print("You're not eligible for a license")
